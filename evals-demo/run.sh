#!/usr/bin/env bash
#
# Lance l'eval du skill python-docker-multistage : avec le skill, puis sans
# (ablation), et compare les scores.
#
# Usage : evals-demo/run.sh [options de `claude plugin eval`, ex. --runs 1]
set -euo pipefail

cd "$(dirname "$0")"

# 1. Le skill évalué, épinglé dans pollen.yaml.
pollen update

# 2. pollen déploie en liens physiques depuis son cache ; le runner d'eval
#    refuse un fichier qui a deux noms. On remplace par de vraies copies.
tmp="$(mktemp -d)"
trap 'rm -rf "$tmp"' EXIT
cp -R plugin/skills "$tmp/" && rm -rf plugin/skills && cp -R "$tmp/skills" plugin/

# 3. L'eval. Résultats hors du plugin : evals-demo/results/<horodatage>/.
claude plugin eval ./plugin \
  --scaffold --allow-tools Write \
  --trust-plugin --no-publish \
  --output-dir "results/$(date +%Y%m%dT%H%M%S)" \
  "$@"
