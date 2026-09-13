# Le Comptoir des Artisans

Dépôt des ressources officielles du serveur Minecraft 26.2 et de son espace Discord.

## Contenu

- `Taverne_Ranks_MCModels_32_Badges_v7_OPAC_FR.zip` : pack complet v6 enrichi de tous les textes traduisibles OPAC 0.31.6 (614 clés, 93 infobulles), prêt pour la distribution au prochain démarrage du serveur.
- `Taverne_Ranks_MCModels_32_Badges_v6.zip` : version précédente, conservée pour le retour arrière.
- `Taverne_Ranks_MCModels_32_Badges_v3.zip` : ancienne version de grades et badges. Il intègre les guides d’interface Redstone Tweaks 2.5.5 avec des caractères d’espacement remappés afin d’éviter toute collision avec les badges de grades.
- `Taverne_Ranks_MCModels_32_Badges_v2.zip` : version intermédiaire qui réactive les guides clients, mais provoque une collision visuelle entre les caractères d’espacement de Redstone Tweaks et certains badges.
- `Taverne_Ranks_MCModels_32_Badges_v1.zip` : ancienne version qui masque les guides de conteneurs de packs clients.
- `deploy-transfer/discord-mcp-v1.5.0.tar.xz.b64` : dernière archive du plugin d’administration Discord ; elle ajoute l’outil sécurisé `discord_add_reaction` et la lecture des réactions.
- `deploy-transfer/discord-mcp-v1.4.0.tar.xz.b64` : archive précédente, conservée pour le retour arrière.
- `branding/logo-principal.png` : logo principal haute définition du Comptoir.
- `branding/discord-icon.png` : variante 512 × 512 utilisée pour le serveur et le bot Discord.
- `branding/minecraft-icon.png` : variante simplifiée 64 × 64, optimisée pour la liste des serveurs Minecraft.

## Identité visuelle

Le logo adopte un médaillon de taverne avec le monogramme `LC` : pierre claire pour le `L`, bois ambré pour le `C`, fond en bois sombre et touche de lierre. La variante Minecraft réduit volontairement les textures et les petits reliefs afin de rester lisible à 64 × 64 pixels.

## Déploiement du pack

La version 3 conserve les véritables glyphes de grades sur `U+F801` à `U+F820` et remappe les caractères d’espacement des interfaces sur `U+E9xx`. Les recettes de l’alambic et les tableaux des conteneurs restent visibles sans afficher de badges parasites.

SHA-1 de `Taverne_Ranks_MCModels_32_Badges_v3.zip` :

```text
a4340398d3cee51396b5e8c2149cf72ac49081cd
```

Les éléments d’interface intégrés proviennent de Redstone Tweaks 2.5.5 par RexxStone, sous licence CC BY-NC-SA 4.0. L’attribution est également incluse dans l’archive.

L’archive `1.5.0` possède l’empreinte SHA-256 suivante avant encodage base64 :

```text
45e8aa6c520412492c450dc968623de36af87f1f4a93cfb213a1e12f851c0312
```

Aucun identifiant, mot de passe ou jeton n’est stocké dans ce dépôt.


## Traduction OPAC — 13 septembre 2026

La version 7 complète la traduction des menus, des messages et des infobulles d’OPAC 0.31.6 pour Minecraft 26.2. Les 82 entrées non concernées du pack v6 restent identiques à l’octet près. « Zone sauvage » reste en vert foncé. Les permissions et les protections du serveur ne sont pas modifiées.

SHA-1 : `b4c06262c266e7e6624091e19f110d1a497acba9` ; SHA-256 : `2c38d489cc87f3e25d7e6121600c1b1d63025f6143b480184d141d584e125d78` ; 131827 octets.

Les identifiants transmis littéralement par OPAC (par exemple `main`, `base`, `Chests`, `Villagers`) restent inchangés : le pack traduit les textes traduisibles et leurs explications, pas ces identifiants.

[Notice](opac-fr-0.31.6/README.md), [traduction](opac-fr-0.31.6/fr_fr.json), [contrôles](opac-fr-0.31.6/validation.json). Chargement des métadonnées et des 615 entrées (614 clés OPAC + alias historique Wilderness) validé avec les classes Minecraft 26.2. Rendu visuel en jeu à confirmer.

Reconstruction : Python 3, depuis `opac-fr-0.31.6`, exécuter `python3 translate.py`. Le script lit le pack v6 à la racine du dépôt et les textes anglais archivés, vérifie la couverture et conserve les autres ressources. La sortie reconstruite se trouve dans ce sous-dossier.
