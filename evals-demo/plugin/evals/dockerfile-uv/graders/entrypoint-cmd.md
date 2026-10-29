---
type: regex
pattern: 'ENTRYPOINT\s*\[\s*"uvicorn"\s*\]'
target: {source: file, path: Dockerfile}
---

ENTRYPOINT et CMD séparés : on surcharge les arguments au `docker run`.
