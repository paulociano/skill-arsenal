#!/usr/bin/env python3
"""Deterministic, read-only catalogue checks. No third-party dependencies."""
from __future__ import annotations
import argparse
import json
import re
from pathlib import Path


def audit(root: Path) -> dict:
    index = (root / "ARSENAL INDEX.md").read_text(encoding="utf-8")
    paths = sorted((root / "skills").glob("*/SKILL.md"))
    findings = []
    names = {}
    for path in paths:
        rel = path.relative_to(root).as_posix()
        text = path.read_text(encoding="utf-8")
        match = re.match(r"\A---\s*\n(.*?)\n---(?:\s*\n|\Z)", text, re.S)
        if not match:
            findings.append({"path": rel, "code": "invalid_frontmatter"})
            continue
        header = match.group(1)
        name_m = re.search(r"^name:\s*['\"]?([^'\"\n]+)", header, re.M)
        desc_m = re.search(r"^description:\s*(.+)", header, re.M)
        name = name_m.group(1).strip() if name_m else ""
        if name != path.parent.name:
            findings.append({"path": rel, "code": "name_path_mismatch", "name": name})
        if not desc_m or not desc_m.group(1).strip().strip('"\''):
            findings.append({"path": rel, "code": "missing_description"})
        if name in names:
            findings.append({"path": rel, "code": "duplicate_name", "first": names[name]})
        names[name] = rel
        if not re.search(r"^\s*-\s+\*\*" + re.escape(path.parent.name) + r"\*\*\s+[—-]", index, re.M):
            findings.append({"path": rel, "code": "missing_index_entry"})
    return {"skills": len(paths), "findings": findings, "finding_count": len(findings)}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = audit(args.root)
    report = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        args.output.write_text(report, encoding="utf-8")
    else:
        print(report, end="")
    raise SystemExit(1 if result["finding_count"] else 0)


if __name__ == "__main__":
    main()
