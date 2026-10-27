# Verrouiller la démo — checklist

**Principe :** une démo « live » est une **performance répétée, pas une
expérience**. Verrouiller = supprimer chaque source de non-déterminisme qu'on
peut, et avoir un filet pour chacune qu'on ne peut pas. La démo **sert** le
message ; elle n'EST pas le message — si elle plante, le talk tient sur les
slides + le contraste capturé.

## 1. Figer le scénario (zéro impro)
- [ ] App de démo définie : petit service Python hexagonal, `GET /quote` + `GET /health`, **stateless, pas de DB, pas de secret**. **Pas de déploiement en live.**
- [ ] Le **prompt exact** est dans `prompts.md`, **copié-collé** (jamais tapé à la main → zéro faute, zéro variabilité).
- [ ] **Même prompt** pour SANS et AVEC (c'est l'essence du contraste).
- [ ] Sortie attendue connue par cœur (pour commenter même si l'écran rame).

## 2. Tout pré-chauffer (le live est incrémental, pas à froid)
- [ ] `skills-demo` sur `main`, propre, `.claude/skills` vide (reset dans `script-demo.md`).
- [ ] `pollen update` déjà joué une fois sur le réseau de la salle (accès SSH à skills-core).
- [ ] Onglet ouvert sur la **release vitrine** (repo existant : tag, PR labellisées, notes classées).
- [ ] Skills à jour + testés ; `~/.claude` dans l'état voulu.

## 3. Rendre le CONTRASTE déterministe (le climax)
- [ ] Onglet/term « SANS » prêt : `claude --safe-mode --disable-slash-commands` dans un dossier vierge.
- [ ] Onglet/term « AVEC » prêt : `claude` dans le dossier projet.
- [ ] Les **deux sorties déjà capturées** en répét' (fichiers ouverts) → bascule immédiate si la génération live traîne.
- [ ] Vue **côte à côte** prête (split screen / 2 Dockerfile) pour montrer le delta visuellement.

## 4. Un filet pour CHAQUE moment live (cascade)
- [ ] Génération KO → artefacts pré-générés sous la main.
- [ ] Réseau KO → **screencast complet** (happy path, enregistré en répét').
- [ ] Claude Code / API KO → screencast.
- [ ] Règle : pour chaque moment live, savoir répondre « et si ça plante ? » en **< 5 s**.

## 5. Durcir l'environnement
- [ ] **Hotspot 4G/5G perso** en réseau primaire ou backup (**jamais** le wifi de conf seul). Testé **sur place**.
- [ ] Notifications coupées (Slack, mail, MAJ système), Do Not Disturb.
- [ ] Terminal **grande police** + thème lisible au vidéoproj ; résolution testée.
- [ ] Versions **figées** (Claude Code, pollen) — aucune MAJ la veille.
- [ ] Alim branchée ; adaptateurs vidéo testés.

## 6. Répéter (le vrai verrou)
- [ ] Démo complète end-to-end répétée **≥ 3 fois**.
- [ ] ≥ 1 run **« à froid »** (machine / dossier frais) → révèle les dépendances cachées.
- [ ] Répété sur la **vraie machine** + écran/résolution de présentation.
- [ ] **Chronométré** (tenir dans ~10 min ; AVEC génère en ~3 min, SANS en ~80 s).
- [ ] **Répéter une panne** : forcer un échec et s'entraîner à basculer sur le filet **sans stress**.

## 7. Script de reset (idempotent)
- [ ] `reset-demo.sh` qui remet tout à l'état initial (supprime le dossier généré, recrée le dossier « sans » vierge, repo de démo propre) → pour re-répéter / re-jouer instantanément.

## 8. Plan B narratif
- [ ] Slides avec **captures des artefacts** (Dockerfile, hexa, tests, AGENTS.md, diff du contraste) → raconter la démo sur slides si tout plante.
- [ ] Le message passe même sans démo live.

---

### Les 3 verrous qui comptent le plus
1. **Les sorties pré-capturées + le screencast** = tes deux filets ultimes. Avec eux, la démo ne peut jamais « échouer » visiblement.
2. **Hotspot perso**, jamais le wifi de conf (la cause n°1 d'échec de démo live).
3. **Répéter une panne**, pas seulement le happy path — c'est ce qui te rend serein sur scène.
