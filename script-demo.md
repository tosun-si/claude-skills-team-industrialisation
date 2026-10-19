# Script de démo (runbook scène) — ~14 min

App cible : un micro-service **FastAPI « citation du jour »** — `GET /quote`
(citation aléatoire, liste en mémoire, **pas de DB, pas de secret**) + `GET
/health`. Trivial à comprendre, mais assez riche pour montrer l'archi hexa, le
Dockerfile, la CI, les tests, le commit et la PR. L'app ne compte pas : c'est la
**façon dont elle est générée** qu'on montre.

Prompt exact : voir `prompts.md` (le **même** pour SANS et AVEC). Il ne cite
aucune convention.

| Côté | Dossier | Session |
|---|---|---|
| **SANS** | `~/demo/quote-bare/` (vide) | `claude --safe-mode --disable-slash-commands` — ni CLAUDE.md, ni skills |
| **AVEC** | `~/my-projects/groupbees/skills-demo/` | `claude`, après `pollen update` |

---

## ✅ Prérequis skills

Ce que la session AVEC doit produire, et le skill qui l'apporte :

| Artefact attendu (côté AVEC) | Skill | Vient de |
|---|---|---|
| Archi hexagonale (domain/application/infrastructure, composition root) | `python-hexagonal-clean-archi` | skills-core (équipe) |
| Tests `Test<X>` / `test_given_when_then`, fakes en `conftest` | `python-hexagonal-clean-archi`, `unit-test-given-when-then` | skills-core |
| Dockerfile multi-stage, non-root | `python-docker-multistage` + `docker-image-conventions` | skills-core |
| CI/CD GitHub Actions → Cloud Run | `cloud-run-cicd-gha` | skills-core |
| Commit sans préfixe, PR labellisée | `commit-groupbees`, `pr-groupbees` | skills-core |
| **Citation avec auteur, ≤ 280 caractères, `lang` + filtre `?lang=fr`, 404 / 422** | **`quote-domain`** | **`.skills/` du projet** |

`quote-domain` n'existe **que** dans le projet : c'est la preuve que pollen
charge aussi des skills au niveau projet. Les skills d'équipe, eux, sont aussi
dans ta config globale ; une session normale les voit de toute façon.

## Pré-stage (état pré-chauffé)

- [ ] `pollen --version` (≥ 0.4.0) ; `pollen outdated -g` : tout à jour.
- [ ] `~/demo/quote-bare/` existe et est **vide** (session SANS).
- [ ] `~/my-projects/groupbees/skills-demo/` : `pollen.yaml` épinglé,
      `.skills/quote-domain/`, **`.claude/skills/` vide** (pour le
      `pollen update` en live : `rm -rf .claude/skills .agents/skills`).
- [ ] Une **app de référence** déjà générée côté AVEC (branche `reference`),
      au cas où la génération live traîne.
- [ ] **App déjà déployée** sur Cloud Run → **URL `/quote` ouverte dans un
      onglet** (filet ultime).
- [ ] Pipeline GHA déjà **verte** une fois.
- [ ] **Sorties SANS et AVEC déjà capturées** (Dockerfile, arbo, `quote.py`
      des deux côtés) → fichiers ouverts pour bascule immédiate.

## Arbo attendue côté AVEC (à pointer du doigt)

```
skills-demo/
├── pollen.yaml                    # skills-core épinglé + local .skills/
├── .skills/quote-domain/SKILL.md  # règles métier du projet
├── pyproject.toml
├── Dockerfile                     # multi-stage : uv builder → slim, USER non-root
├── .github/workflows/ci-cd.yml
├── quote_service/
│   ├── domain/models/quote.py     # Quote(text ≤ 280, author obligatoire, lang)
│   ├── application/
│   │   ├── ports/quote_repository.py
│   │   └── use_cases/get_random_quote_use_case.py   # filtre par langue
│   ├── infrastructure/
│   │   ├── adapters/quote/in_memory_quote_repository.py  # ≥ 3 fr + 3 en
│   │   ├── http/routers/{quotes,system}.py               # ?lang=, 404, 422
│   │   └── composition_root.py
│   └── main.py
└── tests/   classes Test<X>, test_given_<ctx>_when_<action>_then_<résultat>
```

---

## Déroulé beat par beat

