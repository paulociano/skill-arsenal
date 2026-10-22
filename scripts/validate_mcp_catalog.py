#!/usr/bin/env python3
"""Static schema and consistency checks for the Arsenal MCP catalog (stdlib only)."""
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
DIR = ROOT / "mcp"
PROTOCOLS = {"native_connector", "mcp_stdio", "mcp_remote"}
EFFECTS = {"read", "local_write", "remote_write", "shell"}
STATUSES = {"supported", "conditional", "unsupported"}
ID = re.compile(r"^[a-z][a-z0-9]*(?:-[a-z0-9]+)*$")
ERRORS = []


def check(test, message):
    if not test:
        ERRORS.append(message)


def load(path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (ValueError, OSError) as exc:
        ERRORS.append(f"{path}: {exc}")
        return {}


registry = load(DIR / "registry.json")
compat = load(DIR / "compatibility.json")
for name, data in (("registry", registry), ("compatibility", compat)):
    check(data.get("schema_version") == "1.0.0", f"{name}: unknown schema_version")
items = registry.get("tools", [])
check(isinstance(items, list) and bool(items), "registry.tools must be a nonempty list")
seen = set()
for item in items if isinstance(items, list) else []:
    identifier = item.get("id", "")
    check(bool(ID.fullmatch(identifier)), f"invalid tool id: {identifier}")
    check(identifier not in seen, f"duplicate tool: {identifier}")
    seen.add(identifier)
    check(bool(item.get("label")) and bool(item.get("credentials")), f"{identifier}: missing metadata")
    protocols = item.get("protocols", [])
    effects = item.get("effects", [])
    check(bool(protocols) and set(protocols) <= PROTOCOLS, f"{identifier}: invalid protocols")
    check(bool(effects) and set(effects) <= EFFECTS, f"{identifier}: invalid effects")
    check(item.get("verification") == "unverified_per_runtime", f"{identifier}: unsupported verification claim")
clients = compat.get("clients", [])
check(isinstance(clients, list) and bool(clients), "compatibility.clients must be nonempty")
client_ids = set()
for client in clients if isinstance(clients, list) else []:
    identifier = client.get("id", "")
    check(bool(ID.fullmatch(identifier.replace("_", "-"))), f"invalid client id: {identifier}")
    check(identifier not in client_ids, f"duplicate client: {identifier}")
    client_ids.add(identifier)
    check(client.get("status") == "untested", f"{identifier}: unsupported test claim")
    tr = client.get("transports", {})
    check(set(tr) == {"stdio", "remote_http", "native_connector"}, f"{identifier}: transport set mismatch")
    check(set(tr.values()) <= STATUSES, f"{identifier}: invalid transport status")
    check(client.get("tool_writes") in STATUSES, f"{identifier}: invalid write status")
policy = compat.get("policy", {})
check(policy.get("default") == "deny", "policy must fail closed")
check(policy.get("audit") == "decision_before_effect", "policy must audit before effect")
check(policy.get("secret_handling") == "runtime_only_no_prompt_or_logs", "secrets must remain runtime-only")
serialized = json.dumps([registry, compat], ensure_ascii=False)
check(not re.search(r"(?:ghp_|github_pat_|sk-[A-Za-z0-9]{12}|-----BEGIN (?:RSA |EC )?PRIVATE KEY)", serialized), "possible embedded secret")
for required in ("ARSENAL INDEX.md", "AGENTS.md", "skills/agent-action-governance/SKILL.md", "skills/mcp-agent-behavior-testing/SKILL.md", "skills/ai-workflow-automation-engineering/SKILL.md"):
    check((ROOT / required).is_file(), f"missing existing dependency: {required}")
if ERRORS:
    for error in ERRORS:
        print(f"FAIL: {error}", file=sys.stderr)
    sys.exit(1)
print(f"PASS: {len(seen)} tool entries, {len(client_ids)} clients, fail-closed policy, references checked")
