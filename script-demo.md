# Script de démo (runbook scène) — ~10 min

App cible : un petit service **« citation du jour »** en Python hexagonal —
`GET /quote` (citation aléatoire, liste en mémoire, **pas de DB, pas de
secret**) + `GET /health`, avec un test, un Dockerfile, une CI GitHub Actions
vers Cloud Run et de la doc. L'app ne compte pas : c'est la **façon dont elle
est générée** qu'on montre.

Prompt exact, delta mesuré et durées : voir `prompts.md` (le **même** prompt
pour SANS et AVEC). Il ne cite aucune convention, ni pip ni uv.

| Côté | Dossier | Session |
|---|---|---|
| **SANS** | `~/my-projects/groupbees/skills-demo-no-skills/` (repo `groupbees/skills-demo-no-skills`, `main` vide) | `claude --safe-mode --disable-slash-commands` — ni CLAUDE.md, ni skills |
| **AVEC** | `~/my-projects/groupbees/skills-demo/` (branche `main`) | `pollen update`, puis `claude` |

**Pas de déploiement en live.** La fin de démo montre une vraie release déjà
publiée, dans le navigateur.

---

## ✅ Ce que la session AVEC produit, et le skill qui l'apporte

Mesuré sur trois exécutions (skills-core v0.4.0).

| Artefact (côté AVEC) | Skill | Vient de |
|---|---|---|
| `pyproject.toml` + `uv.lock` (SANS : `requirements.txt` + pip) | `python-uv-direnv` | skills-core |
| Archi `domain/application/infrastructure`, `GetRandomQuoteUseCase`, ports, DTO, composition root | `python-hexagonal-clean-archi` | skills-core |
| Tests `TestGetRandomQuoteUseCase`, `test_given_…_when_…_then_…`, fake en `conftest` | `unit-test-given-when-then` | skills-core |
| Dockerfile multi-stage, uv dans le builder seulement | `python-docker-multistage` + `docker-image-conventions` | skills-core |
| CI : uv, ruff, ty, Docker Bake vers Artifact Registry, `deploy-cloudrun` | `cloud-run-cicd-gha`, `docker-bake-cache` | skills-core |
| `AGENTS.md` + `CLAUDE.md` = `@AGENTS.md` | `agents-md-manager` | skills-core |
| **Citation avec auteur, ≤ 280 caractères, `lang` + filtre `?lang=fr`, 404 / 422** | **`quote-domain`** | **`.skills/` du projet** |

`quote-domain` n'existe **que** dans le projet : c'est la preuve que pollen
charge aussi des skills au niveau projet.

**Ce qui n'est PAS une différence** (SANS le fait déjà) : `USER` non-root, un
auteur sur la citation, WIF dans la CI. Ne pas le dire sur scène.

## Pré-stage (état pré-chauffé)

- [ ] `pollen --version` (≥ 0.6.0) ; `claude --version` figée.
- [ ] `skills-demo-no-skills` cloné à côté de `skills-demo`, sur `main` (vide).
- [ ] `skills-demo` sur `main`, propre : `pollen.yaml` (skills-core v0.4.0) +
      `.skills/quote-domain/`, **pas** d'AGENTS.md, CLAUDE.md ni README,
      **`.claude/skills/` vide** (`rm -rf .claude/skills .agents/skills`).
- [ ] **Sorties SANS et AVEC de référence** ouvertes dans l'éditeur pour
      bascule immédiate : branche `reference` de skills-demo-no-skills et
      branche `reference/avec` de skills-demo (générées le 27/10/2026, sans
      retouche, tests verts) :
      ```bash
      cd ~/my-projects/groupbees/skills-demo-no-skills && git fetch
      git worktree add ~/demo/reference-sans origin/reference
      cd ~/my-projects/groupbees/skills-demo && git fetch
      git worktree add ~/demo/reference-avec origin/reference/avec
      ```
- [ ] Onglet navigateur ouvert sur la **release vitrine** (un repo existant :
      tag, PR labellisées, notes classées).
- [ ] Screencast complet du happy path.

## Arbo attendue côté AVEC (à pointer du doigt)

