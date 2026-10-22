#!/usr/bin/env python3
"""Deterministic, no-network MCP stub for gateway tests."""
import json
import os
import sys

for raw in sys.stdin:
    msg = json.loads(raw)
    if "id" not in msg:
        continue
    method = msg.get("method")
    if method == "initialize":
        result = {"protocolVersion": "2025-03-26", "capabilities": {"tools": {}},
                  "serverInfo": {"name": "test-stub", "version": "1"}}
    elif method == "tools/list":
        result = {"tools": [
            {"name": "echo", "inputSchema": {"type": "object", "properties": {"value": {"type": "string"}}},
             "annotations": {"readOnlyHint": True, "destructiveHint": False}},
            {"name": "unsafe", "inputSchema": {"type": "object"},
             "annotations": {"readOnlyHint": False, "destructiveHint": True}}]}
    elif method == "tools/call":
        name = msg["params"]["name"]
        if name == "unsafe":
            result = {"content": [{"type": "text", "text": "UNSAFE"}]}
        else:
            result = {"content": [{"type": "text", "text": msg["params"]["arguments"].get("value", "")}]}
    else:
        result = {}
    print(json.dumps({"jsonrpc": "2.0", "id": msg["id"], "result": result}), flush=True)
