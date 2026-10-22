#!/usr/bin/env python3
"""Arsenal MCP catalog server, stdio JSON-RPC 2.0, read-only.

No third-party packages, subprocess execution, network I/O, or secret access.
"""
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
VERSION = "0.2.0"
TOOLS = [
    {"name": "arsenal_list_integrations",
     "description": "List declared candidates (not installed or connected MCP servers).",
     "inputSchema": {"type": "object", "properties": {}, "additionalProperties": False},
     "annotations": {"readOnlyHint": True, "destructiveHint": False}},
    {"name": "arsenal_get_integration",
     "description": "Describe a declared integration. Does not connect or authorize it.",
     "inputSchema": {"type": "object", "properties": {"id": {"type": "string"}},
                     "required": ["id"], "additionalProperties": False},
     "annotations": {"readOnlyHint": True, "destructiveHint": False}},
    {"name": "arsenal_client_compatibility",
     "description": "Read declared client compatibility, not a runtime verification.",
     "inputSchema": {"type": "object", "properties": {}, "additionalProperties": False},
     "annotations": {"readOnlyHint": True, "destructiveHint": False}},
]


def read_catalog(file):
    # Fixed paths only. No user-controlled filenames, URLs, processes or executable hooks.
    return json.loads((ROOT / "mcp" / file).read_text(encoding="utf-8"))


def success(request_id, result):
    return {"jsonrpc": "2.0", "id": request_id, "result": result}


def error(request_id, code, message):
    return {"jsonrpc": "2.0", "id": request_id,
            "error": {"code": code, "message": message}}


def call_tool(name, arguments):
    if not isinstance(arguments, dict):
        raise ValueError("arguments must be an object")
    if name == "arsenal_list_integrations":
        if arguments:
            raise ValueError("unexpected arguments")
        registry = read_catalog("registry.json")
        return {"schema_version": registry["schema_version"],
                "declared_only": True, "integrations": registry["tools"]}
    if name == "arsenal_get_integration":
        if set(arguments) != {"id"} or not isinstance(arguments["id"], str):
            raise ValueError("expected only string id")
        for item in read_catalog("registry.json")["tools"]:
            if item["id"] == arguments["id"]:
                return {"declared_only": True, "integration": item}
        raise LookupError("integration not in registry")
    if name == "arsenal_client_compatibility":
        if arguments:
            raise ValueError("unexpected arguments")
        data = read_catalog("compatibility.json")
        return {"declared_only": True, "compatibility": data}
    raise LookupError("tool not exposed")


def handle(message):
    if not isinstance(message, dict) or message.get("jsonrpc") != "2.0":
        return error(message.get("id") if isinstance(message, dict) else None,
                     -32600, "Invalid Request")
    if "id" not in message:
        return None  # Notification, no reply.
    request_id = message["id"]
    if not isinstance(request_id, (str, int)) or isinstance(request_id, bool):
        return error(None, -32600, "Invalid Request id")
    method = message.get("method")
    params = message.get("params", {})
    if not isinstance(params, dict):
        return error(request_id, -32602, "Invalid params")
    if method == "initialize":
        return success(request_id, {
            "protocolVersion": "2025-03-26",
            "capabilities": {"tools": {"listChanged": False}},
            "serverInfo": {"name": "arsenal-catalog", "version": VERSION}})
    if method == "ping":
        return success(request_id, {})
    if method == "tools/list":
        return success(request_id, {"tools": TOOLS})
    if method == "tools/call":
        name = params.get("name")
        if not isinstance(name, str):
            return error(request_id, -32602, "Missing tool name")
        try:
            value = call_tool(name, params.get("arguments", {}))
        except (ValueError, LookupError) as exc:
            # Tool-level failure, no side effects.
            return success(request_id, {"content": [{"type": "text", "text": str(exc)}],
                                        "isError": True})
        except (OSError, KeyError, json.JSONDecodeError):
            return error(request_id, -32603, "Catalog unavailable")
        return success(request_id, {
            "content": [{"type": "text", "text": json.dumps(value, ensure_ascii=False)}],
            "structuredContent": value, "isError": False})
    return error(request_id, -32601, "Method not found")


def main():
    for raw in sys.stdin:
        if not raw.strip():
            continue
        try:
            message = json.loads(raw)
            response = handle(message)
        except (ValueError, TypeError):
            response = error(None, -32700, "Parse error")
        except Exception:
            response = error(None, -32603, "Internal error")
        if response is not None:
            sys.stdout.write(json.dumps(response, ensure_ascii=False) + "\n")
            sys.stdout.flush()


if __name__ == "__main__":
    main()
