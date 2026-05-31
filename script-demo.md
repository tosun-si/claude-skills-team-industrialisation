# Script de démo (runbook scène) — ~12 min

App cible : un micro-service **FastAPI « citation du jour »** — `GET /quote`
(citation aléatoire, liste en mémoire, **pas de DB, pas de secret**) + `GET
/health`. Trivial à comprendre, mais assez riche pour montrer l'archi hexa, le
Dockerfile, la CI, les tests, le commit et la PR.

Prompt exact : voir `prompts.md` (le **même** pour SANS et AVEC).

---

## ✅ Prérequis skills (tous présents)

Mapping artefact → skill qui le produit :

| Artefact attendu (côté AVEC) | Skill | État |
|---|---|---|
| Dockerfile multi-stage, non-root | `python-docker-multistage` + `docker-image-conventions` | ✅ existe |
| CI/CD GitHub Actions | `cloud-run-cicd-gha` | ✅ existe |
| Commit squashé, sans préfixe | `commit-groupbees` | ✅ existe |
| PR labellisée (template) | `pr-groupbees` | ✅ existe |
| Archi hexagonale Python (domain/application/infrastructure, composition root, DI) | `python-hexagonal-clean-archi` | ✅ existe |
| Conventions de tests (`Test<X>`, `test_given_when_then`, fakes en `conftest`) | `python-hexagonal-clean-archi` (même skill, couvre les deux) | ✅ existe |

➡️ Tout est en place — la session AVEC produira bien l'archi hexa + les tests
aux conventions depuis un prompt haut niveau, sans rien spécifier. Le skill
`python-hexagonal-clean-archi` a été **extrait de `bff/CLAUDE.md`** : c'est une
mini-histoire à raconter en intro de la partie 3 (« voici comment on a sorti ce
savoir d'un CLAUDE.md projet vers un skill réutilisable ») — illustration
parfaite du propos du talk.

## Pré-stage (état pré-chauffé pour CETTE démo)

- [ ] Dossier vierge `~/demo/quote-bare/` (pour la session SANS).
- [ ] Dossier projet `~/demo/quote-service/` : `git init` + remote, **app déjà
      générée** (côté AVEC), pour servir de référence si la génération live traîne.
- [ ] **App déjà déployée** une fois sur Cloud Run → **URL `/quote` ouverte dans
      un onglet** (filet ultime).
- [ ] Pipeline GHA déjà **verte** une fois sur le commit.
- [ ] **Sorties SANS et AVEC déjà capturées** (Dockerfile + arbo des 2 côtés) →
      fichiers ouverts pour bascule immédiate.
- [ ] Skills à jour (dont le futur `python-hexagonal-architecture`).

## Arbo attendue côté AVEC (à pointer du doigt sur scène)

```
quote-service/
├── pyproject.toml
├── Dockerfile                 # multi-stage : uv builder → python:3.13-slim, USER non-root
├── .dockerignore
├── .github/workflows/ci-cd.yml
├── quote_service/
│   ├── domain/models/quote.py                 # entité Quote (pas d'I/O)
│   ├── application/
│   │   ├── ports/quote_repository.py          # ABC (port)
│   │   └── use_cases/get_random_quote_use_case.py
│   ├── infrastructure/
│   │   ├── adapters/quote/in_memory_quote_repository.py
│   │   ├── http/routers/{quotes,system}.py
│   │   ├── config/settings.py
│   │   └── composition_root.py
│   └── main.py
└── tests/  …  classes Test<X>, méthodes test_given_<ctx>_when_<action>_then_<résultat>
```

---

## Déroulé beat par beat

### Beat 0 — Cadrage (30 s)
- **Dire :** « Même idée, même prompt, deux fois. Une fois sans nos skills, une fois avec. Regardez la différence. »
- **Faire :** afficher les deux terminaux côte à côte (SANS à gauche, AVEC à droite).

### Beat 1 — SANS skills (~2 min 30)
- **Faire :** terminal gauche → `claude --bare --disable-slash-commands` (dossier `quote-bare/`) → **coller** le prompt.
- **Montrer :** la sortie générique — `main.py` quasi monolithique, Dockerfile **mono-stage** qui tourne en **root**, CI minimale, tests pauvres, commit générique, pas de PR aux conventions.
- **Dire :** « C'est correct. Ça marche. Mais ce n'est pas comme NOUS, l'équipe, on code. Pas notre archi, pas notre Dockerfile, pas notre PR. »
- **Filet :** si la génération traîne → ouvrir la sortie SANS pré-capturée.

### Beat 2 — AVEC skills (~4 min)
- **Faire :** terminal droit → `claude` (dossier `quote-service/`) → **coller le MÊME prompt**.
- **Montrer (pointer du doigt) :** l'arbo **hexagonale**, le Dockerfile **multi-stage non-root**, la **CI conforme**, les **tests aux conventions**, le **commit squashé** (style `commit-groupbees`), la **PR labellisée** (template `pr-groupbees`).
- **Dire :** « Même prompt. Mais là, l'IA a appliqué nos règles — sans que je les redonne. Elles sont dans les skills. »
- **Filet :** si la génération traîne → s'appuyer sur l'app déjà générée (référence) et commenter.

### Beat 3 — LE DELTA (~2 min 30, climax)
- **Faire :** vue côte à côte de 2-3 paires d'artefacts :
  1. **Dockerfile** mono-stage/root **vs** multi-stage/non-root.
  2. **Arbo** plate **vs** domain/application/infrastructure.
  3. **Commit/PR** génériques **vs** aux conventions.
- **Dire :** « La différence, ce n'est pas que l'IA est devenue meilleure entre les deux. C'est que les **règles sont là**. Le savoir de l'équipe est devenu activable. »

### Beat 4 — Déploiement, la cerise (~2 min)
- **Faire :** montrer la **pipeline GHA déjà verte** (ou la relancer) → puis **ouvrir l'URL** `…/quote` → une citation s'affiche.
- **Dire :** « De l'idée à l'URL en prod, aux conventions de l'équipe. Et le déploiement, c'est juste la CI que les skills ont générée. »
- **Filet :** pipeline KO en live → l'URL est **déjà ouverte** dans un onglet ; « la voici, déjà en ligne ».

### Transition → Partie 5 (gouvernance)
- **Dire :** « Mais attention : une bibliothèque de skills, ça se gouverne. Sinon on recrée le monolithe qu'on a fui. » → enchaîne sur la partie 5.

---

## Reset entre deux runs (répét')
- `reset-demo.sh` : `rm -rf ~/demo/quote-bare/* ` (recréer vide) ; `git -C ~/demo/quote-service reset --hard <commit-de-base> && git clean -fd` ; fermer la PR de test si recréée. But : pouvoir re-jouer la démo à l'identique, autant de fois que nécessaire.

## Garde-fous (rappel de `demo-prep.md`)
- Prompt **collé**, jamais tapé. **Même** prompt des deux côtés.
- **Hotspot perso**, pas le wifi de conf. Déploiement via **GHA**.
- **Screencast complet** en secours. **URL déjà live** comme filet ultime.
- Répéter **une panne**, pas que le happy path.
