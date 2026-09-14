# BACAP 1.21 — français dans le pack serveur v8

Pack complet pour Le Comptoir des Artisans, Minecraft Java 26.2 (ressources 88).

- 3 616 entrées BACAP dans fr_fr et en_us (repli français), dont les 3 614 clés utiles du modèle de traduction fourni.
- Quatre clés absentes complétées : Ahoy!, exemple des équipes, Item Rewards:, Potions Milestone. Valeur vide The Stink Bomb corrigée.
- Six clés dupliquées normalisées en conservant leur dernière valeur ; commentaires de ligne retirés, JSON strict.
- Les références culturelles et noms propres de la traduction officielle sont conservés. Ce contrôle ne constitue pas une révision linguistique exhaustive.
- Les 83 entrées du ZIP v7 hors pack.mcmeta et fichiers minecraft/lang sont conservées à l’octet près, notamment OPAC, grades et badges. Les anciennes valeurs minecraft/lang sont également identiques.
- Aucun changement aux identifiants de progrès, récompenses, permissions ou protections.

## Fichier

`Taverne_Ranks_MCModels_32_Badges_v8_OPAC_BACAP_FR.zip` à la racine : 333 267 octets.

SHA-1 : `c2520ca7994cd30be1be83ca50b0f3f77f5b7d6f`.
SHA-256 : `89dee901c899be9f7f0fd5f115e3d58541fb4f6d6f3a6f331a711f9f60e525ac`.

## Source et crédits

Datapack BlazeandCave's Advancements Pack, Cavinator1 : https://modrinth.com/datapack/blazeandcaves-advancements-pack .

BACAP Language Pack 1.21 officiel, ZIP fourni par l’utilisateur : https://modrinth.com/resourcepack/bacap-language-pack . SHA-256 : `63b82a4251cac526f9677480f3ba14a1f93fab89206c29004fe63adfb44ca864`.

Traduction française par Personnedu59, contributions de Zangdarss, Chucky2401 et TaeliaDideaux selon l’en-tête du fichier. Les droits des sources et les licences/attributions du pack v7 restent applicables ; les adaptations du Comptoir ne sont pas une version officielle BACAP. Crédits également inclus dans le ZIP.

## Reconstruction et validation

Python 3, sans dépendance : `python build_bacap.py ../Taverne_Ranks_MCModels_32_Badges_v7_OPAC_FR.zip "BACAP Language Pack 1.21.zip" sortie`.

Le ZIP source officiel est à fournir séparément. Le script vérifie les deux empreintes source, la couverture du modèle fourni, l’absence de traductions vides, les paramètres %s, les collisions, tous les JSON, le CRC ZIP et les ressources conservées. `fr_fr.json` conserve la traduction intégrée ; `validation.json` consigne les résultats.

Format 88 conservé depuis le pack v7 validé sous 26.2. Aucun nouveau test des classes Minecraft ni rendu graphique n’a été exécuté pour v8. La couverture est mesurée sur le modèle de traduction fourni, pas sur chaque référence du datapack en fonctionnement. Chargement côté client et lisibilité en jeu restent à confirmer.
