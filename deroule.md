# Déroulé du talk (timé)

**Titre :** *Industrialiser l'IA en équipe : des skills qui encodent vos conventions*
**Speakers :** Mazlum Tosun & Guillaume Leroy · 33 slides

Créneaux : **DevFest Toulouse ≈ 45 min**, **Cloud Nord ≈ 50 min** (à
confirmer). Cœur de **≈ 38 min**, le reste en Q&A. Fil rouge unique : **le
savoir d'équipe devient des modules activables** ; les artefacts sont des
*preuves*, pas le sujet. Climax = le **contraste sans/avec** de la démo.

Qui dit quoi, réplique par réplique : `dialogue.md`. Démo pas à pas :
`script-demo.md`. Prompt et delta mesuré : `prompts.md`.

| # | Bloc | Slides | Durée | Qui | Objectif |
|---|---|---|---|---|---|
| 1 | Ouverture | 1–3 | 2 min | Les deux | Titre, qui on est, le clin d'œil TechCast |
| 2 | Le problème | 4–6 | 3 min | Mazlum → Guillaume → Mazlum | GroupBees, l'équipe de 8, les nouvelles stacks qui divergent |
| 3 | Du CLAUDE.md aux skills | 7–13 | 6 min | Alternance | CLAUDE.md partagé qui grossit → skills chargés à la demande, anatomie, domaines composables |
| 4 | Partager les skills | 14–18 | 4 min | Guillaume, puis Mazlum | Sync global, sa limite, par projet, standards ouverts |
| 5 | pollen | 19–24 | 6 min | Guillaume, Mazlum sur le lockfile, npx skills et sa config | `pollen.yaml`, pas de lockfile, npx skills, trois propriétaires, Spec Kit / BMAD |
| 6 | **DÉMO (le cœur)** | 25 | 10 min | Alternance par beat | Même prompt sans / avec skills, delta, release |
| 7 | Gouvernance | 26–30 | 6 min | Mazlum, Guillaume sur la fiabilité | Référents, skills périmés, CI, la doc d'un outil, Google |
| 8 | Clôture | 31–33 | 2 min | Les deux | À retenir, de quoi l'essayer, punchline |
| — | Q&A | | 6–12 min | Voir le tableau de `dialogue.md` | |

---

## 1. Ouverture — 2 min (slides 1–3)

- **Message :** générer du code avec l'IA = trivial ; le faire *aux conventions
  de l'équipe* = autre histoire.
- Chacun présente l'autre (slide 2), puis 10 secondes sur l'image TechCast
  façon Guignols (slide 3) : on lit le bandeau, on enchaîne.

## 2. Le problème — 3 min (slides 4–6)

- Plateforme de registre d'API, stack exigeante (hexagonal, Terragrunt,
  Workload Identity, IAP), une équipe de 8 aux niveaux variés.
- Grâce à Claude, tout le monde fait évoluer les stacks ; mais les **nouveaux**
  services et stacks IaC **divergent** : chacun son Claude, son CLAUDE.md.

## 3. Du CLAUDE.md aux skills — 6 min (slides 7–13)

- Le CLAUDE.md partagé : simple… puis il grossit, chargé tout le temps, coûteux
  en tokens. Montrer le vrai fichier qui scrolle.
- **Skill = CLAUDE.md modulaire, chargé à la demande.** La description est
  toujours vue, le corps seulement si la tâche correspond.
- Un skill est un dossier : `references/`, `assets/`, `scripts/`.
- Le CLAUDE.md redevient le contexte durable du projet (AGENTS.md + pont).
- Domaines composables : Docker générique + Python par-dessus.

## 4. Partager les skills — 4 min (slides 14–18)

- V1 : un catalogue synchronisé en global, versionné par tags git.
- Limite : nos règles s'appliquent partout, clients compris → choisir projet
  par projet, comme des dépendances.
- Rien de propriétaire : Agent Skills (tous les agents) + AGENTS.md.

## 5. pollen — 6 min (slides 19–24)

- `pollen.yaml` façon pre-commit, `pollen update`, périmètre étroit.
- **Pas de lockfile** (Mazlum) : le SHA épinglé est le lock ; `outdated` →
  `autoupdate` → PR.
- **Et npx skills ?** Guillaume l'avait regardé avant pollen : la différence
  est dans le modèle (déclaratif, sans package.json, épinglé sur une release).
- Ma config machine : trois propriétaires dans un fichier.
- Spec Kit / BMAD : même format, autre contenu (processus vs conventions).

## 6. DÉMO — le cœur — 10 min (slide 25)

