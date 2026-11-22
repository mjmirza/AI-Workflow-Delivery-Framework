#!/usr/bin/env python3
"""Fail when internal document references or numbered series drift.

Markdown links are resolved the way GitHub resolves them, relative to the
file that contains the link. Heading anchors follow the same rule the
hand-written tables of contents in this repo already use: punctuation is
removed and each space becomes a hyphen, so a heading such as
"Backup & Export" keeps the double hyphen.

Backtick paths are looser, because the docs use two conventions. A same
folder name such as `02-security-implementation.md` is resolved next to
the file. A repo path such as `guides/02-security-implementation.md` is
resolved from the repository root when the neighbour lookup misses.

Bare names that are neither numbered (`NN-name.md`) nor a path inside the
repo, for example a licence file in some other project, are left alone.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote

NUMBERED_DIRS = ("checklists", "diagrams", "guides", "processes", "templates")
NUMBERED_NAME = re.compile(r"^(\d{2})-.+\.md$")
FENCE = re.compile(r"^(```+|~~~+)")
HEADING = re.compile(r"^(#{1,6})\s+(.+?)(?:\s+#+\s*)?$")
LINK_TARGET = re.compile(r"\]\(([^)]+)\)")
CODE_SPAN = re.compile(r"`[^`]*`")
BACKTICK = re.compile(r"`([^`\n]+)`")
PATH_TOKEN = re.compile(r"[A-Za-z0-9_./-]+\.md")
PUNCT = re.compile(r"[^\w\s-]", re.UNICODE)
EXPLICIT_ID = re.compile(
    r"""(?:\sid|\sname)\s*=\s*["']([^"']+)["']|\{#([A-Za-z0-9_-]+)\}"""
)
SKIP_PARTS = {".git", "node_modules", ".mermaid_cache"}


