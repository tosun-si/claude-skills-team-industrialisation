# Dialogue Mazlum × Guillaume (proposition, à affiner)

Répartition des 32 slides entre les deux speakers, avec les passages de relais.
Le texte est une base orale, pas un script à réciter : chacun le reformule à sa
façon. Les notes de chaque slide gardent le fond, sous un repère de scène condensé
(`CUES` dans `talks/slides_content.py`).

**Principes**

- Celui qui parle a la télécommande. Le passage de relais se fait par une
  question ou une phrase qui ouvre la slide suivante, jamais par « je laisse la
  parole à… ».
- Répartition par affinité : Mazlum porte le contexte, les skills et le message ;
  Guillaume porte l'outillage (sync, pollen, CI) et la fiabilité.
- Pendant la démo, l'un pilote le clavier, l'autre commente pour la salle. On
  inverse à chaque beat.
- `[à confirmer]` = un fait à vérifier ensemble avant de le dire sur scène.

| Bloc | Slides | Qui |
|---|---|---|
| Ouverture | 1–3 | Les deux |
| Le problème | 4–6 | Mazlum → Guillaume → Mazlum |
| Du CLAUDE.md aux skills | 7–13 | Alternance |
| Partager les skills | 14–18 | Guillaume, puis Mazlum |
| pollen | 19–24 | Guillaume, Mazlum sur npx skills et sa config |
| Démo | 25 | Alternance par beat |
| Gouvernance | 26–30 | Mazlum, Guillaume sur la fiabilité |
| Clôture | 31–32 | Les deux |

---

## Ouverture

### 1 · Industrialiser l'IA en équipe — *Mazlum*

> **Mazlum** : Bonjour à tous ! Générer du code avec une IA, aujourd'hui, c'est
> trivial. Le générer comme votre équipe l'attend, c'est une autre histoire.
>
> **Guillaume** : Et c'est cette histoire-là qu'on vient vous raconter.

### 2 · Qui sommes-nous ? — *chacun présente l'autre*

> **Mazlum** : Guillaume, Platform Engineer et SRE chez GroupBees. Fondateur de
> THEREALM, et formateur à EPITECH et Polytech. C'est lui qui m'empêche de
> mettre en prod le vendredi.
>
> **Guillaume** : Et Mazlum, Head of Data chez GroupBees, GDE Cloud et Docker
> Captain. Lui, c'est celui qui écrit les règles… et qui les oublie dans son
> propre Dockerfile.
>
> **Mazlum** : C'est exactement le sujet du talk.

### 3 · En direct du TechCast — *les deux, 10 secondes*

> *(l'image façon Guignols s'affiche, on laisse rire la salle)*
>
> **Guillaume** : Au programme du JT : comment GroupBees a standardisé ses
> conventions avec les Agent Skills.
>
> **Mazlum** : Et ça commence par notre plateforme.

---

## Le problème

### 4 · Le contexte : une plateforme d'API — *Mazlum*

> **Mazlum** : Chez GroupBees, on construit une plateforme de registre d'API :
> des producteurs publient leurs API, des consommateurs les découvrent, et de
> l'IA par-dessus pour générer. La stack est moderne mais exigeante : archi
> hexagonale, Terragrunt, Workload Identity, IAP. `[à confirmer : une phrase
> sur ce que l'IA génère sur la plateforme]`
>
> **Mazlum** (relais) : Et derrière, une équipe qui n'a pas le même niveau sur
> tout ça. Guillaume ?

### 5 · L'équipe — *Guillaume*

> **Guillaume** : On est huit : quelques seniors, un junior, un stagiaire. Les
> seniors ont posé le premier backend, les fondations cloud et l'IaC. Et grâce à
> Claude, tout le monde a pu faire évoluer ces stacks. Ça, c'est la bonne
> nouvelle.
>
> **Mazlum** : La mauvaise, c'est la suite.

### 6 · Le problème : ça diverge — *Mazlum*

> **Mazlum** : Dès qu'il fallait créer quelque chose de neuf (un nouveau service,
> une nouvelle stack IaC), nos conventions disparaissaient. Chacun son Claude,
> chacun son CLAUDE.md. L'IA est douée, mais elle ne connaît pas NOS règles.
>
> **Guillaume** : Donc on a fait ce que tout le monde fait.

---

## Du CLAUDE.md aux skills

### 7 · Première idée : un CLAUDE.md commun — *Guillaume*

> **Guillaume** : Premier réflexe : un CLAUDE.md partagé. Toutes nos règles au
> même endroit, tout le monde le charge. Simple.
>
> **Mazlum** : Simple… pendant deux semaines.

