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

## Le delta attendu (Beat 4)

| | SANS (attendu) | AVEC (skill qui l'apporte) |
|---|---|---|
| Dépendances | `requirements.txt` + pip | `pyproject.toml` + `uv.lock` (`python-uv-direnv`) |
| Dockerfile | un stage, `pip install` (déjà non-root au 1er test : `USER nobody`) | multi-stage, uv dans le builder seulement, runtime sans uv, `ENTRYPOINT`/`CMD` séparés (`python-docker-multistage`) |
| Archi | hexa « à sa façon » : `GetRandomQuote`, tout dans `domain.py` | `domain/application/infrastructure`, `*UseCase`, composition root (`python-hexagonal-clean-archi`) |
| Test | pytest au fil de l'eau | `Test<X>`, `test_given_…_when_…_then_…`, fake en `conftest` (`unit-test-given-when-then`) |
| CI | pip + pytest, déploiement `--source .` (déjà en WIF au 1er test) | uv, ruff, ty, Docker Bake vers Artifact Registry, `deploy-cloudrun` (`cloud-run-cicd-gha`) |
| Doc | `README.md` | `README.md` + `AGENTS.md` + `CLAUDE.md` d'une ligne (`agents-md-manager`) |
| Citation | `{text, author}` | `text` ≤ 280, `author` obligatoire, `lang`, `?lang=fr` (`quote-domain`, skill du projet) |

## Mise en place côté AVEC (une fois, avant les répétitions)

`pollen.yaml` de skills-demo, à compléter :

```yaml
repos:
  - repo: git@github.com:groupbees/skills-core.git   # private: SSH
    revision: <sha>  # v0.3.2 (à publier : hexagonal-flat + déclencheurs agents-md-manager)
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

Premier test (prompt avec « peu de fichiers ») : SANS 75 s, AVEC 3 min 07.
Sur scène, lancer AVEC dès le début du Beat 1, en parallèle de SANS.

## Après la génération (pas de déploiement en live)

- **Pas de commit, push, tag ni release en live.** Montrer dans le navigateur
  une release déjà faite sur skills-demo : le tag `v0.1.0` (`tag-groupbees`) et
  les release notes classées par labels de PR (`pr-groupbees`).
- Optionnel, 20 s : `git status --short` côté AVEC pour montrer la liste des
  fichiers créés, sans commiter.
