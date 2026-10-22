#!/usr/bin/env python3
"""Opt-in read-only MCP stdio gateway.

The trusted operator config pins commands and exact tool names. No tool writes,
shell interpretation, HTTP endpoints or implicit catalog-to-execution mapping.
"""
import json
import pathlib
import subprocess
import sys

from catalog_server import error, success

ROOT = pathlib.Path(__file__).resolve().parents[1]
CONFIG = ROOT / "mcp" / "gateway.local.json"
PROTOCOL = "2025-03-26"
MAX_BYTES = 1048576


def configuration(path=CONFIG):
    raw = json.loads(path.read_text(encoding="utf-8"))
    if set(raw) != {"version", "servers"} or raw["version"] != 1 or not isinstance(raw["servers"], dict):
        raise ValueError("Invalid gateway configuration")
    for alias, entry in raw["servers"].items():
        if not alias.replace("-", "").isalnum() or not isinstance(entry, dict):
            raise ValueError("Invalid server alias")
        if set(entry) != {"argv", "read_tools"}:
            raise ValueError("Unexpected configuration fields")
        argv, allowed = entry["argv"], entry["read_tools"]
        if not isinstance(argv, list) or not argv or not all(isinstance(x, str) and x for x in argv):
            raise ValueError("Invalid command")
        if not pathlib.Path(argv[0]).is_absolute():
            raise ValueError("Executable must have absolute path")
        if not isinstance(allowed, list) or not allowed or len(allowed) != len(set(allowed)):
            raise ValueError("Invalid allowlist")
        if not all(isinstance(x, str) and x and "/" not in x for x in allowed):
            raise ValueError("Invalid tool name")
    return raw["servers"]


def exchange(entry, messages, timeout=8):
    payload = "".join(json.dumps(m, ensure_ascii=False) + "\n" for m in messages)
    if len(payload.encode("utf-8")) > MAX_BYTES:
        raise ValueError("Request too large")
    # No shell. Child starts only from a trusted, operator-owned config.
    process = subprocess.run(entry["argv"], input=payload, capture_output=True,
                             text=True, timeout=timeout, check=False)
    if process.returncode != 0 or len(process.stdout.encode("utf-8")) > MAX_BYTES:
        raise ValueError("Downstream server failed")
    answers = {}
    for line in process.stdout.splitlines():
        obj = json.loads(line)
        if isinstance(obj, dict) and "id" in obj:
            if obj["id"] in answers:
                raise ValueError("Duplicate response id")
            answers[obj["id"]] = obj
    return answers


def messages(tool=None, arguments=None):
    out = [
        {"jsonrpc": "2.0", "id": 1, "method": "initialize",
         "params": {"protocolVersion": PROTOCOL, "capabilities": {},
                    "clientInfo": {"name": "arsenal-gateway", "version": "0.1.0"}}},
        {"jsonrpc": "2.0", "method": "notifications/initialized"},
        {"jsonrpc": "2.0", "id": 2, "method": "tools/list", "params": {}},
    ]
    if tool is not None:
        out.append({"jsonrpc": "2.0", "id": 3, "method": "tools/call",
                    "params": {"name": tool, "arguments": arguments}})
    return out


def discover(entry):
    responses = exchange(entry, messages())
    init, listing = responses.get(1, {}), responses.get(2, {})
    if "result" not in init or "result" not in listing:
        raise ValueError("MCP handshake failed")
    tools = listing["result"].get("tools")
    if not isinstance(tools, list):
        raise ValueError("Invalid tools/list")
    names = {tool.get("name") for tool in tools if isinstance(tool, dict)}
    return {tool["name"]: tool for tool in tools
            if isinstance(tool, dict) and tool.get("name") in entry["read_tools"]
            and isinstance(tool.get("inputSchema"), dict)
            and tool.get("annotations", {}).get("readOnlyHint") is True
            and tool.get("annotations", {}).get("destructiveHint") is False
            and sum(t.get("name") == tool.get("name") for t in tools if isinstance(t, dict)) == 1}


def proxy_call(entry, tool, arguments):
    allowed = discover(entry)
    if tool not in allowed:
        raise PermissionError("Tool not approved and confirmed read-only")
    responses = exchange(entry, messages(tool, arguments))
    if "result" not in responses.get(1, {}) or "result" not in responses.get(2, {}):
        raise ValueError("Handshake failed")
    # Recheck tool metadata on the exact process carrying the call.
    listing = responses[2]["result"].get("tools", [])
    matching = [t for t in listing if isinstance(t, dict) and t.get("name") == tool]
    if len(matching) != 1 or matching[0] != allowed[tool]:
        raise ValueError("Tool contract changed")
    result = responses.get(3, {})
    if "result" not in result or not isinstance(result["result"], dict):
        raise ValueError("Tool call failed")
    return result["result"]


def handle(message, config=CONFIG):
    if not isinstance(message, dict) or message.get("jsonrpc") != "2.0":
        return error(None, -32600, "Invalid Request")
    if "id" not in message:
        return None
    ident = message["id"]
    if not isinstance(ident, (int, str)) or isinstance(ident, bool):
        return error(None, -32600, "Invalid Request id")
    method = message.get("method")
    params = message.get("params", {})
    if not isinstance(params, dict):
        return error(ident, -32602, "Invalid params")
    if method == "initialize":
        return success(ident, {"protocolVersion": PROTOCOL, "capabilities": {"tools": {}},
                               "serverInfo": {"name": "arsenal-gateway", "version": "0.1.0"}})
    if method == "ping":
        return success(ident, {})
    try:
        servers = configuration(config)
    except (OSError, ValueError, TypeError, KeyError):
        servers = {}  # Fail closed if no operator configuration is present.
    if method == "tools/list":
        tools = []
        for alias, entry in servers.items():
            try:
                found = discover(entry)
            except (OSError, ValueError, subprocess.TimeoutExpired, json.JSONDecodeError):
                continue
            for name, definition in found.items():
                tools.append({"name": alias + "__" + name,
                              "description": "Explicitly allowlisted read-only downstream tool",
                              "inputSchema": definition["inputSchema"],
                              "annotations": {"readOnlyHint": True, "destructiveHint": False}})
        return success(ident, {"tools": tools})
    if method == "tools/call":
        name, arguments = params.get("name"), params.get("arguments", {})
        if not isinstance(name, str) or not isinstance(arguments, dict) or "__" not in name:
            return error(ident, -32602, "Invalid tool arguments")
        alias, tool = name.split("__", 1)
        entry = servers.get(alias)
        if entry is None or tool not in entry["read_tools"]:
            return success(ident, {"isError": True, "content": [{"type": "text", "text": "Denied by gateway policy"}]})
        # Audit decision before spawning downstream. Never log arguments or secrets.
        print(json.dumps({"decision": "allow-read", "server": alias, "tool": tool}), file=sys.stderr, flush=True)
        try:
            return success(ident, proxy_call(entry, tool, arguments))
        except (PermissionError, OSError, ValueError, subprocess.TimeoutExpired, json.JSONDecodeError, KeyError, TypeError):
            return success(ident, {"isError": True, "content": [{"type": "text", "text": "Gateway rejected or downstream failed"}]})
    return error(ident, -32601, "Method not found")


def main():
    for raw in sys.stdin:
        if not raw.strip():
            continue
        try:
            response = handle(json.loads(raw))
        except (ValueError, TypeError):
            response = error(None, -32700, "Parse error")
        if response is not None:
            print(json.dumps(response, ensure_ascii=False), flush=True)


if __name__ == "__main__":
    main()
