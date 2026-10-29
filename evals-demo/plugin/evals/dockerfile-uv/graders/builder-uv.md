---
type: regex
pattern: 'FROM\s+ghcr\.io/astral-sh/uv:\S+\s+AS\s+builder'
flags: i
target: {source: file, path: Dockerfile}
---

Le builder part de l'image uv officielle.
