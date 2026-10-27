#!/usr/bin/env bash
#
# Build the Cloud Nord deck from the DevFest content: same slides, Cloud Nord
# footer and title line, and the OpenFeedback QR code on the end slide.
#
# Usage: talks/build_cloud_nord.sh [output-dir]
#   output-dir defaults to ~/my-projects/conferences/cloud_nord/2026
set -euo pipefail

here="$(cd "$(dirname "$0")" && pwd)"
out="${1:-$HOME/my-projects/conferences/cloud_nord/2026}"
deck="talk_skills_cloud_nord_10_2026"
work="$(mktemp -d)"
trap 'rm -rf "$work"' EXIT

mkdir -p "$work/talks"
cp -R "$here/assets" "$here/generate_slides.py" "$here/slides_content.py" "$work/talks/"

content="$work/talks/slides_content.py"
sed -i.bak \
  -e "s/^DECK_NAME = .*/DECK_NAME = \"$deck\"/" \
  -e "s/^FOOTER_TEXT = .*/FOOTER_TEXT = \"Industrialiser l'IA en équipe · Cloud Nord\"/" \
  -e 's/· DevFest Toulouse 2026",/· Cloud Nord 2026",/' \
  -e 's/^END_QRS = \[\]/END_QRS = [("qr_openfeedback_cloud_nord.png", "Votre avis compte · OpenFeedback")]/' \
  "$content"

if grep -q "DevFest Toulouse 2026\|^END_QRS = \[\]" "$content"; then
  echo "error: the Cloud Nord substitutions did not all apply" >&2
  exit 1
fi

(cd "$work" && uv run -q --with python-pptx python talks/generate_slides.py)
mkdir -p "$out"
cp "$work/talks/slides/$deck.pptx" "$out/"
echo "OK → $out/$deck.pptx"
