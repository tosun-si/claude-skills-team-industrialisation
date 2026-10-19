<!-- agents-md-manager:start — managed section, do not edit by hand -->
# claude-skills-team-industrialisation — Project context

> Project-level context for AI coding agents (Claude Code, GitHub Copilot,
> Cursor…). **Conventions live in the referenced skills; this file only holds what
> is NOT in a skill and NOT derivable from the files.**

## Identity

- **Domain**: conference talk + future blog article (French)
- **Project**: « Industrialiser l'IA en équipe : des skills qui encodent vos conventions »
- **Purpose**: prep material (abstract, timed outline, demo runbook, slides)
- **Speakers**: Mazlum Tosun & Guillaume Leroy (GroupBees) — first target: DevFest Toulouse

## Conventions — source of truth (referenced, NOT copied)

- `groupbees-slides` — the deck in `talks/` (content in `slides_content.py`, look in `generate_slides.py`)
- `commit-open-source` — commits in this repo (personal repo, not under `groupbees/`)
- `skills-module-generator` / `agents-md-manager` — how GroupBees skills modules and AGENTS.md are built (talk material)

## Project specifics

- **Language**: talk, slides and notes in French; this managed block in English.
- **Non-obvious decisions**: see the free zone below (brainstorm decisions, narrative arc).
<!-- agents-md-manager:end -->

<!-- Free zone — add durable, project-specific notes below. -->

# Contexte du talk (FR)

Contexte de préparation d'un **talk de conférence (FR)** + futur article de blog.
Sujet : comment industrialiser l'usage de l'IA (Claude Code) dans une équipe via
une **bibliothèque de skills modulaires partagés** qui encodent les conventions
de l'équipe.

## Speakers

- **Mazlum Tosun** — Head of Data GroupBees · Google Developer Expert Cloud ·
  Docker Captain.
- **Guillaume Leroy** — Platform Engineer & SRE GroupBees · Fondateur THEREALM ·
  Formateur EPITECH & Polytech (la partie formateur peut sauter si trop long).
- Co-auteurs de **skillmgr** (voir plus bas). Abstract « version 2 speakers »
  dans `abstract.md`, CFP dans `notes-orga-improved.md`.

## Thèse / message central

Générer du code avec une IA est devenu trivial. Le faire **aux conventions de
l'équipe** (archi, Dockerfile, CI, tests, PR, déploiement) est une autre
histoire — c'est la limite du *vibe coding* individuel. Les **skills** encodent
ces conventions et les rendent **activables à la demande, pour toute l'équipe**.

Punchline : **« Pas par magie : parce que les règles sont là. »**

## Arc narratif (cheminement retenu, sept. 2026)

1. **Contexte GroupBees** : plateforme de registre d'API (producers publient,
   consumers découvrent) avec de l'IA par-dessus pour générer. Équipe : quelques
   seniors, un junior, un stagiaire ; 8 personnes aujourd'hui (oct. 2026).
2. Les seniors posent backend + fondations cloud + IaC ; stack pas évidente pour
   tous. Grâce à Claude, chacun fait évoluer les stacks… mais les **nouveaux**
   backends / stacks IaC **divergent** (chacun son Claude, son CLAUDE.md global).
3. **CLAUDE.md partagé** → grossit, monolithique, coûteux en tokens.
4. → **Skills** (CLAUDE.md modulaire, chargé à la demande), puis organisation en
   **domaines composables** (ex. `docker-image-conventions` générique +
   `python-docker-multistage` qui le spécialise ; `direnv-local-env` +
   `python-uv-direnv`).
5. **Partage v1 : sync global** (`sync-skills.sh` → `~/.claude/skills` +
   `~/.agents/skills`, ledger par module, versions = tags git).
6. **Limite du global** : s'applique à tous les projets (non-GB, clients) → on
   veut choisir par projet.
7. **Par projet** : modules de skills aux standards **Agent Skills** (+ Agent
   Plugins pour le packaging) importés via un **gestionnaire de skills** (skillmgr).

La frise « parcours » des slides reprend 5 étapes : CLAUDE.md perso → CLAUDE.md
partagé → skills modulaires → sync global → skills par projet.

## Décisions prises (brainstorming)

- **Le cœur du talk = le CODE GÉNÉRÉ conforme**, pas le déploiement.
- **Le moment clé = le CONTRASTE** : même prompt **sans** skills vs **avec**.
  Recette « sans » : `claude --safe-mode --disable-slash-commands` (vérifiée CLI
  v2.1.280 ; `--bare` exige une API key → « Not logged in » en OAuth).
