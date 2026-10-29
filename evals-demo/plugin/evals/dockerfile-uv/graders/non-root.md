---
type: regex
pattern: '^USER\s+(?!root\b)\w+'
flags: m
target: {source: file, path: Dockerfile}
---

Le conteneur ne tourne pas en root.