### 8 · Le CLAUDE.md qui grossit — *Guillaume*

> **Guillaume** : *(montrer le vrai fichier qui scrolle)* Docker, Terraform,
> commits, tests, déploiement… Le problème n'est pas le contenu. C'est qu'il est
> chargé tout le temps : quand j'écris un message de commit, l'agent relit nos
> règles de Dockerfile. Ça coûte des tokens et ça dilue l'attention.
>
> **Mazlum** : Alors on l'a découpé.

### 9 · Du monolithe aux modules : les skills — *Mazlum*

> **Mazlum** : Un skill, c'est un CLAUDE.md modulaire, chargé à la demande.
> Une convention, un skill. Et l'agent ne charge que ce dont la tâche a besoin.

### 10 · Anatomie d'un skill — *Mazlum*

> **Mazlum** : Un dossier, un fichier SKILL.md, au standard ouvert Agent Skills.
> Le point clé, c'est la description : l'agent la voit en permanence et ne lit le
> corps que si la tâche correspond. C'est la progressive disclosure.
>
> **Guillaume** : Et un skill, ce n'est pas que du texte.

### 11 · Un skill, c'est un dossier — *Guillaume*

> **Guillaume** : À côté du SKILL.md, trois dossiers optionnels. `references/` :
> de la doc lue à la demande, un projet Node lit `node.md` et pas les autres.
> `assets/` : des fichiers complets à copier, comme notre Dockerfile Python.
> `scripts/` : des contrôles à exécuter plutôt qu'à décrire.
>
> **Mazlum** : Ce qui ne veut pas dire qu'on jette le CLAUDE.md.

### 12 · CLAUDE.md monolithe vs skills — *Mazlum*

> **Mazlum** : Il redevient ce qu'il doit être : le contexte durable du projet.
> Chez nous, un AGENTS.md, et un CLAUDE.md d'une ligne qui pointe dessus. Les
> conventions, elles, vivent dans les skills.

### 13 · Modulariser : des domaines qui se composent — *Guillaume*

> **Guillaume** : Et on découpe par domaines qui se composent. Un skill Docker
> générique, agnostique du langage. Un skill Python qui se pose par-dessus et
> n'ajoute que le spécifique. Chaque skill reste petit, et le générique sert à
> tous les autres langages.
>
> **Mazlum** : Restait à les partager dans l'équipe.

---

## Partager les skills

### 14 · Partager : un catalogue synchronisé en global — *Guillaume*

> **Guillaume** : Première approche : un repo git de skills, synchronisé sur la
> machine de chaque dev.

### 15 · Un module de skills, synchronisé en global — *Guillaume*

> **Guillaume** : Un script copie chaque skill dans les dossiers personnels que
> lisent les agents. Plusieurs modules cohabitent, la version, c'est un tag git.
> Ça a très bien marché…
>
> **Mazlum** : … jusqu'à ce que je l'utilise chez un client.

### 16 · Global : la limite — *Mazlum*

> **Mazlum** : En global, nos règles s'appliquent partout : sur mes projets
> perso, et chez un client qui a ses propres conventions. Ce sont de bonnes
> pratiques, mais on veut choisir. Projet par projet.
>
> **Guillaume** : Et choisir des skills par projet, c'est gérer des dépendances.

### 17 · Par projet : un gestionnaire de skills — *Guillaume*

> **Guillaume** : On ne copie pas les skills dans chaque projet : on les importe,
> comme des dépendances. Chaque projet déclare les skills d'équipe dont il a
> besoin, plus ses propres skills. Et la factory va accueillir d'autres projets
> que Solis : chacun fera sa sélection.
>
> **Mazlum** : À une condition : ne rien inventer de propriétaire.

### 18 · S'appuyer sur les standards — *Mazlum*

> **Mazlum** : Un skill, c'est le standard Agent Skills. Le même fichier est lu
> par Claude Code, Copilot, Cursor, Codex, Antigravity CLI. Le contexte du projet,
> c'est AGENTS.md, un autre standard. Si l'équipe change d'agent demain, les
> skills restent.
>
> **Mazlum** (relais) : Il manquait juste l'outil pour les installer. Guillaume,
> raconte-leur pollen.

---

## pollen

### 19 · pollen : les skills comme des dépendances — *Guillaume*

> **Guillaume** : pollen, notre CLI open source, écrite en Rust. Un fichier,
> `pollen.yaml`, inspiré de pre-commit : une liste de sources, chacune épinglée.
> `pollen update` installe, rafraîchit ce qui a bougé et supprime ce qu'on a
> retiré.