- **Déploiement GCP = cerise, pas climax** : app déjà déployée ou pipeline GHA
  lancée en live ; **pas de `gcloud deploy` à froid depuis le laptop**.
- **App de démo minuscule** : FastAPI hexa, 1–2 endpoints, stateless, sans DB ni
  secrets, publique ou IAP pré-configuré.
- **Anti-pattern : l'effet catalogue.** UN fil rouge, les artefacts = preuves.
- **Transposabilité** assumée : Cursor, Copilot.

## Gouvernance (argument de crédibilité)

- Skills = code → versionnés + relus en PR, barre plus haute (blast radius).
- L'IA *drafte*, l'humain *possède* et merge ; l'IA sur-généralise les fixes.
- Scanner IA de péremption : bon sur le *factuel*, faible sur le *jugement*.
- Séparer durable (concepts) et volatil (flags, versions) dans chaque skill.
- Capture à chaud des gotchas ; relecture par un pair (n'importe qui sauf
  l'auteur) + CI, pas de CODEOWNERS (équipe de 8, modules privés en GitHub
  Free : CODEOWNERS y serait ignoré) — point à rediscuter en équipe ;
  pinning des versions.
- Sans gouvernance : on recrée le monolithe, éclaté en N fichiers.

## War stories

- **Péremption factuelle** : skill Terragrunt avec `run-all` → le CLI impose
  `run --all`.
- **Capture à chaud** : 401 « could not be verified » sur Cloud Run + IAP, dû au
  proxy UI qui relayait `X-Serverless-Authorization` → gotcha ajouté à
  `cloud-run-iap`.

## Écosystème skills GroupBees (matière première)

- **Modules** : `~/my-projects/groupbees/skills/` — `skills-core` (transverse),
  `skills-slides`, `skills-articles` ; d'autres à venir (dont par client).
  Chaque module : `skills-module.json`, `sync-skills.sh`, CI
  (`skill-validator check --strict`, table README générée, shellcheck).
  Deux époques, deux repos : `skills-core-legacy` (figé, sync global via
  `sync-skills.sh`) vs `skills-core` branche `use-skillmgr` (`skillmgr.yaml`
  local, `examples/` projet + global, `scripts/skills-catalog.sh`,
  `skillmgr validate` en CI). Conf globale : `~/.config/skillmgr/skillmgr.yaml`
  via `--config` (pas de chemin global par défaut dans skillmgr).
  Piège : skillmgr a un state par **target** → une seule config par
  répertoire cible (sinon les configs se prunent mutuellement).
- **État au 08/10/2026** : skillmgr renommé **pollen** (github.com/groupbees/pollen,
  public, v0.1.0, `brew install groupbees/tap/pollen`, config `pollen.yaml`).
  Repos publiés : `groupbees/skills-core` (**privé**, conventions GB, 17 skills)
  et `groupbees/skills-opensource` (**public** : `commit-open-source`,
  `tag-opensource`). Règle : commits/PR suivent l'orga ; les tags suivent la
  nature du projet (open source public, même dans groupbees → `tag-opensource`).
  `skills-module-generator` (skills-core) crée un module de bout en bout via
  `templates/new-module.sh`. Validateur : agent-ecosystem/skill-validator v1.6.2.
- **État au 09/10/2026** : pollen **v0.4.0** (`-g`, `outdated`,
  `autoupdate --freeze`, `validate --pinned`, une config par dossier cible,
  skill `pollen` livré dans `groupbees/pollen` `path: skills`). Convention
  d'épinglage : `revision: <sha>  # vX.Y.Z`, **pas de lockfile** (le SHA est
  le lock). Les modules ne réexpliquent plus pollen : ils renvoient au skill.
  CI des modules = workflow partagé public `groupbees/.github`
  (`skills-module.yml`, épinglé par SHA, bumpé par Dependabot). Rulesets sur
  `main` (pollen, skills-opensource, .github) ; impossible sur skills-core
  privé en offre GitHub gratuite.
  `groupbees/skills-slides` (privé, v0.1.0, skill `groupbees-slides`) publié
  via le générateur. `tosun-si/skills-articles` (public, perso, v0.1.0,
  `blog-article-footer`) créé avec `GITHUB_OWNER=tosun-si` : un module perso
  compose avec ceux de l'orga dans la même config pollen. `sync-skills.sh`
  n'installe plus rien ; config globale = 5 sources épinglées par SHA.
  `groupbees/skills-gitlab` (public, v0.1.0 : gitlab-commit, gitlab-mr,
  gitlab-release, gitlab-ci-shared-components) : chargé **uniquement** dans le
  `pollen.yaml` des projets GitLab (clients), jamais en global. Règle : module
  générique public ; règles propres à un client → module privé par client.
