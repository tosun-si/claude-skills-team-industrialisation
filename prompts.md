# Prompt de démo — à COLLER (jamais taper à la main)

## Le prompt (IDENTIQUE pour SANS et AVEC)

```
Crée un petit service Python « citation du jour » en architecture hexagonale :
un endpoint GET /quote qui renvoie une citation aléatoire (liste en mémoire,
pas de base de données) et un GET /health.
Ajoute un test unitaire, le Dockerfile et une CI GitHub Actions qui déploie
sur Cloud Run. Documente-le pour le prochain développeur.
Reste minimal, c'est une démo. Ne commite rien.
```

Ce que le prompt dit, et ce qu'il tait volontairement :

| Le prompt dit | Le prompt tait (les skills décident côté AVEC) |
|---|---|
| hexagonal, petit, pas de base de données | les couches, les noms (`*UseCase`, ports, composition root) |
| un test unitaire | pytest, Given-When-Then, fakes |
| le Dockerfile | pip ou uv, multi-stage, non-root, image de base |
| une CI qui déploie sur Cloud Run | WIF, ci-cd.yml / release.yml, Artifact Registry |
| documente-le | README seul, ou README + AGENTS.md + CLAUDE.md |
| « citation du jour » | auteur obligatoire, ≤ 280 caractères, `lang`, `?lang=fr` |

« Pas de base de données » et « reste minimal » gardent la génération courte
sur scène : le skill hexagonal est complet (SQLAlchemy, Alembic, DI), le prompt
le ramène à l'essentiel sans citer de convention. Les `*UseCase` restent : un
fichier de plus, et la preuve la plus visible du contraste.

## Les deux sessions

| | SANS | AVEC |
|---|---|---|
| Dossier | `~/demo/skills-demo-no-skills/` (vide) | `~/my-projects/groupbees/skills-demo/` |
| Lancement | `claude --safe-mode --disable-slash-commands` | `pollen update`, puis `claude` |
| Contexte | rien : ni CLAUDE.md, ni skills | `pollen.yaml` + `.skills/quote-domain` |

## Le delta (Beat 4), mesuré sur 3 exécutions

Stable d'une exécution à l'autre, des deux côtés.

| | SANS | AVEC (skill qui l'apporte) |
|---|---|---|
| Dépendances | `requirements.txt` + pip | `pyproject.toml` + `uv.lock` (`python-uv-direnv`) |
| Dockerfile | un stage, `pip install`, `CMD sh -c` | multi-stage, uv dans le builder seulement, runtime sans uv (`python-docker-multistage`) |
| Archi | `app/domain`, `application`, `adapters` à sa façon : `GetRandomQuote` | `domain/application/infrastructure`, `GetRandomQuoteUseCase`, ports, DTO, composition root (`python-hexagonal-clean-archi`) |
| Test | `test_returns_…`, un fichier | `TestGetRandomQuoteUseCase`, `test_given_…_when_…_then_…`, fake en `conftest`, unit + integration (`unit-test-given-when-then`) |
| CI | pip + pytest, déploiement `--source .` | uv, ruff, ty, Docker Bake vers Artifact Registry (`cloud-run-cicd-gha`) |
| Doc | `README.md` | `README.md` + `AGENTS.md` + `CLAUDE.md` = `@AGENTS.md` (`agents-md-manager`) |
| Citation | `{text, author}` | `text` ≤ 280, `author` obligatoire, `lang`, `?lang=fr` (`quote-domain`, skill du projet) |

**Ne pas dire sur scène** : « en root », « sans auteur », « clé JSON ». Côté
SANS, l'agent met déjà un `USER` non-root, un auteur et WIF : ce ne sont plus
des différences.

## Mise en place côté AVEC (une fois, avant les répétitions)

`pollen.yaml` de skills-demo, à compléter :

```yaml
repos:
  - repo: git@github.com:groupbees/skills-core.git   # private: SSH
    revision: 0ada6eff527bad1c81078c6c8b9bc0de3e9bcd34  # v0.4.0
    paths:
      - path: skills/python
      - path: skills/docker
      - path: skills/cicd
      - path: skills/gcp
      - path: skills/git
      - path: skills/meta/agents-md-manager    # AGENTS.md + pont CLAUDE.md
  - repo: local
    paths:
      - path: .skills
```

- Retirer `AGENTS.md`, `CLAUDE.md` et `README.md` de la branche de base : c'est
  la session AVEC qui doit créer les deux premiers, et le README actuel décrit
  la démo et contient l'ancien prompt (il souffle la réponse à l'agent).
- `skills/env` (direnv) sort de la liste : il ajouterait un `.envrc` sans
  intérêt pour la démo.

Pas d'`ARCHITECTURE.md` : pour un service de cette taille, README + AGENTS.md
suffisent, et la génération est plus courte.

## Durée mesurée

| Exécution | SANS | AVEC |
|---|---|---|
| 1 | 84 s, 18 fichiers | 3 min 20, 37 fichiers |
| 2 | 80 s, 19 fichiers | 2 min 39, 41 fichiers |

Environ 1 $ par exécution AVEC (40 à 50 tours). Sur scène, enchaîner sans
attendre : lancer SANS, faire `pollen update` à droite pendant qu'il génère,
lancer AVEC, puis commenter la sortie SANS pendant qu'AVEC tourne.

## Après la génération (pas de déploiement en live)

- **Pas de commit, push, tag ni release en live.** Montrer dans le navigateur
  une release déjà faite sur skills-demo : le tag `v0.1.0` (`tag-groupbees`) et
  les release notes classées par labels de PR (`pr-groupbees`).
- Optionnel, 20 s : `git status --short` côté AVEC pour montrer la liste des
  fichiers créés, sans commiter.
