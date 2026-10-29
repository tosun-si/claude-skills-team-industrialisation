---
type: regex
pattern: 'uv sync[^\n]*--no-install-project'
target: {source: file, path: Dockerfile}
---

Les dépendances s'installent avant le code : leur couche reste en cache.