def github_slug(heading: str) -> str:
    """Turn a heading into the anchor these documents already link to."""
    text = heading.strip().lower()
    text = re.sub(r"!\[([^\]]*)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"<[^>]+>", "", text)
    text = PUNCT.sub("", text)
    return text.replace(" ", "-")


def heading_ids(headings: list[str]) -> set[str]:
    """Assign anchors, suffixing later duplicates the way GitHub does."""
    used: set[str] = set()
    counts: dict[str, int] = {}
    for heading in headings:
        base = github_slug(heading)
        if not base:
            continue
        slug = base
        if slug in used:
            number = counts.get(base, 0)
            while True:
                number += 1
                slug = f"{base}-{number}"
                if slug not in used:
                    break
            counts[base] = number
        used.add(slug)
    return used


def _fence_marker(line: str) -> str | None:
    indent = len(line) - len(line.lstrip(" "))
    if indent > 3:
        return None
    match = FENCE.match(line.lstrip(" "))
    if not match:
        return None
    return match.group(1)


def prose_lines(text: str) -> list[tuple[int, str]]:
    """Lines that are not inside a fenced code block, with 1-based numbers."""
    lines: list[tuple[int, str]] = []
    in_fence = False
    fence_char = ""
    fence_len = 0
    for lineno, line in enumerate(text.splitlines(), 1):
        marker = _fence_marker(line)
        if marker is not None:
            char = marker[0]
            if not in_fence:
                in_fence = True
                fence_char = char
                fence_len = len(marker)
                continue
            if char == fence_char and len(marker) >= fence_len:
                in_fence = False
                continue
        if not in_fence:
            lines.append((lineno, line))
    return lines


def _inside(repo: Path, path: Path) -> bool:
    try:
        path.resolve().relative_to(repo.resolve())
    except ValueError:
        return False
    return True


def _lookup(repo: Path, source: Path, ref: str, *, from_root: bool) -> Path | None:
    candidates = [(source.parent / ref).resolve()]
    if from_root:
        candidates.append((repo / ref).resolve())
    for candidate in candidates:
        if candidate.is_file() and _inside(repo, candidate):
            return candidate
    return None


def _display(repo: Path, path: Path) -> str:
    return path.resolve().relative_to(repo.resolve()).as_posix()


def _split_target(raw: str) -> str:
    target = raw.strip()
    if target.startswith("<") and ">" in target:
        target = target[1 : target.index(">")]
    target = re.sub(r'\s+(?:"[^"]*"|\'[^\']*\')\s*$', "", target)
    return target.strip()


def _external(target: str) -> bool:
    if target.startswith(("http://", "https://", "mailto:", "//")):
        return True
    return bool(re.match(r"^[A-Za-z][A-Za-z0-9+.-]*:", target))


def _ids_for(text: str) -> set[str]:
    headings: list[str] = []
    explicit: set[str] = set()
    for _, line in prose_lines(text):
        match = HEADING.match(line)
        if match:
            headings.append(match.group(2).strip())
        for found in EXPLICIT_ID.finditer(line):
            explicit.add(found.group(1) or found.group(2))
    return heading_ids(headings) | explicit


def _fragment_missing(text: str, fragment: str) -> bool:
    fragment = unquote(fragment)
    if not fragment:
        return False
    return fragment not in _ids_for(text)


def _internal_backtick(token: str) -> bool:
    if not PATH_TOKEN.fullmatch(token):
        return False
    name = token.rsplit("/", 1)[-1]
    if "/" in token:
        return True
    return NUMBERED_NAME.fullmatch(name) is not None


def check_repo(repo: Path) -> list[str]:
    """Return human-readable problems. An empty list means the tree is consistent."""
    repo = repo.resolve()
    problems: list[str] = []
    problems.extend(_check_numbering(repo))
    problems.extend(_check_references(repo))
    return problems


def _markdown_files(repo: Path) -> list[Path]:
    found: list[Path] = []
    for path in repo.rglob("*.md"):
        if any(part in SKIP_PARTS for part in path.parts):
            continue
        if path.is_file():
            found.append(path)
    return found


def _check_numbering(repo: Path) -> list[str]:
    problems: list[str] = []
    for folder_name in NUMBERED_DIRS:
        folder = repo / folder_name
        if not folder.is_dir():
            problems.append(f"{folder_name}: directory is missing")
            continue
        grouped: dict[int, list[str]] = {}
        for path in sorted(folder.glob("*.md")):
            match = NUMBERED_NAME.match(path.name)
            if not match:
                continue
            grouped.setdefault(int(match.group(1)), []).append(path.name)
        if not grouped:
            problems.append(f"{folder_name}: no numbered markdown files")
            continue
        for number, names in grouped.items():
            if len(names) > 1:
                listed = ", ".join(names)
                problems.append(
                    f"{folder_name}: duplicate number {number:02d} ({listed})"
                )
        numbers = sorted(grouped)
        expected = set(range(numbers[0], numbers[-1] + 1))
        for missing in sorted(expected - set(numbers)):
            problems.append(
                f"{folder_name}: numbering gap, {missing:02d} is missing"
            )
        for path in sorted(folder.glob("00-*.md")):
            text = path.read_text(encoding="utf-8")
            for names in grouped.values():
                for name in names:
                    if name == path.name:
                        continue
                    if name not in text:
                        problems.append(
                            f"{_display(repo, path)}: index does not mention {name}"
                        )
    return problems


def _check_references(repo: Path) -> list[str]:
    problems: list[str] = []
    for path in _markdown_files(repo):
        text = path.read_text(encoding="utf-8")
        where = _display(repo, path)
        problems.extend(_check_links(repo, path, where, text))
        problems.extend(_check_backticks(repo, path, where, text))
    return problems


def _check_links(repo: Path, path: Path, where: str, text: str) -> list[str]:
    problems: list[str] = []
    for lineno, line in prose_lines(text):
        masked = CODE_SPAN.sub(lambda match: " " * len(match.group(0)), line)
        for match in LINK_TARGET.finditer(masked):
            target = _split_target(match.group(1))
            if not target or _external(target):
                continue
            path_part, sep, fragment = target.partition("#")
            path_part = unquote(path_part)
            if not path_part:
                if _fragment_missing(text, fragment):
                    problems.append(
                        f"{where}:{lineno}: heading not found for #{fragment}"
                    )
                continue
            resolved = _lookup(repo, path, path_part, from_root=False)
            if resolved is None:
                problems.append(
                    f"{where}:{lineno}: linked file not found: {path_part}"
                )
                continue
            if sep and resolved.suffix.lower() == ".md":
                target_text = resolved.read_text(encoding="utf-8")
                if _fragment_missing(target_text, fragment):
                    problems.append(
                        f"{where}:{lineno}: heading not found for "
                        f"{path_part}#{fragment}"
                    )
    return problems


def _check_backticks(repo: Path, path: Path, where: str, text: str) -> list[str]:
    problems: list[str] = []
    for lineno, line in enumerate(text.splitlines(), 1):
        for match in BACKTICK.finditer(line):
            token = match.group(1).strip()
            if not _internal_backtick(token):
                continue
            if _lookup(repo, path, token, from_root=True) is None:
                problems.append(
                    f"{where}:{lineno}: referenced file not found: {token}"
                )
    return problems


def main(argv: list[str] | None = None) -> int:
    args = list(sys.argv[1:] if argv is None else argv)
    repo = Path(args[0]).resolve() if args else Path(__file__).resolve().parents[2]
    problems = check_repo(repo)
    if problems:
        for problem in problems:
            print(problem)
        print(f"\n{len(problems)} problem(s).")
        return 1
    print("Document links, anchors and numbering look consistent.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
