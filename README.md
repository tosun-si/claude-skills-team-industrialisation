# Industrialiser l'IA en équipe : des skills qui encodent vos conventions

Prépa d'un **talk de conférence (FR)** + futur article de blog sur l'industrialisation
de l'usage de l'IA (Claude Code) dans une équipe, via une **bibliothèque de skills
modulaires partagés** qui encodent les conventions de l'équipe.

> **« Pas par magie : parce que les règles sont là. »**

## Thèse

Générer du code avec une IA est devenu trivial. Le faire **aux conventions de
l'équipe** — la bonne archi, les bons Dockerfile, la bonne CI, les tests attendus,
des PR propres — c'est une autre histoire. C'est la limite du *vibe coding*
individuel. Les **skills** encodent ces conventions et les rendent **activables à
la demande, pour toute l'équipe**.

L'arc : un `CLAUDE.md` monolithique devenu ingérable → une bibliothèque de skills
modulaires et partagés (Dockerfile multi-stage, archi hexagonale Python, conventions
de commits/PR, déploiement Cloud Run + IAP, Terragrunt, direnv…).

## Le moment clé : le contraste

La même demande **sans** les skills (sortie générique) **vs avec** (les conventions
exactes de l'équipe). C'est ça qui prouve que ce sont les skills — et pas « l'IA
douée » — qui font le boulot.

## Gouvernance (l'argument de crédibilité)

Une lib de skills, ça se **gouverne** : versionner, relire en PR (un skill s'applique
à *tout* ce qui sera généré, par toute l'équipe), détecter l'obsolescence, maintenir
en continu — sinon on recrée le monolithe ingérable, juste éclaté en N fichiers.

## Contenu du repo

| Fichier | Rôle |
|---|---|
| [`abstract.md`](abstract.md) | Titre choisi + abstract (version courante) |
| [`deroule.md`](deroule.md) | Déroulé timé du talk |
| [`script-demo.md`](script-demo.md) | Runbook beat-par-beat de la démo |
| [`demo-prep.md`](demo-prep.md) | Checklist anti-panne |
| [`prompts.md`](prompts.md) | Prompts exacts utilisés en démo |
| [`notes-orga.md`](notes-orga.md) | Notes orga + elevator pitch + bio |
| [`CLAUDE.md`](CLAUDE.md) | Contexte & décisions de prépa (pour reprendre sans tout reconstruire) |

## Transposabilité

La méthodologie s'applique à d'autres assistants (Cursor, Copilot) : passer du
prompt qui marche au workflow qui scale.
