# Correctif du sélecteur de tchat — 17 octobre 2026

**Version préparée : client 1.2.1 + pack commun v16. Non activée à la rédaction.**

Le pack v15 avait ajouté ses glyphes dans la police par défaut avec 2553 séquences affectées à U+F0000 et suivants. Le pack client `Icons v.1.14.zip` utilise cette même plage pour les menus. L'audit des polices des packs et des JARs du profil reproduit **443 collisions**, ce qui explique les drapeaux et les chiffres dans le menu pause signalés par le propriétaire. V15 et le client 1.2.0 doivent être considérés comme défectueux ; ne pas installer le 1.2.0 resté en staging.

V16 reconstruit depuis le dernier pack stable v14. Les **3953 nouveaux émojis**, même les émojis Unicode simples, utilisent exclusivement **U+104000 à U+104F70**, une plage contrôlée sans collision avec les **1632 glyphes** des packs et mods clients inspectés ni les polices du pack v14. Les nouveaux fournisseurs n'ajoutent donc aucun remplacement de caractère Unicode standard ou de glyphes déjà employés par les menus. Les 577 anciennes entrées autres que la police d'assemblage et la description du pack sont identiques octet par octet ; aucune traduction ni image de menu n'est ajoutée ou modifiée.

Le complément 1.2.1 conserve un seul point d'entrée : **un bouton immédiatement à gauche du check No Chat Reports dans le tchat**. Le panneau unique défile à droite des messages ; neuf catégories, recherche française sans accents, variantes, noms au survol et insertion au curseur. Les 150 icônes Iconic précédentes restent accessibles. Les prévisualisations utilisent explicitement `lecomptoir:chat_emojis`. Fontes et textures nécessaires sont incluses dans le complément ; le bouton n'attend plus la présence d'un fichier du pack serveur pour apparaître. Aucune injection ne cible le menu pause.

Le pack commun v16 permet aussi aux autres joueurs qui l'acceptent de voir les nouveaux glyphes dans les messages ; le complément client est nécessaire pour avoir le bouton de sélection. Le pack seul ne crée pas une interface client. Les glyphes privés nécessitent le pack ou le complément pour être affichés ; copier le message dans une application externe n'exporte pas une séquence Unicode standard.

## Vérifications

- 8227 contrôles de ressources : archives, JSON, 3953 cases d'atlas dans chaque livrable.
- 4907 contrôles natifs dans Minecraft 26.2 avec Fabric et No Chat Reports 2.20.2 : transformations, catégories, recherche et disposition à six résolutions ; création effective du bouton sans gestionnaire de ressources serveur, position à gauche du check ; action du bouton, clic de grille et insertion au curseur, molette, clic de catégorie, focus de recherche, saisie et Entrée sans envoi.
- Régression reproduite : 443 collisions v15, zéro v16 ; 150 prévisualisations Iconic autonomes, aucune injection pause et aucun ajout de traduction.
- Le test natif fonctionne sans fenêtre et utilise une police de test. **Le rendu réel, la présence du bouton dans la session du propriétaire et l'envoi reçu par un second joueur restent à vérifier après activation.**

## Reconstruction

Dans le dépôt d'administration, conserver les dossiers frères `chat-emoji-client-20261015`, `chat-emoji-expressions-20261016` et `chat-emoji-categories-20261017`. Exécuter `fetch_sources.py`, puis `build.py`, `regression_test.py`, `native_test.py`. Java 25, JAR client Minecraft 26.2, Fabric Loader 0.19.5 et dépendances sont configurables via `EMOJI_CLIENT_DEPS`. Le test utilise Fabric API 0.161.0+26.2 et NCR 2.20.2, répertoire configurable via `EMOJI_CLIENT_INPUTS`.

`build.json` décrit les empreintes des livrables ; `client-font-codepoints.json` contient uniquement l'inventaire des codes de glyphes du client. Visuels Twemoji 17.0.3 (CC BY 4.0), données françaises Emojibase 17.0.0 (MIT/Unicode), catégories demandées d'après Emojipedia. Licences et attribution incluses.

## Activation

Ne pas réutiliser l'ancien installateur 1.2.0. Le nouveau script prépare/vérifie le JAR, puis refuse tout remplacement pendant que ce profil Minecraft est ouvert. Une fois le profil fermé, il archive l'ancien 1.1.0, installe uniquement 1.2.1 et vérifie l'intégrité et la conservation des autres JARs. Aucun arrêt forcé du client.

Les propriétés serveur seront préparées pour v16. **Aucun nouveau redémarrage serveur n'est autorisé** : l'accord du 17 octobre 21:22:15 a déjà été consommé par l'activation v15. Un nouvel accord explicite est nécessaire, avec sauvegarde ciblée, annonce, décompte, `save-all flush`, arrêt/start unique et vérification du démarrage habituel. Le résultat de préparation doit être distingué de l'état réellement chargé.