- **skillmgr** (ancien nom de pollen) — https://github.com/groupbees/skillmgr (Rust, Apache-2.0,
  Mazlum + Guillaume). `skillmgr.yaml` façon pre-commit (`repos[].repo /
  revision / paths[].path|recurse|exclude`, `repo: local`), `skillmgr update`
  → `.claude/skills` + `.agents/skills`. Pas de lockfile (branche = flottante),
  pas de registre, pas de résolution de dépendances. Renommage envisagé :
  **« Skillet » écarté** (nom très pris sur npm/PyPI, dont un package manager
  de skills).
- **Validateur** : https://github.com/agent-ecosystem/skill-validator.
- **Standards** : Agent Skills (agentskills.io, `SKILL.md`) ; **Agent Plugins**
  (agent-plugins.org, v1.0 août 2026 : `plugin.json` + `skills/<name>/` +
  `mcp.json`, packaging seulement — pas d'install ni de registre ; TSC Vercel,
  AWS, Cursor, Microsoft, OpenAI, Google ; **Anthropic absent**, Claude Code garde
  `.claude-plugin/plugin.json`).
- **Spec Kit (v1.0, GitHub) & BMAD (v6)** : eux aussi livrés en Agent Skills
  (`/speckit-*`, personas BMAD), mais ils encodent un **processus** (spec →
  plan → tasks), pas des conventions techniques — celles-ci s'y injectent en
  prose (`.specify/memory/constitution.md`, `persistent_facts` dans
  `_bmad/custom/`). Positionnement retenu : « même format SKILL.md, autre
  contenu : ils se composent » (slide « Et Spec Kit, BMAD ? »). Chacun a sa
  CLI de distribution par projet → même problème que skillmgr.
- **Concurrence / prior art** : `npx skills` (Vercel, lockfile `skills-lock.json`),
  plugins Claude Code déclarés par projet (`enabledPlugins` /
  `extraKnownMarketplaces` dans `.claude/settings.json`).
- **Google** (blog « Behind the scenes: how we build, test and scale Google agent
  skills », repo `google/skills`) : evals obligatoires à la soumission, evals
  hebdo multi-agents, métrique précision × efficacité, owners par skill,
  « skills are products, not snippets ».
- **Exemple réel de bout en bout** : repo `gbf-solis-api-portal` (UI React + BFF
  FastAPI hexagonal, Terragrunt, CI/CD Cloud Run, IAP same-origin).

## Slides

- `talks/` (skill `groupbees-slides`) :
  `uv run --with python-pptx python talks/generate_slides.py` →
  `talks/slides/talk_devfest_skills.pptx`. Types ajoutés au renderer :
  `speakers`, `journey` (frise + abeille sur l'étape courante), `compare`, et la
  clé `bees` (abeilles décoratives) sur toute slide.
- Abeilles dans `talks/assets/bee*.png` ; photos speakers `mazlum.jpg` /
  `guillaume.png` (sans photo, le renderer affiche les initiales).
- Export PDF via PowerPoint/Keynote : nécessite une session macOS déverrouillée.

## Prochaines étapes

1. ✅ Titre, abstract (solo + 2 speakers), déroulé timé, runbook démo, CFP.
2. ✅ Premier jet des slides (`talks/`) — itérer slide par slide.
3. ✅ Projet de démo `~/my-projects/groupbees/skills-demo/` →
   `groupbees/skills-demo` (**privé** ; public avant le DevFest une fois
   skills-core public et un projet GCP de démo dédié en place) : `pollen.yaml` (skills-core épinglé, domaines choisis) +
   skill projet `.skills/quote-domain` (auteur obligatoire, ≤ 280 car., `lang`
   + `?lang=fr`) = preuve visible du chargement projet. Runbook :
   `script-demo.md`. L'app « citation du jour » est générée en live.
   ⏭️ Générer l'app de référence (branche `reference`), la déployer.
4. Screencast happy path + répét' avec panne forcée.
5. Aligner `deroule.md` sur le nouvel arc narratif (sync global → par projet).
