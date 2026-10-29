# Une eval de skill — `python-docker-multistage`

Un skill est du code : il se teste. Cette eval mesure si le skill
`python-docker-multistage` (skills-core) fait vraiment écrire **notre**
Dockerfile, en jouant la même tâche **avec** et **sans** le skill.

Outil : `claude plugin eval` (Claude Code), le même principe que les evals
obligatoires de Google sur `google/skills`.

## Ce que fait l'eval

1. **Un projet de départ** (`scaffold.sh`) : un service FastAPI minuscule,
   géré par uv (`pyproject.toml`, `uv.lock`, `quote_service/main.py`).
2. **Une tâche** (`prompt.md`) : « Écris le Dockerfile de ce projet, prêt pour
   la prod, et le .dockerignore qui va avec. » Elle ne cite aucune convention.
3. **Deux bras** : avec le skill, puis sans (ablation automatique). Le score
   de chaque bras = la part des graders qui passent ; le **Δ** = ce que le
   skill apporte.

## Les graders — une règle du skill = un check

| Grader | Vérifie | Règle du skill |
|---|---|---|
| `builder-uv` | `FROM ghcr.io/astral-sh/uv:… AS builder` | builder sur l'image uv officielle |
| `runtime-sans-uv` | `FROM python:3.x-slim` | uv ne part pas en prod |
| `deps-en-cache` | `uv sync … --no-install-project` | dépendances avant le code, couche en cache |
| `non-root` | `USER` autre que root | jamais root au runtime |
| `entrypoint-cmd` | `ENTRYPOINT ["uvicorn"]` | ENTRYPOINT / CMD séparés |
| `port-8080` | `8080` | le port de Cloud Run, celui de notre CI |
| `dockerignore` | `.dockerignore` créé | livré avec le Dockerfile |
| `skill-fired` | le skill a été chargé | indicateur côté AVEC, hors score |

Tous sont **déterministes** (regex, présence de fichier) : pas de juge LLM,
pas de variance sur la note, seulement sur la génération.

## Résultat mesuré (29/10/2026, Claude Code 2.1.312, skills-core v0.4.0)

| Bras | Score | Échoue sur |
|---|---|---|
| **Avec** le skill | **1.00** (7/7) | — |
| **Sans** | **0.57** (4/7) | builder uv, ENTRYPOINT/CMD, port 8080 |

**Δ +0.43**, 70 s, 0,29 $ (une exécution par bras).

À lire honnêtement : **sans le skill, Claude fait déjà bien** le multi-stage,
le non-root, le cache des dépendances et le `.dockerignore`. Le skill apporte
**nos choix à nous** : l'image de build, la forme de l'entrée, le port de la
plateforme. Une eval montre aussi ce qu'un skill **n'apporte plus** — une
règle que le modèle suit déjà seul est candidate à la suppression.

## Lancer

```bash
evals-demo/run.sh --runs 1     # ~70 s, ~0,30 $ — pour la scène
evals-demo/run.sh              # 3 exécutions par bras (défaut), pour mesurer
```

`run.sh` :

1. `pollen update` : tire le skill épinglé (`pollen.yaml`) dans
   `plugin/skills/`. skills-core est **privé** → ce dossier est ignoré par
   git, le skill n'est jamais commité ici.
2. Remplace les liens physiques de pollen par des copies : le runner d'eval
   refuse un fichier qui a deux noms.
3. `claude plugin eval ./plugin --scaffold --allow-tools Write` ; rapport HTML
   dans `evals-demo/results/<horodatage>/report.html`.

Prérequis : `pollen` ≥ 0.6.0, accès SSH à `groupbees/skills-core`.

## Arborescence

```
evals-demo/
├── pollen.yaml                    # le skill évalué, épinglé (v0.4.0)
├── run.sh
└── plugin/
    ├── .claude-plugin/plugin.json # fait du dossier un plugin évaluable
    ├── skills/                    # déployé par pollen (gitignoré)
    └── evals/dockerfile-uv/
        ├── prompt.md              # la tâche + max_turns, outils autorisés
        ├── case.yaml              # scaffold_script
        ├── scaffold.sh            # le projet de départ
        └── graders/*.md           # un check par fichier
```

## Sur scène (slide « Comment fait Google ? »)

- **Montrer** `prompt.md`, puis un grader (`entrypoint-cmd.md` : quatre
  lignes), puis le tableau du résultat.
- **Dire :** « Une règle du skill, un check. On joue la tâche avec et sans
  le skill : le Δ, c'est ce que le skill apporte vraiment. Et ce que Claude
  fait déjà tout seul, on peut le retirer du skill. »
- **Ne pas lancer en live** (70 s de silence) : ouvrir le `report.html`
  d'une exécution de répétition.

## Pour aller plus loin

- Une eval par skill, dans le repo du module, jouée en CI à chaque PR
  (`--threshold`) : un skill qui régresse bloque le merge.
- `runs: 3` (défaut) pour lisser la variance avant de conclure.
