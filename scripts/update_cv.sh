#!/usr/bin/env bash
# Updates assets/pdf/chrisge-cv.pdf from the Overleaf-linked git repo.
# Usage: bash scripts/update_cv.sh
#   Override Overleaf repo path with OVERLEAF_REPO env var.
set -euo pipefail

OVERLEAF_REPO="${OVERLEAF_REPO:-$HOME/Downloads/chrisge-resume}"
SITE_REPO="$(cd "$(dirname "$0")/.." && pwd)"
DEST="$SITE_REPO/assets/pdf/chrisge-cv.pdf"

if [ ! -d "$OVERLEAF_REPO/.git" ]; then
  echo "Error: $OVERLEAF_REPO is not a git repo." >&2
  exit 1
fi

echo "Pulling latest from Overleaf ($OVERLEAF_REPO)..."
git -C "$OVERLEAF_REPO" pull --ff-only

SRC="$OVERLEAF_REPO/main.pdf"
TEX="$OVERLEAF_REPO/main.tex"
if [ ! -f "$SRC" ]; then
  echo "Error: $SRC not found. Make sure Overleaf has compiled the PDF." >&2
  exit 1
fi

# Overleaf auto-commits sometimes ship only main.tex, leaving main.pdf stale.
# Rebuild locally when the source is newer than the compiled PDF.
if [ -f "$TEX" ] && [ "$TEX" -nt "$SRC" ]; then
  PDFLATEX="${PDFLATEX:-/Library/TeX/texbin/pdflatex}"
  if [ ! -x "$PDFLATEX" ] && ! PDFLATEX="$(command -v pdflatex)"; then
    echo "Error: main.tex is newer than main.pdf but pdflatex was not found." >&2
    echo "  Set PDFLATEX=/path/to/pdflatex or install TeX Live." >&2
    exit 1
  fi
  echo "main.tex is newer than main.pdf; recompiling with $PDFLATEX..."
  (cd "$OVERLEAF_REPO" && "$PDFLATEX" -interaction=nonstopmode -halt-on-error main.tex >/dev/null)
  echo "Rebuilt $SRC"
fi

cp "$SRC" "$DEST"
echo "Copied $SRC -> $DEST"

cd "$SITE_REPO"
git add "$DEST"
if git diff --cached --quiet -- "$DEST"; then
  echo "CV is already up to date; nothing to commit."
  exit 0
fi

echo
echo "CV staged. Review and commit:"
echo "  git diff --cached --stat"
echo "  git commit -m 'Update CV'"
echo "  git push"
