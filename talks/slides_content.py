"""Slide-by-slide content — DevFest Toulouse (2 speakers, ~35 min + Q&A).

« Industrialiser l'IA en équipe : des skills qui encodent vos conventions »
Mazlum Tosun & Guillaume Leroy · GroupBees

Fil rouge (le « parcours », repris en frise) :
  1 CLAUDE.md perso → 2 CLAUDE.md partagé → 3 skills modulaires
  → 4 sync global → 5 skills par projet (package manager).

Abeilles décoratives : clé `bees` sur chaque slide, tuples
(fichier, x, y, hauteur[, rotation°[, flip]]) en pouces. Assets dans assets/ :
bee.png (clin d'œil), bee_happy.png, bee_cool.png (lunettes), bee_grad.png
(diplômée), bee_astro.png (astronaute).
"""

DECK_NAME = "talk_devfest_skills"
FOOTER_TEXT = "Industrialiser l'IA en équipe · DevFest Toulouse"

JOURNEY = [
    ("CLAUDE.md perso", "chacun son Claude"),
    ("CLAUDE.md partagé", "un fichier pour tous"),
    ("Skills modulaires", "chargés à la demande"),
    ("Sync global", "~/.claude/skills"),
    ("Skills par projet", "pollen.yaml"),
]

SLIDES = [
    # ── Ouverture ───────────────────────────────────────────────────────────
    {
        "type": "title",
        "title": "Industrialiser l'IA\nen équipe",
        "subtitle": "Des skills qui encodent vos conventions",
        "footer": "Mazlum Tosun & Guillaume Leroy · GroupBees · DevFest Toulouse 2026",
        "bees": [("bee_happy.png", 7.6, 0.45, 0.95, -12, True)],
        "notes": (
            "Bonjour à tous ! Générer du code avec une IA, aujourd'hui, c'est "
            "trivial. Le générer comme votre équipe l'attend, c'est une autre "
            "histoire. On va vous raconter comment on s'y est pris chez GroupBees."
        ),
    },
    {
        "type": "speakers",
        "title": "Qui sommes-nous ?",
        "speakers": [
            {
                "name": "Mazlum Tosun",
                "photo": "mazlum.jpg",
                "initials": "MT",
                "roles": [
                    "Head of Data · GroupBees",
                    "Google Developer Expert Cloud",
                    "Docker Captain",
                ],
                "badges": [("badge_gde.png", 0.38), ("badge_docker_captain.png", 0.7)],
                # Supporter du PSG : sticker en coin de carte.
                "sticker": ("badge_psg.png", 0.95, 12),
            },
            {
                "name": "Guillaume Leroy",
                # Photo carrée dans assets/ —
                # à défaut, les initiales s'affichent.
                "photo": "guillaume.png",
                "initials": "GL",
                "roles": [
                    "Platform Engineer & SRE · GroupBees",
                    "Fondateur · THEREALM",
                    "Formateur · EPITECH & Polytech",
                ],
            },
        ],
        "bees": [
            ("bee_cool.png", 11.75, 0.25, 1.1, 8),
            ("bee_grad.png", 11.6, 5.1, 1.25, -6),
        ],
        "notes": (
            "Mazlum : Head of Data chez GroupBees, GDE Cloud et Docker Captain. "
            "Guillaume : Platform Engineer & SRE chez GroupBees, fondateur de "
            "THEREALM, et formateur à EPITECH et Polytech."
        ),
    },
    {
        "type": "image",
        "title": "En direct du TechCast",
        "image_path": "assets/jt_satirique.jpg",
        "notes": (
            "Clin d'œil façon Guignols de l'info, on ne s'y attarde pas : "
            "« Comment GroupBees a standardisé ses conventions avec les Agent "
            "Skills ? C'est notre sujet. »"
        ),
    },
    # ── Contexte GroupBees ──────────────────────────────────────────────────
    {
        "type": "bullets",
        "title": "Le contexte : une plateforme d'API",
        "image": "bee_astro.png",
        "bullets": [
            "Un registre d'API : les producers publient, les consumers découvrent",
            "De l'IA par-dessus pour générer ce qui gravite autour",
            "Back Python / FastAPI en archi hexagonale",
            "GCP : Cloud Run, IAP, IaC Terragrunt",
            "CI/CD GitHub Actions, du trunk à la prod",
        ],
        "notes": (
            "TODO : préciser en une phrase ce que l'IA génère sur la plateforme. "
            "L'idée : poser une stack moderne mais exigeante — hexagonal, "
            "Terragrunt, WIF, IAP. Pas triviale pour tout le monde."
        ),
    },
    {
        "type": "bullets",
        "title": "L'équipe",
        "image": "bee_grad.png",
        "bullets": [
            "Une équipe de 8 personnes",
            "Quelques seniors… un junior… et un stagiaire",
            "Les seniors ont posé les fondations : backend, cloud, IaC",
            "Des concepts pas évidents à s'approprier pour tout le monde",
        ],
        "kicker": "Claude aide chacun à avancer. Mais chacun à sa façon.",
        "notes": (
            "Les seniors ont généré le premier backend, les fondations cloud et "
            "l'IaC — et, plus tard, les premiers skills transverses. Avec leur Claude, les autres ont réussi à faire évoluer ces "
            "stacks — c'est le côté positif."
        ),
    },
    {
        "type": "bullets",
        "title": "Le problème : ça diverge",
        "bullets": [
            "Chacun génère avec Claude Code dans son coin",
            "Chacun son CLAUDE.md global, ses habitudes, ses prompts",
            "Nouveau backend, nouvelle stack IaC : conventions ignorées",
            "Dockerfile, tests, CI, PR : huit devs, huit façons de faire",
        ],
        "kicker": "Même IA, même stack… et pourtant du code qui ne se ressemble pas.",
        "bees": [("bee.png", 11.85, 0.3, 1.05, 10)],
        "notes": (
            "Dès qu'il fallait générer quelque chose de nouveau — un nouveau "
            "service back, une nouvelle stack IaC — les conventions n'étaient "
            "pas respectées. L'IA est douée, mais elle ne connaît pas NOS règles."
        ),
    },
    # ── 2. Le CLAUDE.md partagé ─────────────────────────────────────────────
    {
        "type": "journey",
        "title": "Première idée : un CLAUDE.md commun",
        "steps": JOURNEY,
        "current": 1,
        "kicker": "Un fichier pour tous : la bonne idée… pour un temps.",
        "mascot": "bee_happy.png",
        "notes": (
            "Premier réflexe, naturel : on écrit un CLAUDE.md qu'on se partage. "
            "Toutes nos règles au même endroit."
        ),
    },
    {
        "type": "bullets",
        "title": "Le CLAUDE.md qui grossit",
        "bullets": [
            "Ça marche… au début",
            "Chaque règle ajoutée pour tous, chargée à chaque session",
            "Un monolithe : Docker, Terragrunt, commits, tests… tout mélangé",
            "Coûteux en tokens, et du bruit pour l'IA",
            "Personne n'ose plus y toucher",
        ],
        "kicker": "On a recréé le monolithe qu'on refuse dans notre code.",
        "bees": [("bee_cool.png", 11.8, 0.3, 1.0, -8)],
        "notes": (
            "Montrer un vrai CLAUDE.md qui scrolle sans fin. Le problème n'est "
            "pas le contenu, c'est qu'il est chargé en permanence, même quand "
            "on écrit un commit et pas un Dockerfile."
        ),
    },
    # ── 3. Les skills ───────────────────────────────────────────────────────
    {
        "type": "journey",
        "title": "Du monolithe aux modules : les skills",
        "steps": JOURNEY,
        "current": 2,
        "kicker": "Découper, et ne charger que ce dont la tâche a besoin.",
        "mascot": "bee.png",
        "notes": (
            "Naturellement, on a découpé : c'est l'idée des skills. Un CLAUDE.md "
            "modulaire, chargé à la demande."
        ),
    },
    {
        "type": "code",
        "title": "Anatomie d'un skill",
        "code": (
            "# skills/docker/docker-image-conventions/SKILL.md\n"
            "---\n"
            "name: docker-image-conventions\n"
            "description: Stack-agnostic conventions for production Dockerfiles —\n"
            "  multi-stage, non-root at runtime, smallest viable base image...\n"
            "  Trigger when creating, editing, or reviewing any Dockerfile.\n"
            "---\n"
            "\n"
            "# Production Docker images — multi-stage + non-root\n"
            "1. Multi-stage build : builder + runtime\n"
            "2. Non-root user at runtime\n"
            "..."
        ),
        "kicker": "Seule la description est toujours chargée. Le corps, à la demande.",
        "notes": (
            "Un skill = un dossier, un SKILL.md, le standard ouvert Agent Skills "
            "(agentskills.io). La description sert de déclencheur : l'agent la "
            "voit en permanence, et ne lit le corps que si la tâche matche. "
            "C'est la progressive disclosure. Lu tel quel par Claude Code, "
            "Copilot, Cursor, Codex, Antigravity CLI."
        ),
    },
    {
        "type": "code",
        "title": "Un skill, c'est un dossier",
        "code": (
            "skills/\n"
            "├── docker/python-docker-multistage/\n"
            "│   ├── SKILL.md          # les règles : lu au déclenchement\n"
            "│   └── assets/           # copié dans le projet, puis adapté\n"
            "│       ├── Dockerfile\n"
            "│       └── dockerignore\n"
            "├── docker/docker-image-conventions/\n"
            "│   ├── SKILL.md\n"
            "│   └── references/       # lu seulement si la tâche le demande\n"
            "│       └── node.md  jvm.md  go.md  rust.md  nginx.md\n"
            "└── git/tag-groupbees/\n"
            "    ├── SKILL.md\n"
            "    └── scripts/          # exécuté, jamais lu : 0 token\n"
            "        └── pre-tag-check.sh"
        ),
        "kicker": "SKILL.md dit quoi faire. scripts/, references/, assets/ : avec quoi.",
        "bees": [("bee_cool.png", 11.85, 0.25, 1.0, 8)],
        "notes": (
            "Le standard Agent Skills prévoit trois dossiers optionnels à côté "
            "du SKILL.md. references/ : de la doc lue à la demande — sur un "
            "projet Node, l'agent lit node.md, pas les quatre autres. assets/ : "
            "des fichiers complets à copier — le Dockerfile Python, celui qui "
            "tourne en prod sur Solis. scripts/ : du code exécuté, jamais chargé "
            "dans le contexte — une convention vérifiable devient un script "
            "plutôt qu'une phrase. Trois niveaux de chargement : la description "
            "toujours, le SKILL.md au déclenchement, le reste seulement si "
            "besoin. Notre CI refuse tout autre dossier. → Bascule IDE sur "
            "skills-core pour ouvrir ces trois skills."
        ),
    },
    {
        "type": "compare",
        "title": "CLAUDE.md monolithe vs skills",
        "left": {
            "title": "CLAUDE.md monolithe",
            "items": [
                "Tout chargé, tout le temps",
                "Un fichier, tous les sujets",
                "Relu par personne",
                "Spécifique à un outil",
            ],
        },
        "right": {
            "title": "Skills",
            "items": [
                "Chargés quand la tâche le demande",
                "Un skill = une convention",
                "Versionnés et relus en PR",
                "Standard ouvert, multi-agents",
            ],
        },
        "kicker": "Le CLAUDE.md reste : fin, pour le contexte du projet.",
        "notes": (
            "On ne jette pas le CLAUDE.md : il redevient ce qu'il doit être, le "
            "contexte durable du projet (chez nous un AGENTS.md + un pont "
            "CLAUDE.md). Les conventions, elles, partent dans les skills."
        ),
    },
    {
        "type": "code",
        "title": "Modulariser : des domaines qui se composent",
        "code": (
            "skills/\n"
            "├── docker/\n"
            "│   ├── docker-image-conventions/   # universel : multi-stage, non-root\n"
            "│   └── python-docker-multistage/   # + Python : uv, slim vs alpine\n"
            "├── env/\n"
            "│   └── direnv-local-env/           # universel : .envrc, pas de .env\n"
            "├── python/\n"
            "│   ├── python-uv-direnv/           # + Python : venv uv via direnv\n"
            "│   └── python-hexagonal-clean-archi/\n"
            "├── git/        # commit-, pr-, tag-groupbees\n"
            "├── gcp/        # cloud-run-iap\n"
            "└── terraform/  # terragrunt-modular-style"
        ),
        "kicker": "Un skill générique + un skill qui le spécialise, plutôt qu'un gros skill.",
        "notes": (
            "L'exemple de découpage : docker-image-conventions est agnostique du "
            "langage ; python-docker-multistage se compose par-dessus et n'ajoute "
            "que le spécifique Python. Même logique direnv / python-uv-direnv. "
            "Chaque skill reste petit, et le générique sert aux autres stacks."
        ),
    },
    # ── 4. Sync global ──────────────────────────────────────────────────────
    {
        "type": "journey",
        "title": "Partager : un catalogue synchronisé en global",
        "steps": JOURNEY,
        "current": 3,
        "kicker": "Un catalogue git, installé sur chaque poste.",
        "mascot": "bee_cool.png",
        "notes": (
            "Il fallait ensuite partager ces skills. Première approche : un "
            "catalogue git, synchronisé sur la machine de chaque dev."
        ),
    },
    {
        "type": "code",
        "title": "Un module de skills, synchronisé en global",
        "code": (
            "# skills-core/  (+ skills-slides, skills-articles, …)\n"
            "#   skills-module.json   → { name, description }\n"
            "#   skills/<domaine>/<skill>/SKILL.md\n"
            "\n"
            "git pull && ./sync-skills.sh --prune\n"
            "\n"
            "# → ~/.claude/skills/   Claude Code, Copilot VS Code, Cursor\n"
            "# → ~/.agents/skills/   Copilot JetBrains / CLI\n"
            "# ledger par module : --prune / --uninstall ne touchent que lui\n"
            "\n"
            "git checkout v1.2.0 && ./sync-skills.sh --prune   # épingler"
        ),
        "kicker": "Versionné par tags git, validé en CI. Simple, et ça marche.",
        "notes": (
            "Un module = un repo git. Le script copie chaque skill dans les "
            "répertoires personnels que lisent les outils. Plusieurs modules "
            "cohabitent grâce à un ledger par module. Version = tag git."
        ),
    },
    {
        "type": "compare",
        "title": "Global : la limite",
        "left": {
            "title": "Skills en global",
            "items": [
                "Actifs sur TOUS les projets",
                "Conventions GroupBees chez le client",
                "Une seule version pour tous les repos",
                "Le repo ne dit pas ce qu'il attend",
            ],
        },
        "right": {
            "title": "Skills par projet",
            "items": [
                "Chaque projet choisit ses modules",
                "GroupBees, client, perso : sans mélange",
                "Version épinglée par projet",
                "Déclaré et versionné avec le code",
            ],
        },
        "kicker": "De bonnes pratiques… mais on veut choisir où elles s'appliquent.",
        "bees": [("bee_happy.png", 11.9, 0.3, 1.0, 10)],
        "notes": (
            "Chargé en global, ça s'applique tout le temps, même sur nos projets "
            "non-GroupBees ou chez un client qui a ses propres règles. Même si ce "
            "sont de bonnes pratiques, on veut la flexibilité de choisir."
        ),
    },
    # ── 5. Par projet ───────────────────────────────────────────────────────
    {
        "type": "journey",
        "title": "Par projet : un gestionnaire de skills",
        "steps": JOURNEY,
        "current": 4,
        "kicker": "Importer des modules de skills, comme des dépendances.",
        "mascot": "bee_astro.png",
        "notes": (
            "D'où l'idée : ne pas copier les skills dans chaque projet, mais "
            "garder des modules de skills et les importer, comme des dépendances. "
            "Et la factory va accueillir de nouveaux projets après Solis : chacun "
            "déclarera les skills d'équipe dont il a besoin, plus ses propres "
            "skills spécialisés."
        ),
    },
    {
        "type": "bullets",
        "title": "S'appuyer sur les standards",
        "bullets": [
            "Agent Skills : un format ouvert, SKILL.md (agentskills.io)",
            "Lu tel quel par Claude Code, Copilot, Cursor, Codex, Antigravity CLI…",
            "AGENTS.md pour le contexte du projet, SKILL.md pour les conventions",
            "Vérifié en CI : skill-validator contrôle le format",
            "Ni installation ni épinglage dans le standard : c'est le rôle de pollen",
        ],
        "kicker": "Écrits une fois, lus par tous les agents : aucun lock-in.",
        "bees": [("bee.png", 11.8, 0.3, 1.0, -10, True)],
        "notes": (
            "On s'appuie sur des standards ouverts, rien de propre à un outil. "
            "Un skill, c'est un dossier avec un SKILL.md : le même fichier est lu "
            "par Claude Code, Copilot, Cursor, Codex ou Antigravity CLI. pollen le "
            "déploie dans .claude/skills et .agents/skills, le dossier commun "
            "aux autres agents : Claude Code, lui, ne lit encore que "
            ".claude/skills (vérifié sur la v2.1.303), d'où les deux cibles — et dans .github/skills si on veut Copilot : une ligne "
            "dans pollen.yaml. Si l'équipe change d'agent demain, les skills "
            "restent. AGENTS.md, lui aussi standard, porte le contexte durable "
            "du projet ; les conventions vivent dans les skills. Claude Code "
            "lit AGENTS.md nativement depuis la v2.1.277, mais seulement quand "
            "le repo n'a pas de CLAUDE.md : on garde donc un CLAUDE.md d'une "
            "ligne, @AGENTS.md, qui marche dans toutes les sessions et ne fait "
            "jamais lire le fichier deux fois. Si on nous "
            "parle d'Agent Plugins (le format de paquet, v1.0 en août 2026) : "
            "on ne l'utilise pas. Il ne lit que skills/<nom>/, nos domaines "
            "y seraient invisibles, et pollen n'en a pas besoin pour déployer."
        ),
    },
    {
        "type": "code",
        "title": "pollen : les skills comme des dépendances",
        "code": (
            "# pollen.yaml — committé à la racine du projet\n"
            "repos:\n"
            "  - repo: git@github.com:groupbees/skills-core.git\n"
            "    revision: 351fd495…  # v0.3.1\n"
            "    paths:\n"
            "      - path: skills/python      # on choisit ses domaines\n"
            "      - path: skills/docker\n"
            "  - repo: local                    # skills propres au projet\n"
            "    paths:\n"
            "      - path: .skills\n"
            "\n"
            "$ pollen update   # → .claude/skills/ + .agents/skills/"
        ),
        "kicker": "Le projet déclare ses conventions. Un seul fichier, relu en PR.",
        "notes": (
            "pollen, notre CLI open source (Rust). Syntaxe inspirée de "
            "pre-commit : une liste de sources, chacune épinglée. Il installe, "
            "rafraîchit ce qui a bougé et supprime ce qu'on a retiré. Sources "
            "git — SSH pour les repos privés — ou dossier local. Déployé dans "
            ".claude/skills et .agents/skills : tous les agents sont servis."
        ),
    },
    {
        "type": "bullets",
        "title": "pollen, en pratique",
        "image": "bee_cool.png",
        "bullets": [
            "Déclaratif : install, refresh, prune",
            "Par projet, ou pour la machine : pollen update -g",
            "Ne touche jamais un skill qu'il n'a pas installé",
            "Une config par dossier cible, pas de suppression croisée",
            "Pas un registre, pas de résolution de dépendances",
        ],
        "notes": (
            "On assume un périmètre étroit : pollen déplace des dossiers qui "
            "existent et les valide contre la spec. Son état (.pollen.json) "
            "enregistre ce qu'il a installé et quelle config possède le "
            "dossier : un skill écrit à la main n'est jamais écrasé, et une "
            "seconde config sur le même dossier est refusée."
        ),
    },
    {
        "type": "code",
        "title": "Épingler un commit… et pas de lockfile",
        "code": (
            "# un commit ne bouge pas — un tag peut, une branche bouge à chaque push\n"
            "revision: 4e1e8e25a2f32d8311cd52c5d9a703bad990e525  # v0.2.0\n"
            "\n"
            "$ pollen outdated\n"
            "skills-core  4e1e8e25 (v0.2.0)  -> v0.2.5\n"
            "\n"
            "$ pollen autoupdate --freeze     # réécrit le SHA et le tag\n"
            "$ pollen validate --pinned       # en CI : refuse tags et branches"
        ),
        "kicker": "Ni plage de versions, ni dépendance transitive : le SHA est le lock.",
        "notes": (
            "On nous demande souvent : et le lockfile ? Un lockfile fige ce "
            "qu'un résolveur a choisi : des plages de versions et des "
            "dépendances transitives. pollen n'a ni l'un ni l'autre. Le commit "
            "épinglé dans pollen.yaml EST le lock, le tag en commentaire le rend "
            "lisible, et autoupdate --freeze (ou Renovate) le met à jour."
        ),
    },
    {
        "type": "compare",
        "title": "Et npx skills ?",
        "left": {
            "title": "npx skills (Vercel)",
            "items": [
                "Une CLI + un lockfile",
                "Épingle un ref (tag) + un hash",
                "Node ; déclaratif en expérimental",
                "Très large : skills.sh, 75+ agents",
            ],
        },
        "right": {
            "title": "pollen",
            "items": [
                "Un pollen.yaml déclaratif",
                "Épingle le commit d'une release",
                "Un binaire, neutre côté langage",
                "outdated / autoupdate, validate",
            ],
        },
        "kicker": "Même standard Agent Skills dessous : les deux se composent.",
        "notes": (
            "La question qu'on nous pose le plus. npx skills (Vercel) installe "
            "aussi nos catalogues : repos privés en SSH, GitLab, chemins locaux, "
            "structure par domaines. La différence est dans le modèle. Eux : une "
            "CLI, des add successifs, un skills-lock.json qui retient le ref "
            "(souvent un tag) et un hash du contenu ; le déclaratif existe, en "
            "expérimental, dans le package.json. Nous : un pollen.yaml façon "
            ".pre-commit-config.yaml, à la racine de n'importe quel repo, "
            "Terraform, Python ou Java, sans package.json dans un repo qui n'a "
            "rien à voir avec npm. Chaque source est épinglée sur le commit d'une "
            "release, outdated part du dernier tag, et la montée de version se "
            "relit en PR. Eux sont bien plus larges ; nous, plus stricts pour une "
            "équipe. Les deux installent les mêmes skills : aucun lock-in."
        ),
    },
    {
        "type": "code",
        "title": "Un fichier, trois propriétaires",
        "code": (
            "# ~/.config/pollen/pollen.yaml  →  pollen update -g\n"
            "repos:\n"
            "  - repo: git@github.com:groupbees/skills-core.git     # orga, privé\n"
            "    revision: 351fd495…  # v0.3.1\n"
            "  - repo: git@github.com:groupbees/skills-slides.git   # orga, privé\n"
            "    revision: e4d83514…  # v0.4.0\n"
            "  - repo: https://github.com/groupbees/skills-opensource  # orga, public\n"
            "    revision: 3a461867…  # v0.1.1\n"
            "  - repo: https://github.com/groupbees/pollen           # le skill pollen\n"
            "    revision: c327e7e7…  # v0.5.0\n"
            "  - repo: https://github.com/tosun-si/skills-articles   # perso\n"
            "    revision: cd21b30d…  # v0.1.1"
        ),
        "kicker": "Mes conventions perso ne polluent pas l'équipe : un fichier, cinq commits.",
        "bees": [("bee_happy.png", 11.9, 0.3, 0.95, 10)],
        "notes": (
            "Ma vraie config machine (les paths sont omis). Des modules de "
            "l'orga privés et publics, le skill de pollen lui-même, et un module "
            "perso sur mon compte : les règles d'équipe et les miennes se "
            "composent sans se mélanger. Un module perso vit sur le compte de "
            "celui qui le maintient ; un module d'équipe dans l'orga."
        ),
    },
    {
        "type": "compare",
        "title": "Et Spec Kit, BMAD ?",
        "muted_left": False,
        "left": {
            "title": "Skills de processus",
            "items": [
                "Spec Kit, BMAD : le quoi et le quand",
                "spec · plan · tasks · implement",
                "Un cycle par feature",
                "Nos conventions ? En prose, à injecter",
            ],
        },
        "right": {
            "title": "Skills de conventions",
            "items": [
                "GroupBees : le comment",
                "Archi, Dockerfile, CI, Git, IaC",
                "Actifs sur tout le projet",
                "Une convention = un skill, à la demande",
            ],
        },
        "kicker": "Même format SKILL.md, autre contenu : ils se composent.",
        "bees": [("bee_cool.png", 11.85, 0.3, 1.0, -8)],
        "notes": (
            "Question qu'on nous pose souvent. Spec Kit (GitHub, v1.0) et BMAD "
            "(v6) sont eux-mêmes livrés en Agent Skills : /speckit-specify, "
            "plan, tasks… et les personas BMAD (analyste, PM, architecte, dev). "
            "Ils structurent le processus d'une feature. Nos conventions "
            "techniques, eux les prennent en prose : la constitution.md de Spec "
            "Kit, les persistent_facts de BMAD. Les deux se composent : un "
            "/speckit-plan dans un repo qui a nos skills sort un plan hexagonal, "
            "avec notre Dockerfile et notre CI. Et eux aussi ont leur CLI de "
            "distribution par projet : le problème qu'on résout avec pollen "
            "est le même pour tout le monde."
        ),
    },
    {
        "type": "demo",
        "title": "Même prompt, sans puis avec les skills",
        "steps": [
            "Session vierge : le prompt, la sortie générique",
            "pollen update : les skills du projet arrivent",
            "Même prompt : hexagonal, Dockerfile, tests, CI",
            "Commit squashé, PR labellisée, pipeline jusqu'à Cloud Run",
        ],
        "notes": (
            "Session vierge = terminal gauche : claude --safe-mode "
            "--disable-slash-commands (ni CLAUDE.md, ni skills, même les "
            "built-in). Le moment clé, c'est le contraste. Ce ne sont pas les talents de "
            "l'IA qui font la différence, ce sont les règles. Filets : URL déjà "
            "déployée + screencast."
        ),
    },
    # ── Gouvernance ─────────────────────────────────────────────────────────
    {
        "type": "bullets",
        "title": "Une lib de skills, ça se gouverne",
        "bullets": [
            "Les skills sont du code : versionnés, relus en PR",
            "Blast radius : un skill s'applique à tout ce qui est généré",
            "L'IA drafte les mises à jour, l'humain relit et merge",
            "Capture à chaud : un gotcha rencontré remonte dans le skill",
            "Relecture : référents tech (transverse), référents du domaine (spécialisé)",
        ],
        "kicker": "Sans gouvernance, on recrée le monolithe… éclaté en N fichiers.",
        "bees": [("bee_grad.png", 11.8, 0.2, 1.15, 6)],
        "notes": (
            "Qui relit ? Les skills transverses (Docker, CI, IaC, "
            "commits…) : les référents tech, Guillaume et moi, qui les avons "
            "posés au départ. Un skill spécialisé, comme celui de l'API Solis, "
            "est porté par les référents du domaine : Iliass, chercheur, qui "
            "implémente une bonne partie des features de Solis, avec Youssef, "
            "lead API et produit, et Rafik, entre tech et produit. Des profils "
            "tech, spécialisés sur ce sujet, qui en savent plus que nous : on "
            "relit avec eux. Chez Orange, notre client, même modèle : les "
            "modules transverses sont tenus par les référents tech et l'équipe "
            "platform, les repos spécialisés par le référent de leur domaine. "
            "Toujours une PR, jamais relue par son "
            "seul auteur, et la CI vérifie le mécanique."
        ),
    },
    {
        "type": "bullets",
        "title": "Quand un skill périme",
        "bullets": [
            "Séparer le durable (archi) du volatil (flags, versions)",
            "L'agent se trompe : on corrige le skill, pas que le code",
            "Une règle qui peut devenir un check le devient",
            "Scan IA : bon sur le factuel, le jugement reste humain",
            "Prochaine marche : des evals, pas encore en place",
        ],
        "kicker": "Une règle périmée n'échoue pas : elle enseigne le mauvais pattern.",
        "bees": [("bee_grad.png", 11.8, 0.2, 1.15, -6)],
        "notes": (
            "Le vrai risque d'une lib de skills, c'est la règle périmée : elle ne "
            "casse rien, elle apprend en silence le mauvais pattern à l'agent. "
            "Ce qui pourrit, c'est le volatil : flags, versions, commandes. On "
            "l'isole du durable. War story : un skill Terragrunt référençait "
            "run-all, remplacé par run --all. Péremption factuelle, parfaite "
            "pour un scan IA. La péremption de jugement — est-ce encore notre "
            "convention ? — reste humaine, en revue. Quand une règle est "
            "mécanique, on en fait un check qui casse fort : le hook commit-msg "
            "qui refuse les co-auteurs IA, skill-validator sur chaque skill en "
            "CI. Ce qu'on n'a pas encore : des evals, un prompt de référence "
            "rejoué avec le skill pour prouver qu'il produit toujours le bon "
            "résultat. C'est notre démo avec et sans skills, automatisée. On va "
            "commencer par quelques skills mécaniques, Docker et commits."
        ),
    },
    {
        "type": "code",
        "title": "La CI d'un module de skills",
        "code": (
            "# .github/workflows/ci.yml d'un module : une seule ligne utile\n"
            "jobs:\n"
            "  module:\n"
            "    uses: groupbees/.github/.github/workflows/skills-module.yml@3b24f023…  # v1.1.0\n"
            "\n"
            "# ce que vérifie le workflow partagé, à chaque PR :\n"
            "#   skill-validator --strict   spec, tokens, liens, descriptions\n"
            "#   pollen validate            se déploie comme chez un consommateur\n"
            "#   README généré · noms uniques · shellcheck"
        ),
        "kicker": "Barre de review plus haute que pour du code : ça s'applique à tout.",
        "notes": (
            "skill-validator (agent-ecosystem, open source) : conformité à la "
            "spec, budget de tokens, liens cassés, fichiers orphelins, qualité "
            "des descriptions. La CI vit dans un workflow partagé public, "
            "épinglé par commit ; Dependabot ouvre la PR quand il évolue."
        ),
    },
    {
        "type": "bullets",
        "title": "La doc d'un outil est aussi un skill",
        "bullets": [
            "Chaque module réexpliquait pollen : 13 fichiers par version",
            "Le skill pollen vit dans le repo pollen, versionné avec lui",
            "Installé… par pollen, au niveau projet ou machine",
            "Les modules ne gardent qu'un lien",
            "Même règle pour la CI : un workflow partagé, épinglé",
        ],
        "kicker": "Une source par sujet. Sinon le monolithe revient, en N copies.",
        "bees": [("bee_astro.png", 11.85, 0.2, 1.1, -8)],
        "notes": (
            "War story : à la première montée de version de pollen, il a fallu "
            "retoucher 13 fichiers dans nos modules. C'était exactement le "
            "CLAUDE.md monolithique qu'on dénonce, dupliqué. La connaissance de "
            "l'outil est devenue un skill livré avec l'outil ; les modules n'ont "
            "plus rien à retoucher."
        ),
    },
    {
        "type": "bullets",
        "title": "Comment fait Google ?",
        "bullets": [
            "« Skills are products, not snippets »",
            "Evals obligatoires à la soumission : prompts + grille de score",
            "Evals hebdomadaires sur toute la lib, sur plusieurs agents",
            "Deux axes : précision × efficacité (tokens, temps)",
            "Un owner par skill quand une API change ou qu'une eval régresse",
        ],
        "kicker": "Notre prochaine marche : des evals sur nos skills.",
        "bees": [("bee_cool.png", 11.85, 0.25, 1.0, 8)],
        "notes": (
            "Source : blog Google Cloud « Behind the scenes: how we build, test "
            "and scale Google agent skills » (août 2026). Leur CI : lint, "
            "vérification des liens, checklists assistées par IA, et surtout les "
            "evals. C'est là qu'on n'en est pas encore. Et un owner par skill : "
            "nous, on est huit, pas Google. Pas d'organigramme, mais ceux qui "
            "savent : les référents tech relisent le transverse, les référents "
            "d'un domaine portent ses skills spécialisés, et la CI vérifie le "
            "mécanique. "
            "Adaptez la gouvernance à votre taille, mais gardez-en une."
        ),
    },
    # ── Clôture ─────────────────────────────────────────────────────────────
    {
        "type": "takeaways",
        "title": "À retenir",
        "items": [
            ("Vos conventions, en skills", "Petits, composables, chargés à la demande"),
            ("Déclarés par projet, épinglés", "Un commit par source : le pollen.yaml est le lock"),
            ("Gouvernés comme du code", "Relecture par un pair, CI… et bientôt des evals"),
        ],
        "notes": "Trois idées à ramener lundi matin dans votre équipe.",
    },
    {
        "type": "end",
        "title": "Pas par magie.",
        "mascot": "bee_happy.png",
        "lines": [
            "Parce que les règles sont là.",
            "github.com/groupbees/pollen",
            "Merci ! Des questions ?",
        ],
        "notes": "Merci ! On prend vos questions.",
    },
]

