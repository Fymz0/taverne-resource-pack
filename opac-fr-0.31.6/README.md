# Le Comptoir des Artisans — OPAC en français

Pack complet de grades et badges du serveur, enrichi de la traduction française
de tous les textes traduisibles d’**Open Parties and Claims 0.31.6**, pour
**Minecraft Java 26.2**, format de ressources **88**.

## Traduction

- 614 clés OPAC couvertes : menus, boutons, confirmations, messages et permissions.
- Infobulles des réglages rédigées en français ; aucune valeur technique
  `default` ne provoque le retour aux explications anglaises du mod.
- « Sous-profil » pour Sub-Config ; « Listes d’accès » pour Player Groups.
- « OUI / NON » pour ON / OFF ; « Hérité » pour la valeur héritée du parent.
- Un réglage grisé n’est pas modifiable dans ce menu : la traduction ne le déverrouille pas.
- Les commandes, droits et protections ne sont pas modifiés.
- La couleur vert foncé de « Zone sauvage », les grades, badges, glyphes et
  autres ressources du pack v6 sont conservés.

OPAC reçoit les noms personnalisés et les identifiants de catégories comme
des chaînes littérales. Ils restent donc inchangés : `main`, `base`,
`Villagers`, `Chests`, etc. Les textes et explications autour de ces noms sont
traduits. Un pack de ressources ne peut pas renommer ces identifiants dans
le menu. Les chemins de blocs et d’entités dans les informations techniques
restent également des identifiants Minecraft.

## Distribution par le serveur

Le ZIP contient le pack serveur complet, avec la traduction OPAC. Le serveur
peut le transmettre à la connexion avec ses propriétés `resource-pack` et
`resource-pack-sha1`. Aucun nouveau mod client n’est nécessaire pour la
traduction ; le joueur doit déjà disposer d’OPAC pour utiliser ses menus.

Le pack est obligatoire sur Le Comptoir. Un joueur qui a déjà accepté les
packs du serveur reçoit la nouvelle version à la connexion après activation.
Sinon, il doit accepter la demande proposée par Minecraft.

Les fichiers `fr_fr.json` et `en_us.json` contiennent la même traduction OPAC,
comme dans le pack serveur précédent. Cela fournit aussi le français comme
langue de repli, sans changer les textes des autres mods.

Pour un essai local avant activation : déposer le ZIP dans `resourcepacks`
de l’instance puis l’activer dans Options > Packs de ressources. Le pack du
serveur peut avoir priorité sur certaines traductions tant qu’il utilise
encore la version précédente.

## Contrôles

Toutes les clés OPAC et leurs paramètres de formatage sont vérifiés. Les
fichiers JSON sont valides ; le CRC du ZIP et la conservation à l’octet près
des ressources non concernées ont été contrôlés. Le rendu visuel sur un
client connecté doit encore être confirmé en jeu.

## Sources et attributions

- Open Parties and Claims, Xaero96 et contributeurs :
  https://github.com/thexaero/open-parties-and-claims — LGPL-3.0-only.
- Traduction française complétée pour Le Comptoir des Artisans à partir des
  textes de la version 0.31.6 et de la traduction partielle du pack v6.
  Les adaptations des textes OPAC sont proposées sous LGPL-3.0-only.
- Pack source : `Taverne_Ranks_MCModels_32_Badges_v6.zip`, SHA-1
  `49763d6b06fbbd1d5e23f80604c3ece3ef3acea1`.
- Les attributions et licences des grades, badges et ressources Redstone
  Tweaks présentes dans le pack original restent applicables et conservées.
