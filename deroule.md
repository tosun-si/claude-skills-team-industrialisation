# Déroulé du talk (timé)

**Titre :** *Industrialiser l'IA en équipe : des skills qui encodent vos conventions*

Conçu pour un **cœur de 35 min + 5–10 min Q&A**. Variantes 30 / 40 min en bas.
Fil rouge unique : **le savoir d'équipe devient des modules activables** ; les
artefacts sont des *preuves*, pas le sujet. Climax = le **contraste sans/avec**.

| # | Section | Durée | Objectif |
|---|---|---|---|
| 1 | Accroche & problème | 4 min | Poser la douleur : l'IA génère du code *générique*, pas VOS conventions — à l'échelle équipe |
| 2 | Le faux-départ : le `CLAUDE.md` monolithe | 3 min | Échec assumé → besoin de modularité + activation à la demande |
| 3 | Les skills, c'est quoi | 6 min | Concept, activation à la demande, anatomie (durable vs volatil), 1–2 skills réels |
| 4 | **DÉMO (le cœur)** | 12 min | 4a contraste (climax), 4b génération end-to-end, 4c déploiement (cerise) |
| 5 | Gouverner les skills (part d'ombre) | 7 min | Versioning, review, scanner IA, capture à chaud, owners |
| 6 | Méthodo transposable & clôture | 3 min | Lundi matin, Cursor/Copilot, punchline |
| — | Q&A | 5–10 min | |

---

## 1. Accroche & problème — 4 min

- **Message :** générer du code avec l'IA = trivial ; le faire *aux conventions
  de l'équipe* = autre histoire. C'est la limite du vibe coding individuel.
- **À montrer :** une douleur relatable — chacun ré-explique à l'IA son
  Dockerfile, son archi, son format de PR ; résultats incohérents d'un dev à
  l'autre. Question d'ouverture : « comment faire coder l'IA *comme l'équipe
  l'attend* ? »

## 2. Le faux-départ : le `CLAUDE.md` monolithe — 3 min

- **Message :** notre 1re tentative. Ça marche… puis ça devient ingérable :
  trop long, contradictions, chargé tout le temps, personne ne le maintient.
- **À montrer :** un (vrai) gros `CLAUDE.md` qui scrolle sans fin. Honnêteté →
  crée la tension qui appelle les skills (modularité + activation à la demande).

## 3. Les skills, c'est quoi — 6 min

- **Message :** un skill = un module de convention *activé à la demande* (pas
  tout chargé en permanence).
- **À montrer :** 1–2 skills réels seulement (anti-catalogue), p.ex.
  `docker-image-conventions` et `pr-groupbees`. Pointer l'**anatomie** :
  *concepts durables* (hexagonal, non-root au runtime) vs *mécanique volatile*
  (flags, versions, commandes) — ça resservira en partie 5.

## 4. DÉMO — le cœur — 12 min

> Tout pré-chauffé (repo init, auth GCP faite, images en cache, app déjà
> déployée). Voir « Prépa démo & filets » plus bas.

- **4a — LE CONTRASTE (≈4 min, climax) :**
  - Session Claude Code **sans skills / sans CLAUDE.md** (config pristine — voir
    note technique) → même prompt → sortie **générique** : Dockerfile mono-stage,
    pas d'archi claire, pas vos conventions.
  - Session **avec** skills → même prompt → **vos conventions exactes** : hexa
    Python, Dockerfile multi-stage non-root, CI conforme, tests aux conventions.
  - Montrer le **delta côte à côte**. C'est *ça* la preuve que ce sont les
    skills — pas « l'IA douée ».
- **4b — Génération end-to-end (≈5 min) :** poursuivre *avec* skills →
  back Python hexa, Dockerfile, CI/CD, tests aux conventions, **commit squashé**
  (`commit-groupbees`) + **PR labellisée** (`pr-groupbees`). Montrer les
  artefacts ; si risqué, s'appuyer sur du pré-généré et *commenter*.
- **4c — Déploiement = cerise (≈3 min) :** app **déjà en ligne** (ouvrir l'URL)
  OU lancer la **pipeline GHA** ; même si elle tombe en erreur, montrer le
  résultat / l'URL déjà live. Court — ce n'est pas le climax.

## 5. Gouverner les skills (part d'ombre) — 7 min

- **Message :** une lib de skills, ça se gouverne — sinon on recrée le monolithe.
- **Points :**
  - Les skills sont **du code** → versionnés + relus en **PR**. Barre *plus
    haute* : un skill s'applique à **tout** ce qui sera généré (blast radius).
  - **L'IA drafte, l'humain possède et merge.**
  - **Scanner IA de péremption** : factuelle (le flag existe-t-il encore ?) → PR,
    pas auto-merge. Faible sur la péremption *de jugement*.
  - **Durable vs volatil** (rappel partie 3) : la revue cible la zone volatile.
  - **Capture à chaud** (war stories) : `run-all` → `run --all` (péremption
    factuelle) ; le `401` Cloud Run dû à `X-Serverless-Authorization` relayé
    (gotcha remonté dans le skill `cloud-run-iap` au point de douleur).
  - **Owners** (`CODEOWNERS`) : sans propriétaire, « l'équipe maintient » =
    personne ne maintient.

## 6. Méthodo transposable & clôture — 3 min

- **Lundi matin :** extraire vos conventions de vos têtes → skills modulaires →
  les gouverner comme du code.
- **Transposable** : le principe (conventions encodées en modules activables +
  gouvernées) vaut pour Cursor, Copilot.
- **Punchline :** « Pas par magie : parce que les règles sont là. »

---

## Variantes de durée

- **30 min :** démo 10 (contraste 4 + génération 4 + deploy 2), gouvernance 6,
  skills 5, accroche 3.
- **40 min :** démo 14 (2e exemple de skill / un échec en live rattrapé),
  gouvernance 9 (process de revue détaillé + diffusion/versioning), +2 sur les
  skills.

## Prépa démo & filets (anti-panne)

- **Tout pré-chauffé** : repo init, `gcloud auth` faite, layers d'images en
  cache, **app déjà déployée** (URL ouverte dans un onglet).
- **Déploiement** : via **GHA** (build/push sur les runners GitHub, pas le wifi
  de conf), avec l'URL déjà live comme filet. Jamais de `gcloud deploy` à froid
  depuis le laptop.
- **Génération** : pré-générer en répét' ; garder les artefacts sous la main pour
  *commenter* si la génération live traîne.
- **Screencast de secours** de toute la démo (au cas où réseau/Claude Code KO).
- **App de démo** : minuscule, stateless, **pas de DB / pas de secrets**,
  **publique (`--allow-unauthenticated`) ou IAP pré-configuré** — ne pas rejouer
  le flow login IAP en live.

### Note technique — la session « sans skills » pour le contraste

**VÉRIFIÉ sur Claude Code v2.1.280** (test réel en `-p`, 23/09/2026). Toggle
**non destructif** — juste des flags, rien à restaurer après :

```bash
# SANS (baseline générique) : ni CLAUDE.md, ni mémoire, ni skills (user, projet, plugins, built-in)
claude --safe-mode --disable-slash-commands

# AVEC : dans le projet de démo, après `skillmgr update`
claude
```

Résultats mesurés (« liste tes skills » + « vois-tu un CLAUDE.md ? ») :

| Flags | Skills visibles | CLAUDE.md |
|---|---|---|
| (aucun) | ~40 (perso + built-in + plugins) | oui |
| `--safe-mode` | 13 built-in (`simplify`, `code-review`…) | non |
| `--disable-slash-commands` | aucun | **oui** |
| `--safe-mode --disable-slash-commands` | **aucun** | **non** ✅ |
| `--bare --disable-slash-commands` | — | ❌ « Not logged in » |

- ❌ **L'ancienne recette `--bare` ne marche plus avec un login Claude
  (OAuth)** : `--bare` n'accepte que `ANTHROPIC_API_KEY` / `apiKeyHelper`.
- `--safe-mode` coupe toutes les personnalisations (CLAUDE.md, skills,
  plugins installés, hooks, MCP, agents…) mais garde l'auth et les built-in ;
  `--disable-slash-commands` retire le reste des skills (built-in compris).
- **Impossible de désactiver les skills dans une session déjà lancée** : leur
  liste est injectée au démarrage. Pour le « sans », toujours une session neuve
  (un 2ᵉ terminal).
- ⚠️ **À répéter** : rejouer le tableau sur la machine de démo (version CLI
  figée la veille).