### 20 · pollen, en pratique — *Guillaume*

> **Guillaume** : On assume un périmètre étroit : pollen déplace des dossiers et
> les valide contre la spec. Il sait ce qu'il a installé : un skill écrit à la
> main n'est jamais écrasé.
>
> **Mazlum** : Et la question qu'on nous pose à chaque fois : où est le lockfile ?

### 21 · Épingler un commit… et pas de lockfile — *Guillaume*

> **Guillaume** : Il n'y en a pas, volontairement. Un lockfile fige ce qu'un
> résolveur a choisi : des plages de versions, des dépendances transitives.
> pollen n'a ni l'un ni l'autre. Le commit épinglé EST le lock, et le tag en
> commentaire le rend lisible. `pollen outdated` vous dit qu'une release est
> sortie, `autoupdate` met à jour le SHA, et ça passe en PR.
>
> **Mazlum** : Et l'autre question, sous mon post LinkedIn : pourquoi pas npx
> skills ?

### 22 · Et npx skills ? — *Mazlum, Guillaume conclut*

> **Mazlum** : npx skills, de Vercel, est un super outil, bien plus large que le
> nôtre. Et il sait installer nos catalogues privés aussi.
>
> **Guillaume** : La différence est dans le modèle. Eux : une CLI qui trace ce
> qu'on a installé dans un lockfile. Nous : un fichier déclaratif façon
> pre-commit, à la racine de n'importe quel repo, Terraform ou Python, sans
> package.json. Et épinglé sur le commit d'une release. `[à confirmer :
> Guillaume avait fait l'état de l'art avant de démarrer pollen, à raconter en
> une phrase]`
>
> **Mazlum** : Et les deux installent les mêmes skills. Aucun lock-in.

### 23 · Un fichier, trois propriétaires — *Mazlum*

> **Mazlum** : Ma vraie config machine : des modules de l'orga, privés et
> publics, le skill de pollen lui-même, et un module perso sur mon compte. Les
> règles de l'équipe et les miennes se composent, sans se mélanger.
>
> **Guillaume** : Et on nous demande aussi : vous réinventez Spec Kit ?

### 24 · Et Spec Kit, BMAD ? — *Guillaume*

> **Guillaume** : Spec Kit et BMAD sont eux aussi livrés en Agent Skills, mais
> ils encodent un processus : spec, plan, tâches. Nous, on encode des
> conventions techniques. Même format, autre contenu : ils se composent.
>
> **Mazlum** : Assez parlé. Montrons-le.

---

## Démo (≈ 13 min, voir `script-demo.md`)

Deux terminaux côte à côte : SANS à gauche, AVEC à droite. Celui qui pilote ne
commente pas, l'autre raconte pour la salle.

### 25 · Même prompt, sans puis avec les skills

**Beat 0 · Cadrage (30 s)** — *Mazlum parle*

> **Mazlum** : Même idée, même prompt, deux fois. Une fois sans nos skills, une
> fois avec. Regardez la différence.

**Beat 1 · SANS skills (≈ 2 min 30)** — *Mazlum pilote, Guillaume commente*

> **Guillaume** : Mazlum lance une session vierge : pas de CLAUDE.md, pas de
> skills. Il colle le prompt… *(pendant la génération)* Ça tourne, c'est propre…
> Dockerfile en un seul stage, en root. Une citation sans auteur ni langue.
>
> **Mazlum** : C'est correct. Ça marche. Mais ce n'est pas comme NOUS, on code.

**Beat 2 · pollen charge les skills (≈ 2 min)** — *Guillaume pilote, Mazlum commente*

> **Mazlum** : À droite, Guillaume est dans le projet. Le projet déclare ses
> skills dans `pollen.yaml`… et le dossier des skills est vide.
>
> **Guillaume** : `pollen update`. *(défilement)* Quinze skills, dont celui-là :
> `quote-domain`. Il n'existe que dans ce projet : les règles métier de l'app.

**Beat 3 · AVEC skills (≈ 4 min)** — *Guillaume pilote, Mazlum commente*

> **Mazlum** : Même prompt, au caractère près. *(pendant la génération)*
> Regardez l'arbo : domain, application, infrastructure. Le Dockerfile :
> multi-stage, non-root.
>
> **Guillaume** : Et `quote.py` : auteur obligatoire, 280 caractères maximum, une
> langue, et `?lang=fr`. Le prompt n'en parlait pas : ça vient du skill du
> projet.

**Beat 4 · Le delta (≈ 2 min 30, climax)** — *ping-pong, une paire chacun*

> **Mazlum** : Dockerfile : un stage en root, contre multi-stage non-root.
>
> **Guillaume** : Arbo : à plat, contre trois couches.
>
> **Mazlum** : Le modèle : un texte, contre texte, auteur et langue validés.
>
> **Guillaume** : Commit et PR : génériques, contre nos conventions.
>
> **Mazlum** : L'IA n'est pas devenue meilleure entre les deux.
>
> **Guillaume** : Les règles sont là.

**Beat 5 · Déploiement, la cerise (≈ 2 min)** — *Guillaume pilote, Mazlum commente*

> **Guillaume** : La pipeline GitHub Actions est verte… `/quote?lang=fr`.
>
> **Mazlum** : Une citation en français, avec son auteur. De l'idée à l'URL en
> prod, aux conventions de l'équipe.

**Filets** : génération trop lente → sorties pré-capturées ou branche
`reference` ; pipeline KO → l'URL est déjà ouverte. Celui qui ne pilote pas
décide de basculer, pour que celui qui pilote reste concentré.

> **Guillaume** (sortie de démo) : Mais une bibliothèque de skills, ça se
> gouverne. Sinon, on recrée le monolithe qu'on a fui.

---

## Gouvernance

### 26 · Une lib de skills, ça se gouverne — *Mazlum*

> **Mazlum** : Les skills, c'est du code : versionnés, relus en PR. Et le blast
> radius est énorme : un skill s'applique à tout ce qu'on génère. Qui relit ?
> Les skills transverses, Guillaume et moi, qui les avons posés. Les skills d'un
> domaine, ceux qui le connaissent mieux que nous. On est huit, pas Google.
>
> **Guillaume** : Et même relu, un skill finit par vieillir.

### 27 · Quand un skill périme — *Guillaume*

> **Guillaume** : Une règle périmée n'échoue pas : elle apprend le mauvais
> pattern à l'agent, en silence. Ce qui pourrit, c'est le volatil : les flags,
> les versions. On l'a vécu : un skill Terragrunt avec `run-all`, alors que le
> CLI impose `run --all`.
>
> **Mazlum** : Ça, un agent le repère très bien. « Est-ce encore notre
> convention ? », beaucoup moins : ça reste humain.
>
> **Guillaume** : Et quand une règle peut devenir un check, on en fait un. Elle
> casse fort en CI au lieu de pourrir. Ce qu'on n'a pas encore : des evals.

### 28 · La CI d'un module de skills — *Guillaume*

> **Guillaume** : Chaque module de skills a sa CI : skill-validator contrôle la
> spec, les liens cassés, les fichiers orphelins, la taille. Un workflow partagé,
> épinglé par commit, et Dependabot le met à jour.
>
> **Mazlum** : Et on a appris une chose en route.

### 29 · La doc d'un outil est aussi un skill — *Mazlum*

> **Mazlum** : À la première montée de version de pollen, il a fallu retoucher
> treize fichiers dans nos modules. Le CLAUDE.md monolithique qu'on dénonce…
> dupliqué. Maintenant, la connaissance de pollen est un skill livré avec pollen.
>
> **Guillaume** : Et pour aller plus loin, on a regardé chez les gros.

### 30 · Comment fait Google ? — *Mazlum*

> **Mazlum** : Google a publié comment ils gèrent leurs skills. « Skills are
> products, not snippets. » Des evals obligatoires, hebdomadaires, sur plusieurs
> agents. C'est là qu'on n'en est pas encore, et c'est notre prochaine marche.
> Adaptez la gouvernance à votre taille, mais gardez-en une.

---

## Clôture

### 31 · À retenir — *un point chacun, puis le troisième à deux*

> **Mazlum** : Un : les conventions dans des skills, chargés à la demande, pas
> dans un CLAUDE.md géant.
>
> **Guillaume** : Deux : des skills par projet, épinglés comme des dépendances.
>
> **Mazlum** : Trois : gouvernés comme du code.
>
> **Guillaume** : Relecture, CI… et bientôt des evals.

### 32 · Pas par magie. — *les deux*

> **Mazlum** : Ce n'est pas par magie que l'IA a codé comme nous.
>
> **Guillaume** : C'est parce que les règles sont là.
>
> **Mazlum** : Merci ! On prend vos questions.

---

## Q&A : qui répond à quoi

| Sujet | Qui |
|---|---|
| pollen, Rust, npx skills, Windows | Guillaume |
| Skills, écriture, Claude Code, AGENTS.md | Mazlum |
| Gouvernance, référents, Orange | Mazlum |
| CI, skill-validator, evals | Guillaume |
| GCP, Cloud Run, IAP, la démo | Celui qui a piloté le beat |
