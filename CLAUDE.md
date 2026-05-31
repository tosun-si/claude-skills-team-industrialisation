# CLAUDE.md — Talk « Industrialiser l'IA en équipe avec des skills »

Contexte de préparation d'un **talk de conférence (FR)** + futur article de blog.
Sujet : comment industrialiser l'usage de l'IA (Claude Code) dans une équipe via
une **bibliothèque de skills modulaires partagés** qui encodent les conventions
de l'équipe.

> Ce fichier capture le contexte et les décisions prises lors du brainstorming,
> pour pouvoir reprendre la prépa (titre/abstract → déroulé → slides → démo)
> sans tout reconstruire.

---

## Thèse / message central

Générer du code avec une IA est devenu trivial. Le faire **aux conventions de
l'équipe** (archi, Dockerfile, CI, tests, PR, déploiement) est une autre
histoire — c'est la limite du *vibe coding* individuel. Les **skills** encodent
ces conventions et les rendent **activables à la demande, pour toute l'équipe**.

Punchline : **« Pas par magie : parce que les règles sont là. »**

## Arc narratif

`CLAUDE.md` monolithique devenu ingérable → **bibliothèque de skills modulaires
et partagés** (Dockerfile multi-stage, archi hexagonale Python, conventions de
commits/PR, déploiement Cloud Run + IAP, Terragrunt, direnv…).

## Décisions prises (brainstorming)

- **Le cœur du talk = le CODE GÉNÉRÉ conforme**, pas le déploiement. Montrer :
  back Python hexagonal *comme l'équipe l'attend*, Dockerfile propre, CI propre,
  tests aux conventions, commit squashé + PR labellisée.
- **Le moment clé = le CONTRASTE** : même prompt **sans** skills (sortie
  générique) **vs avec** skills (nos conventions exactes). C'est ça qui prouve
  que ce sont les skills — et pas « l'IA douée » — qui font le boulot.
- **Déploiement GCP = cerise, pas climax.** Option retenue : app **déjà
  déployée** montrée en live, ou **lancer la pipeline GHA** (et même si elle
  tombe en erreur, montrer le résultat). **Pas de `gcloud deploy` à froid depuis
  le laptop** (risque wifi de conf + non-déterminisme Cloud Run/IAP).
- **App de démo : minuscule et sans dépendances** — FastAPI hexa, 1–2 endpoints,
  **stateless, pas de DB, pas de secrets**, et **public (`--allow-unauthenticated`)
  ou IAP pré-configuré** (ne pas rejouer le flow login IAP en live).
- **Anti-pattern à éviter : l'effet catalogue.** Garder UN fil rouge (les skills
  comme savoir d'équipe), les artefacts servent de preuves.
- **Transposabilité** assumée : méthodo applicable à Cursor, Copilot.

## Part d'ombre / gouvernance & maintenance (= argument de crédibilité)

Ne pas faire un talk 100 % upside. Assumer que **une lib de skills, ça se
gouverne** :

- **Les skills sont du code → versionnés + relus en PR.** Barre de review *plus
  haute* que du code normal : un skill s'applique à **tout** ce qui sera généré,
  par **toute** l'équipe (blast radius / amplification).
- **L'IA *drafte*, l'humain *possède* et merge.** L'IA peut proposer des MAJ de
  skills (excellent usage) ; le merge sans revue est le problème, pas le draft.
- **L'IA tend à sur-généraliser** : encoder un fix one-shot en règle universelle.
  Un humain tranche « convention d'équipe ou cas spécifique ? ».
- **Revue périodique par l'IA en *scanner* de péremption** : bonne pour la
  péremption *factuelle* (un flag/une version existe-t-il encore ?), faible pour
  la péremption *de jugement* (est-ce encore notre convention ?). → ouvre une PR,
  un humain merge.
- **Séparer le durable du volatil** dans la structure même du skill : *concepts/
  archi* (hexagonal, non-root au runtime…) = stable ; *mécanique* (flags,
  versions, commandes) = pourrit vite. La revue cible la zone volatile.
- **Capture à chaud** : un gotcha rencontré remonte dans le skill dans la foulée
  (item de checklist PR), pas dans une réunion « MAJ skills » qui n'arrive jamais.
- **Owners** (`CODEOWNERS` par domaine) : « l'équipe maintient en continu » sans
  propriétaire = personne ne le fait.
- **Diffusion** : repo de skills importable par les membres → attention au
  versioning/pinning (si tout le monde `pull latest`, un skill cassé casse toute
  l'équipe en même temps).
- **Risque** : sans gouvernance, on **recrée le `CLAUDE.md` monolithique
  ingérable**, juste éclaté en N fichiers.

## Exemples concrets (war stories à réutiliser sur scène)

- **Péremption factuelle** : un skill Terragrunt référençait `run-all` ; le CLI
  redessiné impose `run --all`. Cas parfait pour le scanner IA de péremption.
- **Capture à chaud d'un gotcha** : sur un déploiement Cloud Run + IAP réel, un
  `401 "could not be verified"` venait du proxy UI qui relayait l'en-tête
  `X-Serverless-Authorization` injecté par IAP (que Cloud Run préfère à
  `Authorization`). Fix → ajouté comme gotcha au skill `cloud-run-iap`. Illustre
  « le savoir s'accumule au point de douleur ».

## Matière première (source des exemples)

- **Skills GroupBees** (`~/.claude/skills/`) : `docker-image-conventions`,
  `python-docker-multistage`, `cloud-run-iap`, `cloud-run-cicd-gha`,
  `docker-bake-cache`, `terragrunt-modular-style`, `direnv-local-env`,
  `python-uv-direnv`, `commit-groupbees`, `pr-groupbees`, `tag-groupbees`,
  `cloud-build-conventions`.
- **Exemple réel de bout en bout** : le repo `gbf-solis-api-portal` (UI React +
  BFF Python/FastAPI hexagonal, Terragrunt IaC, CI/CD Cloud Run, IAP same-origin).

## Titre & abstract

Voir `abstract.md` (version courante) — en cours d'itération.

## Prochaines étapes

1. ✅ Titre choisi (option A : *Industrialiser l'IA en équipe : des skills qui
   encodent vos conventions*) + abstract révisé → `abstract.md`.
2. ✅ Déroulé timé écrit → `deroule.md`. Recette
   `claude --bare --disable-slash-commands` vérifiée sur la CLI v2.1.154 pour
   le contraste sans/avec.
3. ✅ Checklist anti-panne → `demo-prep.md`. Runbook beat-par-beat →
   `script-demo.md`. Prompt exact → `prompts.md`.
4. ✅ Notes orga + elevator pitch → `notes-orga.md`. Bio à remplir.
5. ✅ Prérequis skills : `python-hexagonal-clean-archi` existe désormais (le
   bloqueur démo est levé ; tableau dans `script-demo.md` à jour).
6. ⏭️ **Prochain step concret** : scaffolder `~/demo/quote-service/` —
   FastAPI hexa, 1 endpoint `GET /quote` + `GET /health`, Dockerfile,
   CI, tests aux conventions, commit squashé, PR labellisée. Sert de
   référence et de filet pour les répét'.
7. Screencast happy path complet + 1ʳᵉ répet' avec déclenchement de panne
   forcée (pour entraîner la bascule sur le filet).
8. Slides (captures des artefacts pour le plan B narratif).
