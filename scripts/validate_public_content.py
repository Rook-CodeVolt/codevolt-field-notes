#!/usr/bin/env python3
"""Validate the narrow public-documentation boundary."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
REQUIRED = {
    "README.md",
    "PUBLICATION_POLICY.md",
    "MAINTENANCE.md",
    "CONTRIBUTING.md",
    "SECURITY.md",
    "SUPPORT.md",
    "CHANGELOG.md",
    "LICENSE",
}
FORBIDDEN = {
    "BEGIN PRIVATE KEY": "private-key material",
    "BEGIN OPENSSH PRIVATE KEY": "private-key material",
    "/Users/": "local macOS home path",
    "/home/": "local Unix home path",
    "[SOURCE NEEDED]": "unresolved source marker",
    "[SME REVIEW]": "unresolved review marker",
    "external contractor": "internal staffing disclosure",
    "external agent": "internal staffing disclosure",
    "CONTRACTOR_X_BRIEF": "internal publishing-operations reference",
    "Hannah at CodeVolt": "individual framing instead of the CodeVolt team",
}
LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")


def main() -> int:
    errors: list[str] = []
    for name in sorted(REQUIRED):
        if not (ROOT / name).is_file():
            errors.append(f"missing required file: {name}")

    for path in sorted(ROOT.rglob("*")):
        if not path.is_file() or ".git" in path.parts:
            continue
        if path.suffix not in {".md", ".yml", ".yaml", ".py"} and path.name != "LICENSE":
            continue
        text = path.read_text(encoding="utf-8")
        rel = path.relative_to(ROOT)
        if not text.strip():
            errors.append(f"empty public file: {rel}")
            continue
        if rel != Path("scripts/validate_public_content.py"):
            for token, label in FORBIDDEN.items():
                if token in text:
                    errors.append(f"{rel}: contains {label}")
        if path.suffix == ".md":
            for target in LINK_RE.findall(text):
                target = target.split("#", 1)[0]
                if not target or target.startswith(("http://", "https://", "mailto:")):
                    continue
                resolved = (path.parent / target).resolve()
                try:
                    resolved.relative_to(ROOT)
                except ValueError:
                    errors.append(f"{rel}: relative link escapes repository: {target}")
                    continue
                if not resolved.exists():
                    errors.append(f"{rel}: broken relative link: {target}")

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("Public content validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
