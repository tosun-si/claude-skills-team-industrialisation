---
type: regex
pattern: 'FROM\s+python:3\.\d+-slim'
target: {source: file, path: Dockerfile}
---

Le runtime part de python slim : uv ne part pas en prod.
