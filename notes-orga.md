# Notes pour l'orga + elevator pitch

## Elevator pitch (~85 mots)

> Chez GroupBees, chaque dev avait son `CLAUDE.md` perso — illisible à plusieurs,
> impartageable, et chargé à chaque session : lourd en tokens à l'échelle. Les
> **skills** ont tout changé : nos conventions (archi, Dockerfile, CI/CD, tests)
> sont devenues des modules **activés à la demande**, partagés en équipe — *une
> vraie usine de dev*, à condition de les gouverner comme du code. Je raconte
> comment on l'a fait, ce que ça coûte en rigueur, et comment vous pouvez le
> rejouer — Claude Code, Cursor, Copilot.

---

## Notes pour l'orga

**Format** — 35 min + 5–10 min Q&A. Variantes 30 / 40 min disponibles.

**Audience & niveau** — dev / lead / tech lead. Familiarité Docker / CI/CD /
archi backend attendue. **Aucune** expérience Claude Code requise : la méthodo
est transposable.

**Ce que le public emporte**
- Une méthodologie concrète pour encoder les conventions d'équipe en modules IA
  — applicable à Claude Code, Cursor, Copilot.
- Le **process de gouvernance** qui rend ça durable (versioning, review,
  péremption, owners) — la part que la plupart des talks IA cachent.
- Des artefacts concrets transposables (Dockerfile multi-stage, archi hexa, CI,
  PR) vus en démo.

**Angle différenciant** — les talks « IA pour devs » saturent l'upside. Le vrai
sujet — *industrialiser à l'échelle équipe avec rigueur* — est sous-couvert.
Retour d'XP terrain (GroupBees) avec ses cicatrices, pas une démo cosmétique.

**Ce que le talk ose montrer (et que peu osent)**
- **Blast radius** : un skill mal écrit s'applique à *tout* ce qui sera généré,
  par toute l'équipe — la barre de review doit être plus haute que pour du code
  normal.
- L'IA tend à **sur-généraliser** un fix one-shot en règle universelle — sans
  humain dans la boucle, les skills dérivent.
- **Péremption** : flags / versions / commandes pourrissent vite — un skill
  faux est pire que pas de skill.
- Sans **owners**, la « maintenance continue » = personne ne maintient.

**Démo live — risque assumé, filets en place**
- App cible minuscule, stateless, sans secret.
- Déploiement via **GitHub Actions** — réseau GitHub, pas le laptop sur le wifi
  de conf.
- Deux filets ultimes : **URL déjà déployée** + **screencast complet** de la
  démo en happy path.
- Le message tient même si la démo plante.

**Pré-requis salle**
- Vidéoprojecteur avec bon contraste (lecture de terminal).
- Deux prises secteur (laptop + hotspot 4G/5G personnel).
- **Aucune dépendance** au wifi de conférence.

**Bio speaker** — _[à remplir]_
