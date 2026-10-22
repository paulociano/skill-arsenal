"""Smoke and denial tests for the Arsenal catalog MCP server (stdlib only)."""
import json
import pathlib
import subprocess
import sys
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "mcp"))
import catalog_server


def request(method, ident=1, params=None):
    return {"jsonrpc": "2.0", "id": ident, "method": method,
            "params": params if params is not None else {}}


class CatalogTests(unittest.TestCase):
    def test_initialize(self):
        result = catalog_server.handle(request("initialize"))["result"]
        self.assertEqual(result["serverInfo"]["name"], "arsenal-catalog")
        self.assertIn("tools", result["capabilities"])

    def test_discovery_and_read_only(self):
        tools = catalog_server.handle(request("tools/list"))["result"]["tools"]
        self.assertEqual(len(tools), 3)
        self.assertTrue(all(t["annotations"]["readOnlyHint"] for t in tools))
        self.assertTrue(all(not t["annotations"]["destructiveHint"] for t in tools))

    def test_list_contract(self):
        value = catalog_server.handle(request("tools/call", params={
            "name": "arsenal_list_integrations", "arguments": {}}))["result"]
        self.assertFalse(value["isError"])
        self.assertTrue(value["structuredContent"]["declared_only"])
        self.assertGreater(len(value["structuredContent"]["integrations"]), 0)

    def test_detail_and_compatibility(self):
        response = catalog_server.handle(request("tools/call", params={
            "name": "arsenal_get_integration", "arguments": {"id": "github"}}))
        self.assertEqual(response["result"]["structuredContent"]["integration"]["id"], "github")
        compat = catalog_server.handle(request("tools/call", params={
            "name": "arsenal_client_compatibility"}))
        self.assertEqual(compat["result"]["structuredContent"]["compatibility"]["policy"]["default"], "deny")

    def test_unknown_tool_denied(self):
        response = catalog_server.handle(request("tools/call", params={
            "name": "run_shell", "arguments": {"command": "echo unsafe"}}))
        self.assertTrue(response["result"]["isError"])

    def test_malformed_inputs_denied(self):
        self.assertEqual(catalog_server.handle(request("tools/call", params={
            "name": "arsenal_get_integration", "arguments": {"id": "../secrets"}}))
            ["result"]["isError"], True)
        self.assertEqual(catalog_server.handle(request("tools/call", params={
            "name": "arsenal_list_integrations", "arguments": {"execute": True}}))
            ["result"]["isError"], True)
        self.assertEqual(catalog_server.handle(request("other"))["error"]["code"], -32601)
        self.assertIsNone(catalog_server.handle({"jsonrpc": "2.0", "method": "notifications/initialized"}))

    def test_stdio_round_trip(self):
        commands = [
            request("initialize"), {"jsonrpc": "2.0", "method": "notifications/initialized"},
            request("tools/list", 2),
            request("tools/call", 3, {"name": "arsenal_list_integrations"}),
            request("tools/call", 4, {"name": "unknown"}),
        ]
        process = subprocess.run([sys.executable, str(ROOT / "mcp" / "catalog_server.py")],
            input="\n".join(json.dumps(c) for c in commands) + "\n",
            text=True, capture_output=True, timeout=10, check=True, cwd=ROOT)
        self.assertEqual(process.stderr, "")
        rows = [json.loads(line) for line in process.stdout.splitlines()]
        self.assertEqual([row["id"] for row in rows], [1, 2, 3, 4])
        self.assertEqual(rows[1]["result"]["tools"][0]["name"], "arsenal_list_integrations")
        self.assertTrue(rows[3]["result"]["isError"])


if __name__ == "__main__":
    unittest.main()
