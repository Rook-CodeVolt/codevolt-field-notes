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
    "PUBLIC_COMMUNICATION_STANDARD.md",
    "MAINTENANCE.md",
    "CONTRIBUTING.md",
    "SECURITY.md",
    "SUPPORT.md",
    "CHANGELOG.md",
    "LICENSE",
    "templates/public-work-note.md",
}
SAFETY_FORBIDDEN = {
    "BEGIN PRIVATE KEY": "private-key material",
    "BEGIN OPENSSH PRIVATE KEY": "private-key material",
    "/Users/": "local macOS home path",
    "/home/": "local Unix home path",
    "[SOURCE NEEDED]": "unresolved source marker",
    "[SME REVIEW]": "unresolved review marker",
    "external contractor": "internal staffing disclosure",
    "external agent": "internal staffing disclosure",
    "CONTRACTOR_X_BRIEF": "internal publishing-operations reference",
}
STYLE_FORBIDDEN = {
    "I hope this helps": "chatbot carry-over",
    "Let me know if you'd like": "chatbot carry-over",
    "Let's dive in": "formulaic introduction",
    "Here's what you need to know": "formulaic introduction",
    "As an AI": "chatbot self-reference",
    "—": "em dash associated with generated public copy",
    "–": "en dash used as an em dash substitute",
    "―": "horizontal bar used as an em dash substitute",
    "&mdash;": "escaped em dash",
    "&#8212;": "escaped em dash",
}
LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
FENCE_RE = re.compile(r"^```.*?^```", re.MULTILINE | re.DOTALL)
INLINE_RE = re.compile(r"`[^`\n]+`")
BLOCKQUOTE_RE = re.compile(r"^\s*>.*$", re.MULTILINE)


def own_prose(text: str) -> str:
    """Return CodeVolt prose without quoted evidence, code or identifiers."""
    text = FENCE_RE.sub("\n", text)
    text = INLINE_RE.sub(" ", text)
    return BLOCKQUOTE_RE.sub("", text)


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
            prose = own_prose(text)
            for token, label in SAFETY_FORBIDDEN.items():
                if token in text:
                    errors.append(f"{rel}: contains {label}")
            for token, label in STYLE_FORBIDDEN.items():
                if token in prose:
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

    marker_sets = {
        "PUBLIC_COMMUNICATION_STANDARD.md": [
            "## Check the facts",
            "## Write like a person",
            "## Review before posting",
            "## Correct mistakes openly",
        ],
        "PUBLICATION_POLICY.md": [
            "## Correctness review",
            "PUBLIC_COMMUNICATION_STANDARD.md",
        ],
        "templates/public-work-note.md": [
            "## Source check",
            "## Final public copy",
            "## Review record",
            "Independent editorial and factual review completed",
        ],
    }
    for name, markers in marker_sets.items():
        path = ROOT / name
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        for marker in markers:
            if marker not in text:
                errors.append(f"{name}: missing publication marker: {marker}")

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("Public content validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
