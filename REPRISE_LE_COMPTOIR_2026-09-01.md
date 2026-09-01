# Reprise — Le Comptoir des Artisans — 1er septembre 2026

Ce document conserve l’état final vérifié après la mise à jour de l’identité visuelle et des messages Minecraft.

## État opérationnel vérifié

- Serveur Minecraft MineStrator : `454706`
- Version Minecraft : `26.2`
- État au dernier contrôle : en ligne
- Joueurs connectés au dernier contrôle : `0/50`
- Mode maintenance : activé
- Aucun redémarrage du VPS n’a été effectué.
- Aucun redémarrage Minecraft n’a été effectué pendant les modifications de MOTD.

## MOTD Minecraft validé

Message normal enregistré dans `/server.properties` :

```properties
motd=§6⚒ Le Comptoir des Artisans §8— §aVotre histoire façonne ce monde §2🌿
```

Rendu attendu :

> ⚒ Le Comptoir des Artisans — Votre histoire façonne ce monde 🌿

Message de maintenance actif dans `/config/mmode.json` :

```json
"enabled": true,
"motd": "§6⚒ Le Comptoir des Artisans §7- §cMaintenance ⛔"
```

Rendu vérifié :

> ⚒ Le Comptoir des Artisans - Maintenance ⛔

Le mod utilisé est `MaintenanceMode-Universal-1.3.4.jar`. La configuration peut être rechargée à chaud avec la commande console `maintenance reload`. L’état interne se vérifie avec `maintenance status`.

## Identité visuelle appliquée

- Icône du serveur Discord : mise à jour et vérifiée.
- Avatar du bot Discord : mis à jour et vérifié.
- Icône Minecraft : variante simplifiée avec verdure, installée et vérifiée.
- Empreinte SHA-256 de l’icône Minecraft 64 × 64 :
  `29c5c14a5b8be3b51446d184a3ce92e3110717a9ad3a8dd2332513f0359c66c1`
- Les fichiers sources sont conservés dans le dossier `branding/` de ce dépôt.

## Liste blanche

Joueurs ajoutés et vérifiés :

- `Melt1s`
- `FuraxJumper`
- `Shadow_Zz`

Aucune permission opérateur n’a été modifiée.

## Pack de ressources

Le fichier `Taverne_Ranks_MCModels_32_Badges_v1.zip` n’a pas été modifié par cette mise à jour. Le SHA-1 configuré reste :

```text
4ab4083338b2406a34247cd2220d8d50b774cfa7
```

## Sécurité pour la prochaine reprise

- Ne pas désactiver la maintenance sans confirmation explicite de l’utilisateur.
- Ne pas redémarrer Minecraft sans confirmation explicite juste avant l’action.
- Ne pas redémarrer le VPS sans confirmation explicite juste avant l’action.
- Ne jamais enregistrer de mot de passe, jeton, clé ou identifiant sensible dans GitHub.
- Vérifier l’état en ligne et le nombre de joueurs avant toute intervention.
