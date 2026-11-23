# Titre & abstract — version courante

## Titre

**✅ CHOISI — A :**
> Industrialiser l'IA en équipe : des skills qui encodent vos conventions

_Alternatives conservées au cas où :_

**B — garde le hook « vibe coding » (bon pour un CFP qui aime l'accroche) :**
> Du vibe coding au workflow d'équipe : industrialiser l'IA avec des skills partagés

**C — valeur en avant :**
> Faire coder l'IA aux conventions de l'équipe avec des skills partagés

## Abstract — version solo (défaut)

Générer du code avec une IA, c'est devenu trivial. Le faire **aux conventions de
votre équipe** — la bonne archi, les bons Dockerfile, la bonne CI, les tests
attendus, des PR propres — c'est une autre histoire. C'est là que le vibe coding
individuel atteint ses limites.

Je partage comment on a industrialisé Claude Code chez GroupBees : du `CLAUDE.md`
monolithique devenu ingérable jusqu'à une **bibliothèque de skills modulaires et
partagés** qui encodent nos best practices — archi hexagonale Python, Dockerfile
multi-stage, conventions de tests, commits propres, PR labellisées, déploiement
Cloud Run. Ce qui vivait dans la tête de chacun devient activable à la demande,
pour toute l'équipe.

En démo, je pars d'une idée et je génère une petite app : back Python hexagonal,
Dockerfile, CI/CD, tests aux conventions, commit squashé et PR — jusqu'au
déploiement sur GCP. Le moment clé n'est pas la magie, c'est le **contraste** :
la même demande sans les skills, puis avec. Les règles font la différence.

Mais une bibliothèque de skills, ça se **gouverne** : versionner, relire (un
skill s'applique à *tout* ce qui sera généré, par toute l'équipe), détecter ce
qui devient obsolète, maintenir en continu — sinon on recrée le monolithe
ingérable.

Vous repartirez avec une méthodologie transposable à d'autres assistants (Cursor,
Copilot) : passer du prompt qui marche au workflow qui scale.

## Abstract — version 2 speakers (DevFest Toulouse)

Générer du code avec une IA, c'est devenu trivial. Le faire **aux conventions de
votre équipe** — la bonne archi, les bons Dockerfile, la bonne CI, les tests
attendus, des PR propres — c'est une autre histoire. C'est là que le vibe coding
individuel atteint ses limites.

On partage comment on a industrialisé Claude Code chez GroupBees : du `CLAUDE.md`
monolithique devenu ingérable jusqu'à une **bibliothèque de skills modulaires et
partagés** qu'on a construits — et adoptés — ensemble, et qui encodent nos best
practices : archi hexagonale Python, Dockerfile multi-stage, conventions de tests,
commits propres, PR labellisées, déploiement Cloud Run. Ce qui vivait dans la tête
de chacun devient activable à la demande, pour toute l'équipe.

En démo, on part d'une idée et on génère une petite app : back Python hexagonal,
Dockerfile, CI/CD, tests aux conventions, commit squashé et PR — jusqu'au
déploiement sur GCP. Le moment clé n'est pas la magie, c'est le **contraste** :
la même demande sans les skills, puis avec. Les règles font la différence.

Mais une bibliothèque de skills, ça se **gouverne** : versionner, relire (un
skill s'applique à *tout* ce qui sera généré, par toute l'équipe), détecter ce
qui devient obsolète, maintenir en continu — sinon on recrée le monolithe
ingérable.

Vous repartirez avec une méthodologie transposable à d'autres assistants (Cursor,
Copilot) : passer du prompt qui marche au workflow qui scale.

## Abstract — Devoxx France (1 200 caractères max)

Version courte, alignée sur la démo réelle (SANS / AVEC, pas de déploiement
en live). 1 005 caractères. Texte brut : pas de backticks ni de tirets longs.

> Générer du code avec une IA, c'est devenu trivial. Le faire selon les conventions de votre équipe (architecture, Dockerfile, CI/CD, tests, PR), c'est une autre histoire. C'est là que le vibe coding individuel atteint ses limites.
>
> Chez GroupBees, on est passés d'un CLAUDE.md monolithique et ingérable à une bibliothèque de skills modulaires et partagés, basés sur le standard Agent Skills. Ils encodent nos pratiques : architecture hexagonale Python, Docker multi-stage, tests, Git, CI/CD et déploiement sur Cloud Run.
>
> En démo, on soumet la même demande à Claude Code, sans puis avec les skills, et on compare ce qui sort. Si le résultat change, ce n'est pas par magie : c'est parce que les règles sont là.
>
> Mais une bibliothèque de skills, ça se gouverne : revue, versioning, responsables, mise à jour des skills obsolètes. Sinon, on recrée le monolithe.
>
> Vous repartirez avec une méthode applicable à Claude Code, Cursor, Copilot et d'autres agents : passer du prompt qui marche au workflow qui scale.