### Beat 0 — Cadrage (30 s)
- **Dire :** « Même idée, même prompt, deux fois. Une fois sans nos skills, une fois avec. Regardez la différence. »
- **Faire :** les deux terminaux côte à côte (SANS à gauche, AVEC à droite).

### Beat 1 — SANS skills (~2 min 30)
- **Faire :** terminal gauche, dans `~/demo/quote-bare/` → `claude --safe-mode --disable-slash-commands` → **coller** le prompt.
- **Montrer :** la sortie générique — `main.py` quasi monolithique, Dockerfile **mono-stage** en **root**, CI minimale, tests pauvres, une citation **sans auteur ni langue**.
- **Dire :** « C'est correct. Ça marche. Mais ce n'est pas comme NOUS, on code. »
- **Filet :** génération trop lente → ouvrir la sortie SANS pré-capturée.

### Beat 2 — pollen charge les skills (~2 min)
- **Faire :** terminal droit, dans `skills-demo/` :
  ```bash
  pollen list -g             # au niveau machine : mes skills d'équipe, partout
  cat pollen.yaml            # ce que CE projet déclare : skills-core épinglé + .skills/
  ls .claude/skills          # vide
  pollen update              # + 15 skills, dont « + quote-domain  local .skills/quote-domain »
  pollen list                # les skills du projet, chacun avec son commit
  ```
- **Dire :** « Le projet déclare ses skills, épinglés sur un commit — c'est le lock, pas besoin de lockfile. Et il y a ce skill-là, `quote-domain`, qui n'existe que dans ce projet : les règles métier de cette app. »
- **Option (si le temps le permet) :** `pollen outdated` → `pollen autoupdate --freeze` → `git diff pollen.yaml` : le SHA et le tag changent, rien d'autre.

### Beat 3 — AVEC skills (~4 min)
- **Faire :** terminal droit → `claude` → **coller le MÊME prompt**.
- **Montrer (pointer du doigt) :** l'arbo **hexagonale**, le Dockerfile **multi-stage non-root**, la **CI**, les **tests aux conventions**, le **commit** et la **PR** aux conventions — **et** `quote.py` : `author` obligatoire, `text` ≤ 280, `lang`, plus `GET /quote?lang=fr` et ses 404 / 422.
- **Dire :** « Le prompt ne parlait ni d'auteur, ni de langue, ni de 280 caractères. Ça vient du skill du projet. L'archi et le Dockerfile, ça vient des skills de l'équipe. »
- **Filet :** génération trop lente → branche `reference` et commenter.

### Beat 4 — LE DELTA (~2 min 30, climax)
- **Faire :** vue côte à côte de 3-4 paires :
  1. **Dockerfile** mono-stage/root **vs** multi-stage/non-root.
  2. **Arbo** plate **vs** domain/application/infrastructure.
  3. **`Quote`** : `{text}` **vs** `text ≤ 280 + author + lang`, validés dans l'entité.
  4. **Commit/PR** génériques **vs** aux conventions.
- **Dire :** « L'IA n'est pas devenue meilleure entre les deux. Les **règles sont là** : celles de l'équipe, et celles du projet. »

### Beat 5 — Déploiement, la cerise (~2 min)
- **Faire :** la **pipeline GHA déjà verte** (ou la relancer) → **ouvrir** `…/quote?lang=fr` → une citation en français, avec son auteur.
- **Dire :** « De l'idée à l'URL en prod, aux conventions de l'équipe. »
- **Filet :** pipeline KO → l'URL est **déjà ouverte** dans un onglet.

### Transition → gouvernance
- **Dire :** « Mais une bibliothèque de skills, ça se gouverne. Sinon on recrée le monolithe qu'on a fui. »

---

## Reset entre deux runs (répét')

```bash
rm -rf ~/demo/quote-bare && mkdir ~/demo/quote-bare
cd ~/my-projects/groupbees/skills-demo
git reset --hard <commit-de-base> && git clean -fd
rm -rf .claude/skills .agents/skills        # pour rejouer `pollen update`
```

Fermer la PR de test si elle a été recréée.

## Garde-fous (rappel de `demo-prep.md`)
- Prompt **collé**, jamais tapé. **Même** prompt des deux côtés.
- **Hotspot perso**, pas le wifi de conf. Déploiement via **GHA**.
- **Screencast complet** en secours. **URL déjà live** comme filet ultime.
- Répéter **une panne**, pas que le happy path.
