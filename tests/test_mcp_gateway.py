import json
import pathlib
import sys
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "mcp"))
import gateway_server

MOCK = ROOT / "tests" / "fixtures" / "mock_mcp_stdio.py"


class GatewayTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.path = pathlib.Path(self.tmp.name) / "config.json"
        self.write(["echo"])

    def write(self, tools):
        self.path.write_text(json.dumps({"version": 1, "servers": {"mock": {
            "argv": [sys.executable, str(MOCK)], "read_tools": tools}}}), encoding="utf-8")

    def request(self, method, params=None):
        return gateway_server.handle({"jsonrpc": "2.0", "id": 9, "method": method,
                                      "params": params or {}}, self.path)

    def test_handshake(self):
        self.assertEqual(self.request("initialize")["result"]["serverInfo"]["name"], "arsenal-gateway")

    def test_allowlisted_readonly_discovery(self):
        tools = self.request("tools/list")["result"]["tools"]
        self.assertEqual([tool["name"] for tool in tools], ["mock__echo"])

    def test_readonly_execution(self):
        res = self.request("tools/call", {"name": "mock__echo", "arguments": {"value": "hello"}})
        self.assertEqual(res["result"]["content"][0]["text"], "hello")

    def test_unsafe_denied_even_if_allowlisted(self):
        self.write(["echo", "unsafe"])
        self.assertEqual([t["name"] for t in self.request("tools/list")["result"]["tools"]], ["mock__echo"])
        res = self.request("tools/call", {"name": "mock__unsafe", "arguments": {}})
        self.assertTrue(res["result"]["isError"])

    def test_unknown_and_bad_config_fail_closed(self):
        res = self.request("tools/call", {"name": "mock__not-listed"})
        self.assertTrue(res["result"]["isError"])
        self.path.unlink()
        self.assertEqual(self.request("tools/list")["result"]["tools"], [])
        self.assertTrue(self.request("tools/call", {"name": "mock__echo"})["result"]["isError"])

    def test_no_shell_or_relative_executable(self):
        self.path.write_text(json.dumps({"version": 1, "servers": {"mock": {
            "argv": ["python", str(MOCK)], "read_tools": ["echo"]}}}))
        self.assertEqual(self.request("tools/list")["result"]["tools"], [])

    def test_bad_args_rejected(self):
        self.assertEqual(self.request("tools/call", {"name": "mock__echo", "arguments": []})["error"]["code"], -32602)


if __name__ == "__main__":
    unittest.main()
