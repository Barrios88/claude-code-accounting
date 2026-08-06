#!/bin/bash
# Double-click me to rebuild the whole site from the .qmd sources.
cd "$(dirname "$0")"
echo "Rebuilding site from sources…"
if ! command -v quarto >/dev/null 2>&1; then
  echo ""
  echo "Quarto isn't installed on this Mac yet."
  echo "One-time install: download it from  https://quarto.org/docs/get-started/"
  echo "…or just ask Claude to rebuild the site for you."
  echo ""
  read -n 1 -s -r -p "Press any key to close."
  exit 1
fi
quarto render && echo "" && echo "Done. Refresh your browser (the site is in _site/index.html)." || echo "Render hit an error — see the message above, or ask Claude to fix it."
echo ""
read -n 1 -s -r -p "Press any key to close."