> Pas de déploiement en live. Tout est pré-chauffé, les deux sorties sont
> pré-capturées. Détail dans `script-demo.md`.

On enchaîne sans temps mort : **SANS génère (~80 s) pendant `pollen update`,
AVEC génère (~3 min) pendant qu'on commente SANS.**

| Beat | Durée | Pilote → commente | Contenu |
|---|---|---|---|
| 0 Cadrage | 30 s | Mazlum | Même prompt, deux fois |
| 1 Lancer SANS | 30 s | Mazlum → Guillaume | Session vierge, prompt collé |
| 2 pollen, lancer AVEC | 1 min 30 | Guillaume → Mazlum | `pollen.yaml`, dossier vide, `pollen update`, `quote-domain` |
| 3 Sortie SANS | 2 min | Mazlum → Guillaume | pip, un stage, `GetRandomQuote`, README seul |
| 4 Sortie AVEC | 2 min 30 | Guillaume → Mazlum | uv, trois couches, `GetRandomQuoteUseCase`, Given-When-Then, AGENTS.md, `?lang=fr` |
| 5 Delta (climax) | 1 min 30 | Ping-pong | « L'IA n'est pas devenue meilleure. Les règles sont là. » |
| 6 Release | 1 min | Mazlum → Guillaume | Une vraie release d'un repo existant : tag, PR labellisées, notes classées |

## 7. Gouvernance — 6 min (slides 26–30)

- **Une lib de skills, ça se gouverne** : du code, versionné, relu en PR ;
  blast radius énorme. Relecture par les **référents** (transverses : Mazlum et
  Guillaume ; spécialisés : ceux qui connaissent le domaine), pas de
  CODEOWNERS.
- **Quand un skill périme** : une règle périmée n'échoue pas, elle apprend le
  mauvais pattern (`run-all` → `run --all`). Ce qui peut devenir un check en
  devient un.
- **La CI d'un module** : skill-validator, workflow partagé épinglé, Dependabot.
- **La doc d'un outil est aussi un skill** : le skill `pollen` livré avec pollen.
- **Comment fait Google ?** Evals obligatoires et hebdomadaires : notre
  prochaine marche.

## 8. Clôture — 2 min (slides 31–33)

- À retenir, un point chacun : skills plutôt qu'un CLAUDE.md géant ; par
  projet, épinglés ; gouvernés comme du code.
- **Essayez-le** : QR pollen et QR de nos skills en public (`tosun-si/skills-core`),
  la commande d'installation ; 10 secondes pour scanner.
- **Punchline :** « Pas par magie : parce que les règles sont là. »
- La slide de fin porte le QR feedback de l'événement (DevFest : à ajouter
  dans `FEEDBACK_QR` ; Cloud Nord : OpenFeedback) et nos deux LinkedIn ; elle
  reste affichée pendant les questions.

---

## Ajuster à la répétition

- **Trop long** : passer en annexe « Et Spec Kit, BMAD ? » (slide 24) et « La
  doc d'un outil est aussi un skill » (slide 29) ; écourter le Beat 6.
- **Cloud Nord (≈ 50 min)** : les 5 minutes de plus vont aux questions, pas au
  contenu.
- La démo est le seul bloc à durée variable : chronométrer AVEC sur le réseau
  de la salle.

## Note technique — la session « sans skills » pour le contraste

**Vérifié sur Claude Code v2.1.280** (test réel en `-p`, 23/09/2026), et
utilisé tel quel pour les tests de démo du 27/10/2026 (v2.1.309). Toggle
**non destructif** — juste des flags, rien à restaurer après :

```bash
# SANS (baseline générique) : ni CLAUDE.md, ni mémoire, ni skills (user, projet, plugins, built-in)
claude --safe-mode --disable-slash-commands

# AVEC : dans skills-demo, après `pollen update`
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

- ❌ **`--bare` ne marche pas avec un login Claude (OAuth)** : il n'accepte que
  `ANTHROPIC_API_KEY` / `apiKeyHelper`.
- `--safe-mode` coupe toutes les personnalisations (CLAUDE.md, skills,
  plugins installés, hooks, MCP, agents…) mais garde l'auth et les built-in ;
  `--disable-slash-commands` retire le reste des skills (built-in compris).
- **Impossible de désactiver les skills dans une session déjà lancée** : leur
  liste est injectée au démarrage. Pour le « sans », toujours une session neuve
  (un 2ᵉ terminal).
- ⚠️ **À répéter** : rejouer le tableau sur la machine de démo (version CLI
  figée la veille).
