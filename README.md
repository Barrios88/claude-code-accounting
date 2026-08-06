# Claude Code for Accounting Research — Course Website

PhD intensive course site built with [Quarto](https://quarto.org/). Visual identity follows the Yale SOM design system (`course/shared/yale_som_style.md`).

## Repository boundary

**Only this `website/` folder** is published to the public GitHub repository. Course materials, local configs, and the broader monorepo stay private.

## Prerequisites

- [Quarto](https://quarto.org/docs/get-started/) ≥ 1.4
- Python 3.9+ (for `scripts/sync_skills.py`)

## Local preview

```bash
cd website
quarto preview
```

Opens a live-reloading dev server (default `http://localhost:4200`).

## Build

```bash
cd website
quarto render
```

Output lands in `_site/` (gitignored).

## Access code

The live site shows an access-code gate before content. Only a SHA-256 hash of
the code is stored in `styles/access-gate.html` (not the plaintext).

To change the code:

```bash
echo -n 'NEW_CODE' | shasum -a 256
# paste the hex digest into CODE_HASH in styles/access-gate.html
```

Then commit, push, and wait for the Pages deploy.

This is a soft client-side gate for temporary course access. Direct asset URLs
(PDFs, zip labs) are not encrypted.

## Publish to GitHub Pages

Pushes to `main` trigger `.github/workflows/publish.yml`, which renders the site
and deploys the `_site/` output to the `gh-pages` branch.

Live URL: https://johnmbarrios.com/claude-code-accounting/

Repo: https://github.com/Barrios88/claude-code-accounting

To redeploy manually:

```bash
gh workflow run publish.yml --repo Barrios88/claude-code-accounting
```

Or locally (after `quarto render`):

```bash
quarto publish gh-pages --no-prompt
```

## Sync skills catalog

The skills pages are generated from the Barrios Skills source tree:

```bash
python3 scripts/sync_skills.py
```

Options:

```bash
python3 scripts/sync_skills.py --help
python3 scripts/sync_skills.py --source /path/to/skills --site-root .
python3 scripts/sync_skills.py --dry-run
```

Default source: `~/Documents/Barrios_Skills/skills`. The script converts each `SKILL.md` folder to `skills/<name>.qmd`, zips it to `assets/skills/<name>.zip`, and regenerates `skills/index.qmd`.

Install a skill locally:

```bash
# Cursor
cp -r <skill-folder> ~/.cursor/skills/

# Claude Code
cp -r <skill-folder> ~/.claude/skills/
```

## Project layout

```
website/
├── _quarto.yml          # Site config, navbar, sidebar, footer
├── styles/custom.scss   # Yale SOM design tokens
├── index.qmd            # Landing page
├── modules/             # Day 1–6 content (sidebar)
├── labs/                # Hands-on exercises
├── skills/              # Generated skills catalog
├── assets/              # Zips, slides, figures
└── scripts/sync_skills.py
```

## Instructor

John Barrios · Yale School of Management