# Repères de scène, en tête des notes : qui parle, les points à ne pas
# oublier, la phrase qui passe le relais. Indexés par titre de slide ; le
# dialogue complet, pour les répétitions, est dans ../dialogue.md.
CUES = {
    "Industrialiser l'IA\nen équipe": (
        "🎤 Mazlum, puis Guillaume\n"
        "• Générer du code avec une IA : trivial. Comme l'équipe l'attend : autre histoire.\n"
        "↪ Guillaume : « Et c'est cette histoire-là qu'on vient vous raconter. »"
    ),
    "Qui sommes-nous ?": (
        "🎤 Chacun présente l'autre\n"
        "• Mazlum présente Guillaume (« m'empêche de mettre en prod le vendredi »)\n"
        "• Guillaume présente Mazlum (« écrit les règles… et les oublie dans son Dockerfile »)\n"
        "↪ Mazlum : « C'est exactement le sujet du talk. »"
    ),
    "En direct du TechCast": (
        "🎤 Les deux, 10 secondes\n"
        "• Clin d'œil, on ne s'attarde pas : on lit le bandeau\n"
        "↪ Mazlum enchaîne sur le contexte GroupBees"
    ),
    "Le contexte : une plateforme d'API": (
        "🎤 Mazlum\n"
        "• Registre d'API : producteurs publient, consommateurs découvrent, IA par-dessus\n"
        "• Stack exigeante : hexagonal, Terragrunt, Workload Identity, IAP\n"
        "↪ « Et derrière, une équipe qui n'a pas le même niveau sur tout ça. Guillaume ? »"
    ),
    "L'équipe": (
        "🎤 Guillaume\n"
        "• 8 personnes : quelques seniors, un junior, un stagiaire\n"
        "• Grâce à Claude, tout le monde fait évoluer les stacks : la bonne nouvelle\n"
        "↪ Mazlum : « La mauvaise, c'est la suite. »"
    ),
    "Le problème : ça diverge": (
        "🎤 Mazlum\n"
        "• Nouveau service, nouvelle stack IaC → nos conventions disparaissent\n"
        "• Chacun son Claude, son CLAUDE.md : l'IA ne connaît pas NOS règles\n"
        "↪ Guillaume : « Donc on a fait ce que tout le monde fait. »"
    ),
    "Première idée : un CLAUDE.md commun": (
        "🎤 Guillaume\n"
        "• Un CLAUDE.md partagé, toutes les règles au même endroit\n"
        "↪ Mazlum : « Simple… pendant deux semaines. »"
    ),
    "Le CLAUDE.md qui grossit": (
        "🎤 Guillaume (montrer le vrai fichier qui scrolle)\n"
        "• Chargé tout le temps : un commit relit les règles Dockerfile\n"
        "• Coûte des tokens, dilue l'attention\n"
        "↪ Mazlum : « Alors on l'a découpé. »"
    ),
    "Du monolithe aux modules : les skills": (
        "🎤 Mazlum\n"
        "• Un skill = un CLAUDE.md modulaire, chargé à la demande\n"
        "• Une convention, un skill"
    ),
    "Anatomie d'un skill": (
        "🎤 Mazlum\n"
        "• Un dossier, un SKILL.md, standard Agent Skills\n"
        "• La description est toujours vue ; le corps, seulement si la tâche correspond\n"
        "↪ Guillaume : « Et un skill, ce n'est pas que du texte. »"
    ),
    "Un skill, c'est un dossier": (
        "🎤 Guillaume\n"
        "• references/ : lu à la demande · assets/ : fichiers à copier · scripts/ : contrôles\n"
        "↪ Mazlum : « Ce qui ne veut pas dire qu'on jette le CLAUDE.md. »"
    ),
    "CLAUDE.md monolithe vs skills": (
        "🎤 Mazlum\n"
        "• CLAUDE.md redevient le contexte durable du projet (AGENTS.md + pont d'une ligne)\n"
        "• Les conventions vivent dans les skills"
    ),
    "Modulariser : des domaines qui se composent": (
        "🎤 Guillaume\n"
        "• Docker générique + Python par-dessus, qui n'ajoute que le spécifique\n"
        "↪ Mazlum : « Restait à les partager dans l'équipe. »"
    ),
    "Partager : un catalogue synchronisé en global": (
        "🎤 Guillaume\n"
        "• Un repo git de skills, synchronisé sur la machine de chaque dev"
    ),
    "Un module de skills, synchronisé en global": (
        "🎤 Guillaume\n"
        "• Script → dossiers perso des agents ; plusieurs modules ; version = tag git\n"
        "↪ Mazlum : « … jusqu'à ce que je l'utilise chez un client. »"
    ),
    "Global : la limite": (
        "🎤 Mazlum\n"
        "• En global, nos règles s'appliquent partout : perso, clients\n"
        "• On veut choisir, projet par projet\n"
        "↪ Guillaume : « Et choisir des skills par projet, c'est gérer des dépendances. »"
    ),
    "Par projet : un gestionnaire de skills": (
        "🎤 Guillaume\n"
        "• On importe les skills comme des dépendances, + les skills du projet\n"
        "• La factory accueillera d'autres projets que Solis\n"
        "↪ Mazlum : « À une condition : ne rien inventer de propriétaire. »"
    ),
    "S'appuyer sur les standards": (
        "🎤 Mazlum\n"
        "• Agent Skills : Claude Code, Copilot, Cursor, Codex, Antigravity CLI\n"
        "• AGENTS.md pour le contexte ; on change d'agent, les skills restent\n"
        "↪ « Il manquait l'outil pour les installer. Guillaume, raconte-leur pollen. »"
    ),
    "pollen : les skills comme des dépendances": (
        "🎤 Guillaume\n"
        "• CLI open source en Rust, pollen.yaml façon pre-commit\n"
        "• update : installe, rafraîchit, supprime ce qu'on a retiré"
    ),
    "pollen, en pratique": (
        "🎤 Guillaume\n"
        "• Périmètre étroit : déplace des dossiers, valide la spec\n"
        "• Un skill écrit à la main n'est jamais écrasé\n"
        "↪ Mazlum : « Et la question à chaque fois : où est le lockfile ? »"
    ),
    "Épingler un commit… et pas de lockfile": (
        "🎤 Guillaume\n"
        "• Pas de résolveur → pas de lockfile : le SHA épinglé EST le lock\n"
        "• outdated → autoupdate → PR\n"
        "↪ Mazlum : « Et l'autre question, sous mon post LinkedIn : pourquoi pas npx skills ? »"
    ),
    "Et npx skills ?": (
        "🎤 Mazlum, puis Guillaume, Mazlum conclut\n"
        "• Mazlum : super outil, bien plus large, sait installer nos catalogues privés\n"
        "• Guillaume : avant pollen, seul outil open source trouvé, on l'a regardé\n"
        "• Guillaume : CLI + lock vs fichier déclaratif, sans package.json, épinglé sur une release\n"
        "• Mazlum : les deux installent les mêmes skills, aucun lock-in"
    ),
    "Un fichier, trois propriétaires": (
        "🎤 Mazlum\n"
        "• Ma vraie config : modules de l'orga (privés + publics), skill pollen, module perso\n"
        "• Les règles de l'équipe et les miennes se composent sans se mélanger\n"
        "↪ Guillaume : « Et on nous demande aussi : vous réinventez Spec Kit ? »"
    ),
    "Et Spec Kit, BMAD ?": (
        "🎤 Guillaume\n"
        "• Eux aussi en Agent Skills, mais ils encodent un processus (spec → plan → tâches)\n"
        "• Nous, des conventions techniques : ils se composent\n"
        "↪ Mazlum : « Assez parlé. Montrons-le. »"
    ),
    "Même prompt, sans puis avec les skills": (
        "🎤 Démo, on alterne (script-demo.md) · le non-pilote décide de basculer sur les filets\n"
        "0 · Cadrage : Mazlum parle\n"
        "1 · SANS : Mazlum pilote, Guillaume commente (1 stage root, citation sans auteur)\n"
        "2 · pollen update : Guillaume pilote, Mazlum commente (quote-domain)\n"
        "3 · AVEC : Guillaume pilote, Mazlum commente (3 couches, non-root, ?lang=fr)\n"
        "4 · Delta : ping-pong, une paire chacun → « Les règles sont là. »\n"
        "5 · Déploiement : Guillaume pilote, Mazlum commente\n"
        "↪ Guillaume : « Une bibliothèque de skills, ça se gouverne. »"
    ),
    "Une lib de skills, ça se gouverne": (
        "🎤 Mazlum\n"
        "• Skills = code : versionnés, relus en PR, blast radius énorme\n"
        "• Transverses : Guillaume et moi · Domaine : ceux qui le connaissent · « On est huit, pas Google »\n"
        "↪ Guillaume : « Et même relu, un skill finit par vieillir. »"
    ),
    "Quand un skill périme": (
        "🎤 Guillaume, Mazlum, Guillaume\n"
        "• Une règle périmée n'échoue pas : elle apprend le mauvais pattern (run-all → run --all)\n"
        "• Mazlum : le factuel, un agent le repère ; « encore notre convention ? » reste humain\n"
        "• Guillaume : une règle qui peut devenir un check en devient un"
    ),
    "La CI d'un module de skills": (
        "🎤 Guillaume\n"
        "• skill-validator : spec, liens, orphelins, taille\n"
        "• Workflow partagé épinglé par SHA, Dependabot\n"
        "↪ Mazlum : « Et on a appris une chose en route. »"
    ),
    "La doc d'un outil est aussi un skill": (
        "🎤 Mazlum\n"
        "• 1re montée de version de pollen : 13 fichiers à retoucher\n"
        "• Désormais, la connaissance de pollen est un skill livré avec pollen\n"
        "↪ Guillaume : « Et pour aller plus loin, on a regardé chez les gros. »"
    ),
    "Comment fait Google ?": (
        "🎤 Mazlum\n"
        "• « Skills are products, not snippets » ; evals obligatoires et hebdo, multi-agents\n"
        "• Notre prochaine marche : les evals\n"
        "• Adaptez la gouvernance à votre taille, mais gardez-en une"
    ),
    "À retenir": (
        "🎤 Un point chacun\n"
        "• Mazlum : conventions dans des skills, pas un CLAUDE.md géant\n"
        "• Guillaume : skills par projet, épinglés comme des dépendances\n"
        "• Mazlum : gouvernés comme du code · Guillaume : « relecture, CI… et bientôt des evals »"
    ),
    "Pas par magie.": (
        "🎤 Les deux\n"
        "• Mazlum : « Ce n'est pas par magie que l'IA a codé comme nous. »\n"
        "• Guillaume : « C'est parce que les règles sont là. »\n"
        "• Mazlum : « Merci ! On prend vos questions. »"
    ),
}
