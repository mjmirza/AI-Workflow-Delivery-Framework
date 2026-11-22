#!/usr/bin/env python3
"""Unit tests for the internal document link check."""

from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

import check_doc_links as check


def _write(root: Path, relative: str, text: str) -> None:
    path = root / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


class SlugTests(unittest.TestCase):
    def test_punctuation_and_double_hyphen(self) -> None:
        self.assertEqual(
            check.github_slug("6. Backup & Export Locations"),
            "6-backup--export-locations",
        )

    def test_plain_numbered_heading(self) -> None:
        self.assertEqual(
            check.github_slug("1. Project Completion Summary"),
            "1-project-completion-summary",
        )

    def test_duplicate_headings_gain_a_suffix(self) -> None:
        ids = check.heading_ids(["Notes", "Notes", "Notes"])
        self.assertEqual(ids, {"notes", "notes-1", "notes-2"})


class RepoTests(unittest.TestCase):
    def test_consistent_tree_passes(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            _write(root, "checklists/01-one.md", "# One\n")
            _write(root, "diagrams/01-one.md", "# One\n")
            _write(root, "guides/01-one.md", "# One\n\nSee `02-two.md`.\n")
            _write(root, "guides/02-two.md", "# Two\n")
            _write(
                root,
                "processes/00-index.md",
                "# Index\n\n- `01-one.md`\n",
            )
            _write(root, "processes/01-one.md", "# One\n")
            _write(
                root,
                "templates/00-index.md",
                "# Index\n\n- `01-one.md`\n",
            )
            _write(
                root,
                "templates/01-one.md",
                "# One\n\n## 6. Backup & Export Locations\n\n"
                "[Backup](#6-backup--export-locations)\n",
            )
            _write(
                root,
                "README.md",
                "[Guide](guides/02-two.md)\n\n`guides/01-one.md`\n",
            )
            self.assertEqual(check.check_repo(root), [])

    def test_numbering_gap_and_duplicate(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for folder in check.NUMBERED_DIRS:
                _write(root, f"{folder}/01-a.md", "# A\n")
            _write(root, "guides/01-b.md", "# B\n")
            _write(root, "guides/03-c.md", "# C\n")
            problems = check.check_repo(root)
        self.assertTrue(
            any("guides: duplicate number 01" in item for item in problems)
        )
        self.assertTrue(
            any("guides: numbering gap, 02 is missing" in item for item in problems)
        )

    def test_index_must_name_every_sibling(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for folder in check.NUMBERED_DIRS:
                _write(root, f"{folder}/01-a.md", "# A\n")
            _write(root, "templates/00-index.md", "# Index\n\n`01-a.md`\n")
            _write(root, "templates/02-b.md", "# B\n")
            problems = check.check_repo(root)
        self.assertIn(
            "templates/00-index.md: index does not mention 02-b.md",
            problems,
        )

    def test_broken_markdown_link_and_anchor(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for folder in check.NUMBERED_DIRS:
                _write(root, f"{folder}/01-a.md", "# A\n")
            _write(
                root,
                "README.md",
                "[Missing](no-such.md)\n\n[Bad](#not-a-heading)\n",
            )
            problems = check.check_repo(root)
        self.assertTrue(any("linked file not found: no-such.md" in item for item in problems))
        self.assertTrue(any("heading not found for #not-a-heading" in item for item in problems))

    def test_markdown_links_do_not_fall_back_to_repo_root(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for folder in check.NUMBERED_DIRS:
                _write(root, f"{folder}/01-a.md", "# A\n")
            _write(root, "guides/02-real.md", "# Real\n")
            _write(root, "guides/01-a.md", "[Wrong](guides/02-real.md)\n")
            problems = check.check_repo(root)
        self.assertTrue(
            any("linked file not found: guides/02-real.md" in item for item in problems)
        )

    def test_backtick_root_path_and_ignored_foreign_name(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for folder in check.NUMBERED_DIRS:
                _write(root, f"{folder}/01-a.md", "# A\n")
            _write(
                root,
                "guides/01-a.md",
                "See `guides/01-a.md` and `12-missing.md`.\n"
                "`LICENSE.md` in some other repository is unchanged.\n",
            )
            problems = check.check_repo(root)
        self.assertTrue(any("referenced file not found: 12-missing.md" in item for item in problems))
        self.assertFalse(any("LICENSE.md" in item for item in problems))
        self.assertFalse(any("referenced file not found: guides/01-a.md" in item for item in problems))

    def test_heading_inside_a_fence_is_not_an_anchor(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for folder in check.NUMBERED_DIRS:
                _write(root, f"{folder}/01-a.md", "# A\n")
            _write(
                root,
                "guides/01-a.md",
                "# Real\n\n```\n## 9. Hidden\n```\n\n[Hidden](#9-hidden)\n",
            )
            problems = check.check_repo(root)
        self.assertTrue(any("heading not found for #9-hidden" in item for item in problems))


if __name__ == "__main__":
    unittest.main()