```
skills-demo/
├── pollen.yaml                    # skills-core v0.4.0 + local .skills/
├── .skills/quote-domain/SKILL.md  # règles métier du projet
├── AGENTS.md                      # contexte projet pour les agents
├── CLAUDE.md                      # @AGENTS.md
├── README.md
├── pyproject.toml / uv.lock
├── Dockerfile                     # multi-stage : uv builder → slim, sans uv
├── docker-bake.hcl
├── .github/workflows/ci-cd.yml
├── quote_service/
│   ├── domain/models/quote.py     # Quote(text ≤ 280, author, lang)
│   ├── application/
│   │   ├── ports/quote_repository.py
│   │   └── use_cases/get_random_quote_use_case.py
│   └── infrastructure/
│       ├── adapters/http/routers/{quotes,health}.py   # ?lang=, 404, 422
│       ├── adapters/persistence/in_memory_quote_repository.py
│       └── composition_root.py
└── tests/unit/…  tests/integration/…   # Test<X>, given/when/then
```

---

## Déroulé beat par beat

On enchaîne sans temps mort : **SANS génère pendant `pollen update`, AVEC
génère pendant qu'on commente SANS.**

### Beat 0 — Cadrage (30 s)
- **Dire :** « Même idée, même prompt, deux fois. Une fois sans nos skills, une fois avec. Regardez la différence. »
- **Faire :** les deux terminaux côte à côte (SANS à gauche, AVEC à droite).

### Beat 1 — Lancer SANS (30 s)
- **Faire :** terminal gauche, `skills-demo-no-skills/` → `claude --safe-mode --disable-slash-commands` → **coller** le prompt. Ne pas attendre (~80 s de génération).

### Beat 2 — pollen charge les skills, lancer AVEC (~1 min 30)
- **Faire :** terminal droit, dans `skills-demo/` :
  ```bash
  cat pollen.yaml            # ce que CE projet déclare : skills-core épinglé + .skills/
  ls .claude/skills          # vide
  pollen update              # + 16 skills, dont « + quote-domain  local .skills/quote-domain »
  claude                     # puis coller le MÊME prompt (~3 min de génération)
  ```
- **Dire :** « Le projet déclare ses skills, épinglés sur un commit. Et il y a ce skill-là, `quote-domain`, qui n'existe que dans ce projet. »

### Beat 3 — La sortie SANS (~2 min)
- **Montrer :** `requirements.txt` + pip, Dockerfile **un stage**, `GetRandomQuote` posé à sa façon, tests `test_returns_…`, un README seul.
- **Dire :** « C'est correct. Ça marche. Mais ce n'est pas comme NOUS, on code. »
- **Filet :** génération trop lente → sortie SANS pré-capturée.

### Beat 4 — La sortie AVEC (~2 min 30)
- **Montrer :** l'arbo en trois couches, `GetRandomQuoteUseCase`, le Dockerfile multi-stage sans uv au runtime, un test Given-When-Then, **`AGENTS.md` + `CLAUDE.md`**, et `quote.py` : `author` obligatoire, `text` ≤ 280, `lang`, `?lang=fr`.
- **Dire :** « Le prompt ne parlait ni de uv, ni de UseCase, ni d'AGENTS.md, ni de 280 caractères. L'équipe et le projet l'ont décidé pour lui. »
- **Filet :** génération trop lente → sortie AVEC pré-capturée.

### Beat 5 — LE DELTA (~1 min 30, climax)
- **Faire :** vue côte à côte, une paire chacun : pip/uv, Dockerfile, archi, tests, doc.
- **Option :** dans la session AVEC, `Compare ../skills-demo-no-skills et ce projet : Dockerfile, archi, tests, CI, doc. Un tableau.` (à chronométrer en répét').
- **Dire :** « L'IA n'est pas devenue meilleure entre les deux. Les **règles sont là**. »

### Beat 6 — Jusqu'à la release (~1 min)
- **Faire :** navigateur, la release vitrine : le tag, les notes rangées par catégorie, une PR et son label.
- **Dire :** « On ne pousse pas en live, mais voilà où ça mène : titres et labels à nos conventions, et les release notes se rangent toutes seules. »

### Transition → gouvernance
- **Dire :** « Mais une bibliothèque de skills, ça se gouverne. Sinon on recrée le monolithe qu'on a fui. »

---

## Reset entre deux runs (répét')

```bash
for repo in skills-demo-no-skills skills-demo; do
  cd ~/my-projects/groupbees/$repo
  git switch main && git reset --hard origin/main && git clean -fdx -e .idea -e "*.iml"
done
```

`git clean -fdx` retire aussi `.claude/skills`, `.agents/skills` et `.venv`
(ignorés par git) : `pollen update` repart de zéro.

## Garde-fous (rappel de `demo-prep.md`)
- Prompt **collé**, jamais tapé. **Même** prompt des deux côtés.
- **Hotspot perso**, pas le wifi de conf.
- **Screencast complet** et **sorties pré-capturées** en secours.
- Répéter **une panne**, pas que le happy path.
