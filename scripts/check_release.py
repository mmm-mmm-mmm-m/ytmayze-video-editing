#!/usr/bin/env python3
"""Check the public package without loading source projects or third-party code.

Metadata uses a deliberately small YAML subset: single-line JSON strings, plus
the interface mapping in openai.yaml. This validator is not a general YAML parser.
"""
import ast
import json
from pathlib import Path
import re
import struct
from urllib.parse import unquote
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
SKILLS = {
    "ytmayze-video-editing", "ytmayze-frame-daw", "ytmayze-pace-music",
    "ytmayze-reactive-vfx", "ytmayze-design-sound", "ytmayze-engagement",
    "ytmayze-hyperframes-inserts", "ytmayze-effect-presets",
}
ROOT_FILES = {"README.md", "CONTRIBUTING.md", "CHANGELOG.md", "VERSION", ".gitignore", "LICENSE", "LICENSE.txt"}
SUFFIXES = {".md", ".py", ".yaml", ".yml", ".svg", ".png"}
PNG_FILES = {"docs/images/laptop-showcase.png", "docs/images/daw-framing.png"}
PRIVATE_PATTERNS = {
    "personal filesystem path": re.compile(r"/(?:Users|Volumes|home)/[^\s\"<>]+"),
    "private chat identifier": re.compile(r"\b01[0-9a-f]{6}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}\b", re.I),
    "GitHub credential": re.compile(r"\b(?:gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,})"),
    "secret key": re.compile(r"\bsk[-_](?:live|test|proj)[-_][A-Za-z0-9_-]{12,}"),
    "private key": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    "JWT": re.compile(r"\beyJ[A-Za-z0-9_-]{15,}\.[A-Za-z0-9_-]{15,}\.[A-Za-z0-9_-]{10,}"),
}


def fields(text, indent=""):
    result = {}
    for line in text.splitlines():
        match = re.fullmatch(re.escape(indent) + r"([a-z_]+): (.+)", line)
        if not match:
            raise ValueError("metadata must use single-line JSON-compatible string values")
        key, raw = match.groups()
        if key in result:
            raise ValueError("duplicate metadata field")
        value = json.loads(raw)
        if not isinstance(value, str) or not value.strip():
            raise ValueError("metadata strings must be nonempty")
        result[key] = value
    return result


def check_png(raw):
    if raw[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError("invalid PNG signature")
    offset, last = 8, None
    while offset < len(raw):
        size = struct.unpack(">I", raw[offset:offset + 4])[0]
        kind = raw[offset + 4:offset + 8]
        if kind in {b"tEXt", b"zTXt", b"iTXt", b"eXIf"}:
            raise ValueError("PNG has metadata requiring manual review/removal")
        offset += size + 12
        if offset > len(raw):
            raise ValueError("truncated PNG chunk")
        last = kind
    if offset != len(raw) or last != b"IEND":
        raise ValueError("invalid PNG termination")


def main():
    errors = []
    actual = {p.name for p in (ROOT / "skills").iterdir() if p.is_dir()}
    if actual != SKILLS:
        errors.append("skill directory set differs from the eight public skills")
    for path in sorted(ROOT.rglob("*")):
        rel = path.relative_to(ROOT)
        if ".git" in rel.parts or "__pycache__" in rel.parts:
            continue
        if path.is_symlink():
            errors.append(f"{rel}: symlinks are excluded")
            continue
        if not path.is_file():
            continue
        try:
            if len(rel.parts) == 1:
                if path.name not in ROOT_FILES:
                    raise ValueError("unexpected root file")
            elif rel.parts[0] not in {"skills", "docs", "scripts", ".github"}:
                raise ValueError("unexpected top-level directory")
            elif path.suffix not in SUFFIXES:
                raise ValueError("file type is excluded from the public package")
            if path.name.startswith("._") or path.name == ".DS_Store":
                raise ValueError("machine metadata file")
            raw = path.read_bytes()
            if len(raw) > 2_000_000:
                raise ValueError("file exceeds public package size limit")
            if path.suffix == ".png":
                if rel.as_posix() not in PNG_FILES:
                    raise ValueError("new image needs an explicit allowlist/provenance review")
                check_png(raw)
                continue
            text = raw.decode("utf-8")
            for label, pattern in PRIVATE_PATTERNS.items():
                if pattern.search(text):
                    raise ValueError(label + " found; inspect locally without printing the value")
            if path.suffix != ".py" and ("REPO-OWNER" in text or "YOUR-ACCOUNT" in text):
                raise ValueError("unresolved repository placeholder")
            if any(handle != "@ytmayze" for handle in re.findall(r"@[yY][tT][mM][aA][yY][zZ][eE]", text)):
                raise ValueError("handle must be lowercase")
            if path.suffix == ".md":
                for target in re.findall(r"!?\[[^\]]*\]\(([^)]+)\)", text):
                    if re.match(r"^[a-z]+:", target) or target.startswith("#"):
                        continue
                    resolved = (path.parent / unquote(target.split("#")[0])).resolve()
                    if not resolved.is_relative_to(ROOT) or not resolved.exists():
                        raise ValueError("broken or external local Markdown link")
            if path.suffix == ".svg":
                ET.fromstring(text)
                if re.search(r"<\s*(?:script|foreignObject)\b|(?:href|src)\s*=\s*[\"']https?:", text, re.I):
                    raise ValueError("SVG must be static and self-contained")
            if path.suffix == ".py":
                ast.parse(text)
            if path.name == "SKILL.md":
                match = re.match(r"^---\n(.*?)\n---\n", text, re.S)
                if not match:
                    raise ValueError("missing skill frontmatter")
                header = fields(match.group(1))
                if set(header) != {"name", "description"} or header["name"] != path.parent.name:
                    raise ValueError("skill frontmatter/folder mismatch")
                if len(header["description"]) > 1024:
                    raise ValueError("description too long")
                for sibling in re.findall(r"\$((?:ytmayze-)[a-z-]+)", text):
                    if sibling not in SKILLS:
                        raise ValueError("unknown companion skill")
            if path.name == "openai.yaml":
                if not text.startswith("interface:\n"):
                    raise ValueError("expected interface metadata")
                ui = fields(text[len("interface:\n"):].rstrip("\n"), "  ")
                if set(ui) != {"display_name", "short_description", "default_prompt"}:
                    raise ValueError("unexpected UI fields; review schema before extending")
                if not 25 <= len(ui["short_description"]) <= 64:
                    raise ValueError("short description length")
                if "$" + path.parent.parent.name not in ui["default_prompt"]:
                    raise ValueError("default prompt does not invoke its skill")
        except (OSError, ValueError, SyntaxError, struct.error, ET.ParseError) as error:
            errors.append(f"{rel}: {error}")
    if errors:
        print("Release checks failed:\n" + "\n".join(errors))
        return 1
    print("Public package checks passed: eight skills, metadata, links, file allowlist, privacy patterns and PNG metadata.")
    print("Human review of images, private context and creative claims is still required.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
