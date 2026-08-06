#!/usr/bin/env python3
"""Sync Barrios Skills into the Quarto course website.

Source layout: <source>/<category>/<skill>/SKILL.md (flat <source>/<skill>/SKILL.md
also works). For each skill:
  - Convert to skills/<name>.qmd (YAML title + optional subtitle from description)
  - Zip the skill folder to assets/skills/<name>.zip
  - Regenerate skills/index.qmd as a catalog grouped by category

Categories listed in SKIP_CATEGORIES (e.g. "optional") are excluded.
"""

from __future__ import annotations

import argparse
import re
import sys
import zipfile
from pathlib import Path

DEFAULT_SOURCE = Path("/Users/jmb432/Documents/Barrios_Skills/skills")
DEFAULT_SITE_ROOT = Path(__file__).resolve().parent.parent

# Category folders excluded from the course catalog.
SKIP_CATEGORIES = {"optional"}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Sync SKILL.md folders into the course website skills catalog."
    )
    parser.add_argument(
        "--source",
        type=Path,
        default=DEFAULT_SOURCE,
        help=f"Root directory containing skill subfolders (default: {DEFAULT_SOURCE})",
    )
    parser.add_argument(
        "--site-root",
        type=Path,
        default=DEFAULT_SITE_ROOT,
        help=f"Quarto website root directory (default: {DEFAULT_SITE_ROOT})",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print actions without writing files",
    )
    return parser.parse_args()


def parse_skill_md(content: str) -> tuple[dict[str, str], str]:
    """Strip YAML frontmatter from SKILL.md; return metadata dict and body."""
    content = content.lstrip("\ufeff")
    if not content.startswith("---"):
        return {}, content

    end = content.find("---", 3)
    if end == -1:
        return {}, content

    frontmatter = content[3:end].strip()
    body = content[end + 3 :].lstrip("\n")

    meta: dict[str, str] = {}
    for line in frontmatter.splitlines():
        if ":" in line:
            key, _, value = line.partition(":")
            meta[key.strip()] = value.strip().strip("\"'")
    return meta, body


def folder_to_title(name: str) -> str:
    """Convert folder name to a human-readable title."""
    return name.replace("-", " ").replace("_", " ").title()


def category_to_group(name: str) -> str:
    """Convert a category folder name to a display group name."""
    words = name.replace("-", " ").replace("_", " ").split()
    return " ".join(w if w.lower() == "and" else w.title() for w in words)


def discover_skills(source: Path) -> list[tuple[str, Path]]:
    """Find (group, skill_dir) pairs.

    Supports skills nested one level under category folders as well as
    skill folders sitting directly in the source root.
    """
    found: list[tuple[str, Path]] = []
    for entry in sorted(source.iterdir(), key=lambda p: p.name.lower()):
        if not entry.is_dir():
            continue
        if (entry / "SKILL.md").is_file():
            found.append(("General", entry))
            continue
        if entry.name.lower() in SKIP_CATEGORIES:
            continue
        group = category_to_group(entry.name)
        for sub in sorted(entry.iterdir(), key=lambda p: p.name.lower()):
            if sub.is_dir() and (sub / "SKILL.md").is_file():
                found.append((group, sub))
    return found


def zip_skill_folder(skill_dir: Path, zip_path: Path, dry_run: bool) -> None:
    """Zip entire skill folder, preserving relative paths."""
    if dry_run:
        print(f"  [dry-run] would zip {skill_dir} -> {zip_path}")
        return

    zip_path.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for file_path in sorted(skill_dir.rglob("*")):
            if file_path.is_file():
                arcname = file_path.relative_to(skill_dir.parent)
                zf.write(file_path, arcname)


def yaml_quote(value: str) -> str:
    """Double-quote a string for YAML front matter."""
    return '"' + value.replace("\\", "\\\\").replace('"', '\\"') + '"'


def write_skill_qmd(
    name: str,
    meta: dict[str, str],
    body: str,
    qmd_path: Path,
    dry_run: bool,
    group: str = "General",
) -> None:
    """Write skills/<name>.qmd with listing-ready front matter.

    description + categories feed the listing grid on skills/index.qmd;
    the download button sits at the top of the page body.
    """
    title = meta.get("title") or folder_to_title(name)
    description = meta.get("description", "")

    # De-link relative file references (reference/*.md, scripts/, etc.) that
    # are not copied to the site: keep the link text, drop the broken target.
    # External links (http/https/mailto) and same-page anchors are preserved.
    body = re.sub(
        r"\[([^\]]+)\]\((?!https?://|mailto:|#)[^)]+\)", r"`\1`", body
    )

    lines = ["---", f'title: "{title}"']
    if description:
        lines.append(f"description: {yaml_quote(description)}")
    lines += ["categories:", f"  - {yaml_quote(group)}", "---", ""]
    lines.append(f"[Download {name}.zip](../assets/skills/{name}.zip){{.btn}}")
    lines.append("")
    lines.append(body.rstrip())
    lines.append("")

    if dry_run:
        print(f"  [dry-run] would write {qmd_path}")
        return

    qmd_path.parent.mkdir(parents=True, exist_ok=True)
    qmd_path.write_text("\n".join(lines), encoding="utf-8")


def generate_index(
    skills: list[dict[str, str]],
    index_path: Path,
    dry_run: bool,
    license_text: str = "",
) -> None:
    """Regenerate skills/index.qmd as a listing grid with search + categories."""
    n = len(skills)
    lines = [
        "---",
        'title: "Skills Catalog"',
        "toc: false",
        "listing:",
        "  id: skills-listing",
        '  contents: ["*.qmd"]',
        "  type: grid",
        "  grid-columns: 3",
        "  categories: true",
        '  sort: "title"',
        "  sort-ui: false",
        "  filter-ui: true",
        "  fields: [title, description, categories]",
        "  page-size: 60",
        "---",
        "",
        f"Agent skills for accounting research workflows — {n} skills, "
        "each with a download and a one-line install. Use the search box to "
        "filter, or the category list to browse by area. Click a card for "
        "the full skill documentation and its download.",
        "",
        "::: {.callout-note icon=false}",
        "## Snapshot",
        "This catalog is a snapshot of the [Barrios Skills collection]"
        "(https://barrios88.github.io/barrios-skills/) taken at course build time. "
        "The live collection is the canonical, updated source.",
        ":::",
        "",
        "## Install quick-start",
        "",
        "```bash",
        "# Cursor",
        "cp -r <skill-folder> ~/.cursor/skills/",
        "",
        "# Claude Code",
        "cp -r <skill-folder> ~/.claude/skills/",
        "```",
        "",
        "Or download a `.zip` from any skill page and extract into the same location.",
        "",
        "::: {#skills-listing}",
        ":::",
        "",
    ]

    if license_text:
        lines += [
            "---",
            "",
            "*Skills are from the Barrios Skills collection, MIT licensed "
            "([full license](LICENSE.txt)).*",
            "",
        ]

    content = "\n".join(lines).rstrip() + "\n"

    if dry_run:
        print(f"  [dry-run] would write {index_path}")
        return

    index_path.write_text(content, encoding="utf-8")


def sync_skills(source: Path, site_root: Path, dry_run: bool = False) -> int:
    """Main sync logic. Returns exit code (0 = success, 1 = error)."""
    if not source.exists():
        print(f"Error: source directory not found: {source}", file=sys.stderr)
        print(
            "Create the skills source or pass --source with a valid path.",
            file=sys.stderr,
        )
        return 1

    if not source.is_dir():
        print(f"Error: source is not a directory: {source}", file=sys.stderr)
        return 1

    skills_dir = site_root / "skills"
    assets_dir = site_root / "assets" / "skills"

    skill_entries: list[dict[str, str]] = []
    discovered = discover_skills(source)

    if not discovered:
        print(f"Warning: no skill folders found in {source}", file=sys.stderr)

    for group, skill_dir in discovered:
        name = skill_dir.name
        print(f"Processing: {group} / {name}")

        raw = (skill_dir / "SKILL.md").read_text(encoding="utf-8")
        meta, body = parse_skill_md(raw)
        title = meta.get("title") or folder_to_title(name)
        description = meta.get("description", "")

        write_skill_qmd(
            name, meta, body, skills_dir / f"{name}.qmd", dry_run, group=group
        )
        zip_skill_folder(skill_dir, assets_dir / f"{name}.zip", dry_run)

        skill_entries.append(
            {
                "name": name,
                "title": title,
                "description": description,
                "group": group,
            }
        )

    # Carry over the collection LICENSE (lives at the collection root,
    # one level above the skills/ source directory).
    license_text = ""
    license_src = source.parent / "LICENSE"
    if license_src.exists():
        license_text = license_src.read_text(encoding="utf-8")
        if not dry_run:
            (skills_dir / "LICENSE.txt").write_text(
                license_text, encoding="utf-8"
            )
        print("Carried over collection LICENSE -> skills/LICENSE.txt")
    else:
        print(
            f"Warning: no LICENSE found at {license_src}; "
            "index will omit the license section.",
            file=sys.stderr,
        )

    generate_index(
        skill_entries, skills_dir / "index.qmd", dry_run, license_text
    )
    print(f"Synced {len(skill_entries)} skill(s).")
    return 0


def main() -> int:
    args = parse_args()
    return sync_skills(args.source, args.site_root, dry_run=args.dry_run)


if __name__ == "__main__":
    raise SystemExit(main())
