"""Build the French OPAC resource pack from the exact production artifacts."""
from pathlib import Path
import json
import zipfile
import hashlib
import re
import copy

ROOT = Path(__file__).resolve().parent
SOURCE = json.loads((ROOT / 'en_us.source.json').read_text())
KEYS = list(SOURCE)
BASE_PATH = ROOT / 'server-original-v6.zip'
if not BASE_PATH.exists():
    BASE_PATH = ROOT.parent / 'Taverne_Ranks_MCModels_32_Badges_v6.zip'
BASE = zipfile.ZipFile(BASE_PATH)
FR = json.loads(BASE.read('assets/openpartiesandclaims/lang/fr_fr.json'))

def lines(start, text):
    for index, value in enumerate(text.strip('\n').split('\n'), start):
        FR[KEYS[index]] = value.replace('\\n', '\n')

def set_option(path, label, tooltip):
    FR['gui.xaero_pac_player_config_playerConfig.' + path] = label
    FR['gui.xaero_pac_player_config_tooltip_playerConfig.' + path] = tooltip

lines(58, r'''
Le joueur ciblé est invalide !
Mode modérateur des claims activé ! Les claims de groupe affichent le nom de leur propriétaire au lieu du nom du groupe.
Mode modérateur des claims désactivé !
Mode administrateur des claims activé ! Tu disposes des fonctions de modération et d'un accès complet à tous les claims, sans les limitations habituelles.
Mode administrateur des claims désactivé !
Mode claims du serveur activé !
Mode claims du serveur désactivé ! Retour au mode de claim par défaut.
Mode claims de groupe activé !
Mode claims de groupe désactivé ! Retour au mode de claim par défaut.
Mode claims personnels activé ! Tu réserves les terrains en ton nom.
Mode claims personnels désactivé ! Retour au mode de claim par défaut.
Mode de claim par défaut activé ! Le mode personnel ou de groupe sera choisi automatiquement lors du claim.
Mode visiteur activé ! Tu vois tes claims et y accèdes comme un joueur non allié.
Mode visiteur désactivé !
Les chunks ont été claim avec succès !
Les claims ont été retirés avec succès !
Chunk claim en (%1$s, %2$s) dans %3$s !
Claim retiré en (%1$s, %2$s) dans %3$s !
Les chunks ciblés sont trop éloignés ! Le mode administrateur ou le mot « anyway » à la fin de la commande est nécessaire.
Tu ne peux pas claim dans une autre dimension ! Le mode administrateur ou le mot « anyway » à la fin de la commande est nécessaire.
Un remplacement de claims est encore en cours !
Les chunks ciblés sont déjà claim !
Ce chunk appartient déjà à %1$s !
Tu as atteint ta limite de claims !
Tu dépasses ta limite de claims : tu peux seulement en retirer !
Les claims sont désactivés dans cette dimension par les réglages du serveur !
Les réglages de la zone sauvage interdisent ce claim ! Un autre mode de claim peut fonctionner.
Tu ne peux pas retirer un claim appartenant à un autre propriétaire que celui de ton mode de claim actuel !
Ce chunk n'est pas claim : il n'y a rien à retirer !
Trop de chunks pour une seule action !
Le système de claims est désactivé !
Tu n'as pas l'autorisation de créer des claims du serveur !
Tu n'as pas l'autorisation de claim au nom de ton groupe !
Tu essaies d'agir au nom d'un groupe alors que tu n'en as pas !
Un seul joueur peut être ciblé !
Le joueur ciblé est invalide !
Le sous-profil utilisé pour le mode de claim « %2$s » est « %1$s ».
Un seul joueur peut être ciblé !
Le joueur ciblé est invalide !
Ce sous-profil n'existe pas !
L'identifiant du sous-profil est invalide !
Les prochains claims du mode « %2$s » utiliseront le sous-profil « %1$s ».
Chunks marqués pour le chargement forcé !
Marquage de chargement forcé retiré !
Chunk marqué pour le chargement forcé en (%1$s, %2$s) dans %3$s !
Marquage de chargement forcé retiré en (%1$s, %2$s) dans %3$s !
Tu as atteint ta limite de chunks à chargement forcé !
Tu dois d'abord claim les chunks ciblés !
Ces chunks sont déjà marqués pour le chargement forcé !
Ces chunks ne sont pas marqués pour le chargement forcé !
Tous les claims correspondants ont été remplacés !
Le nouvel état des claims correspond déjà au critère de remplacement !
Option verrouillée : seuls les opérateurs du serveur peuvent la régler pour toi !
(%1$s) L'option %2$s a été réglée sur %3$s.
Le serveur impose la valeur %1$s.
Clé d'option invalide !
Un seul joueur peut être ciblé !
Le joueur ciblé est invalide !
Le format de la valeur est invalide !
La valeur saisie est invalide !
Identifiant de sous-profil invalide !
Cette option n'est pas autorisée dans cette configuration !
Hérité
Configuration de joueur invalide ! Une erreur est survenue. Signale-la à Xaero.
Clé d'option invalide !
Un seul joueur peut être ciblé !
Le joueur ciblé est invalide !
Identifiant de sous-profil invalide !
Cette option n'est pas autorisée dans cette configuration !
(%1$s) %2$s = %3$s
Claims du serveur
Claims expirés
Zone sauvage
Réglages par défaut
Réglages du joueur
Claims du groupe
Conversion des claims utilisant le sous-profil « %1$s » en cours...
Claims convertis et sous-profil « %1$s » supprimé !
Un remplacement de claims est déjà en cours pour ce joueur. Attends qu'il se termine.
Un seul joueur peut être ciblé !
Le joueur ciblé est invalide !
Aucun sous-profil ne possède cet identifiant !
Le profil principal ne peut pas être supprimé !
L'identifiant doit être unique, contenir au maximum %1$d caractères et utiliser uniquement A-Z, a-z, 0-9, « - » ou « _ ».
L'identifiant du sous-profil doit être celui de sa dimension, par exemple minecraft:the_nether.
Un sous-profil existe déjà pour cette dimension !
La limite de sous-profils (%1$s) est atteinte !
Un seul joueur peut être ciblé !
Le joueur ciblé est invalide !
Nouveau sous-profil créé !
Un seul joueur peut être ciblé !
Le joueur ciblé est invalide !
Cette configuration ne contient que %1$s sous-profils !
Sous-profils à partir de la position %1$d/%2$d :\n
, 
...
Open Parties and Claims
Open Parties and Claims
Limite de claims
Limite de chargement forcé
Claims du serveur
Mode modérateur des claims
Mode administrateur des claims
Agir au nom d'un joueur : claims
Mode administrateur des groupes
Agir au nom d'un joueur : groupe
Nombre maximal de claims que ce joueur peut posséder.
Nombre maximal de chunks que ce joueur peut maintenir chargés.
Autorise le joueur à créer ou retirer des claims du serveur et à utiliser ce mode de claim.
Autorise le joueur à utiliser le mode modérateur des claims.
Autorise le joueur à utiliser le mode administrateur des claims.
Autorise le joueur à agir au nom d'autres joueurs pour leurs claims.
Autorise le joueur à utiliser le mode administrateur des groupes.
Autorise le joueur à agir au nom d'autres joueurs pour les groupes intégrés à OPAC.
Téléportation vers les claims
Autorise le joueur à se téléporter vers les claims de n'importe quel joueur.
Nombre maximal de listes d'accès
Nombre maximal de listes de joueurs que ce joueur peut créer dans sa configuration.
Capacité des listes d'accès
Nombre d'entrées disponibles pour les listes de joueurs de cette configuration.
Tu n'as pas le droit d'interagir avec ce bloc (%1$s) !
(%1$s) Tu n'as pas le droit d'interagir avec ce bloc (%2$s) !
(%1$s) Essaie à nouveau avec la main vide.
L'interaction avec ce bloc est désactivée sur le serveur (%1$s).
Ton projectile ne peut pas atteindre les blocs de ce chunk (%1$s) !
Tu n'as pas le droit d'interagir avec cette entité dans ce chunk (%1$s) !
(%1$s) Tu n'as pas le droit d'interagir avec cette entité dans ce chunk (%2$s) !
(%1$s) Essaie à nouveau avec la main vide.
L'un de vous n'a pas le droit d'interagir avec l'autre joueur !
(%1$s) L'un de vous n'a pas le droit d'interagir avec l'autre joueur !
L'interaction avec cette entité est désactivée sur le serveur (%1$s).
Ton projectile ne peut pas atteindre les entités de ce chunk (%1$s) !
Ton projectile ne peut pas atteindre les joueurs de ce chunk (%1$s) !
Tu ne peux pas utiliser cet objet aussi près du claim d'un autre joueur (%1$s) ! Essaie avec la main vide.
(%1$s) Tu ne peux pas utiliser cet objet aussi près du claim d'un autre joueur (%2$s) ! Essaie avec la main vide.
Cet objet est désactivé sur le serveur (%1$s). Essaie avec la main vide.
(%1$s) Cet objet est désactivé sur le serveur (%2$s). Essaie avec la main vide.
Tu ne peux pas te téléporter ici avec un fruit de chorus !
Tu ne peux pas appliquer cet objet à cet endroit (%1$s) ! Essaie avec la main vide.
(%1$s) Tu ne peux pas appliquer cet objet à cet endroit (%2$s) ! Essaie avec la main vide.
(%1$s) Tu ne peux pas appliquer cet objet aussi près du claim d'un autre joueur (%2$s) ! Essaie avec la main vide.
Main principale
Main secondaire
Tu ne peux pas coller tout ou partie de la sélection.
Tu ne peux pas retirer la colle dans certains claims de cette sélection.
Tu ne peux pas piloter ce train ! Appuie sur Échap pour quitter les commandes.
%1$s - %2$s
§2Zone sauvage
Claim de %1$s%2$s
Claim du serveur%1$s
Claim expiré%1$s
%1$s%2$s
 (Chargement forcé possible)
Le serveur n'a pas répondu à OPAC. Le mod est-il installé sur le serveur ?
Le serveur a désactivé les groupes !
Le serveur a désactivé les claims !
Open Parties and Claims
Menu principal
Réglages des joueurs et claims
Informations
Claim
Retirer le claim
Forcer le chargement
Retirer le chargement forcé
Réglages du joueur
Mes réglages
%1$s - %2$s
Claims du serveur
Claims expirés
Zone sauvage
Réglages par défaut
Claims du groupe
Pseudo du joueur dont tu veux consulter les réglages
Autre joueur :
Modifier les réglages
Chargement des réglages de %1$s...
Synchronisation...
Annuler
Réglages de %1$s
Synchronisation...
Suppression de ce sous-profil en cours...
Actualiser
Groupe : %1$s
Propriétaire : %1$s
Membres : %1$s
Alliés : %1$s
Invitations : %1$s
Synchronisation...
Claims : %1$s
Nom : %1$s
Chargement forcé : %1$s
Couleur : %1$s
Synchronisation...
Sous-profil
Choisis le sous-profil à modifier. Cette sélection seule ne change pas le profil utilisé pour tes prochains claims.
Utiliser %1$s
Utiliser ce sous-profil pour les prochains claims. Les claims existants ne changent pas de profil.
Utilisé pour les nouveaux claims
Ce sous-profil est utilisé pour tes prochains claims. Les anciens claims gardent leur profil.
Supprimer %1$s
Veux-tu vraiment supprimer le sous-profil « %1$s » ?
Tous les claims qui l'utilisent seront rattachés au profil principal.
Nouveau profil
Saisis l'identifiant du sous-profil à créer.\n%1$s
OUI
NON
Ouvrir le menu OPAC
Retour
Quitter
Suiv. >>
<< Préc.
%1$s est sélectionné.
[MONTER]
[DESCENDRE]
''')

# Menus de gestion des listes d'accès et commandes administratives.
lines(454, r'''
Personne
Groupe
Alliés
Tous
Listes d'accès +
Nombre de listes d'accès supplémentaires accordées par le serveur.
Places dans les listes +
Nombre d'entrées supplémentaires accordées dans les listes d'accès.
Listes d'accès
Listes d'accès personnalisées de :
Listes incluses :
Joueurs inclus :
Créer une liste
Supprimer la liste
Inclure une liste
Retirer une liste
Ajouter un joueur
Retirer un joueur
Aucune liste d'accès personnalisée n'a encore été créée.
Choisis une liste.
Ce joueur figure déjà dans la liste !
Le joueur ciblé ne figure pas dans la liste !
La liste ciblée ne figure pas parmi les listes incluses !
Cette liste est déjà incluse !
L'action a réussi mais n'a rien changé !
Une liste possède déjà cet identifiant !
L'identifiant de la liste contient des caractères interdits !
L'identifiant de la liste est trop long !
Aucune liste ne possède cet identifiant !
Tu essaies de modifier une liste qui n'existe pas !
Cette liste d'accès n'existe plus !
Actualisation du menu pour rétablir la synchronisation...
Joueur inconnu
Choisis une liste à consulter ou à modifier.
Synchronisation en cours... Patiente un instant.
Rétablissement de la synchronisation...
Créer une liste d'accès
Saisis un identifiant court pour la nouvelle liste.
Identifiant de la nouvelle liste
Caractères autorisés :
a-z, A-Z, 0-9, - ou _, sans espaces
Caractères interdits !
Déjà utilisé !
Confirmer
Annuler
Cette option ne se modifie pas directement. Utilise les commandes prévues pour gérer ces données.
Veux-tu vraiment supprimer cette liste d'accès ?
%1$s (action irréversible !)
Inclure une liste dans une autre
Choisis la liste à inclure :
Sélection de la liste
Toutes les autres listes sont déjà incluses !
Ajouter un joueur à une liste
Choisis un joueur connecté à ajouter :
Sélection du joueur
Tous les joueurs connectés figurent déjà dans la liste !
Pseudo du joueur
Ou saisis le pseudo du joueur :
Le nombre maximal de listes d'accès est atteint !
Il ne reste plus de place dans les listes d'accès de cette configuration !
Le serveur ne connaît pas encore ce joueur ! Seuls les opérateurs peuvent effectuer cette action.
Le pseudo indiqué est invalide !
Liste d'accès « %1$s » créée !
Liste d'accès « %1$s » supprimée !
Liste « %1$s » incluse dans la liste « %2$s » !
Joueur %1$s ajouté à la liste « %2$s » !
Liste « %1$s » retirée de la liste « %2$s » !
Joueur %1$s retiré de la liste « %2$s » !
Ajoute « confirm » à la fin de la commande pour confirmer la suppression.
Vérifie que le mot « confirm » à la fin de la commande est correctement écrit.
Un seul joueur peut être ciblé !
Le joueur ciblé est invalide !
Option obsolète
Groupe de %1$s
Tu n'as pas l'autorisation d'effectuer cette action dans cette configuration !
Choisir le mode de claim
Claims personnels
Claims de groupe
Claims du serveur
Par défaut (%1$s)
L'accès à ce claim est limité : son propriétaire ou toi dépassez la limite de claims. L'accès complet et les exceptions ne fonctionnent qu'une fois toutes les %1$s minute(s).
Tu ne peux pas modifier ces réglages tant que le propriétaire dépasse sa limite de claims.
Le joueur ciblé est inconnu !
Tu ne peux agir au nom que d'un seul joueur à la fois !
Tu n'agis plus au nom d'un autre joueur pour les claims !
Tu agis maintenant au nom de %1$s ! Tu peux créer ou retirer ses claims et utiliser les exceptions de protection qui lui sont accordées.
Téléportation vers un claim de %1$s réussie !
Le joueur ciblé est invalide !
La téléportation vers les claims nécessite le mode créatif ou l'invulnérabilité.
Ce joueur ne possède aucun claim ! Essaie avec le propriétaire du groupe.
Active le mode administrateur pour supprimer tous les claims d'un autre joueur (%1$s).
Le joueur ciblé est invalide !
Le profil du joueur au nom duquel tu agis n'est plus en cache. Désactive puis réactive ce mode.
Ce joueur ne possède aucun claim !
Tu ne possèdes aucun claim !
Ajoute « confirm » pour supprimer tous tes claims (%1$s), y compris ceux de ton groupe %2$s (%3$s).
tu ne possèdes aucun claim de groupe
Ajoute « confirm » pour supprimer tous les claims de %1$s, y compris ceux de son groupe %2$s (%3$s).
ce joueur ne possède aucun claim de groupe
Suppression des claims de %1$s en cours...
Tous les claims de %1$s ont été supprimés !
Le joueur ciblé est invalide !
Tu ne peux pas transférer des claims à leur propriétaire actuel.
Ajoute « confirm » pour transférer tous tes claims (%1$s) à %2$s. Les listes d'accès seront copiées et les sous-profils transférés. Hors mode administrateur, le destinataire devra aussi accepter.
Le destinataire est hors ligne. Ce transfert nécessite le mode administrateur et le droit d'agir au nom d'autres joueurs.
Le profil du joueur au nom duquel tu agis n'est plus en cache. Désactive puis réactive ce mode.
Tu n'as plus l'autorisation d'agir au nom d'autres joueurs !
Il n'y a aucun claim à transférer !
Le destinataire ne peut recevoir que %1$s sous-profils supplémentaires, contre %2$s à transférer. Il doit d'abord en supprimer.
Tu ne peux recevoir que %1$s sous-profils supplémentaires, contre %2$s à transférer. Supprime d'abord des sous-profils.
Le destinataire ne peut recevoir que %1$s chunks supplémentaires, contre %2$s à transférer. Pour transférer un groupe et ses claims, commence par le groupe afin de transmettre le bonus de claims. Une différence de bonus personnels peut encore bloquer le transfert.
Tu ne peux recevoir que %1$s chunks supplémentaires, contre %2$s à transférer. Pour transférer un groupe et ses claims, commencez par le groupe afin de transmettre le bonus de claims. Une différence de bonus personnels peut encore bloquer le transfert.
Le destinataire ne peut recevoir que %1$s listes supplémentaires, contre %2$s à transférer. Une différence de bonus de listes peut bloquer le transfert.
Tu ne peux recevoir que %1$s listes supplémentaires, contre %2$s à transférer. Une différence de bonus de listes peut bloquer le transfert.
Le destinataire dispose de %1$s places libres dans ses listes, contre %2$s à transférer. Une différence de bonus de capacité peut bloquer le transfert.
Tu disposes de %1$s places libres dans tes listes, contre %2$s à transférer. Une différence de bonus de capacité peut bloquer le transfert.
Transfert de tes claims (%1$s) vers %2$s en cours...
Transfert des claims de %1$s vers toi (%2$s) en cours...
Tes claims (%1$s) ont été transférés à %2$s !
Les claims de %1$s t'ont été transférés (%2$s) !
Un transfert de claims est encore en cours !
Un transfert de claims est en cours. Attends qu'il se termine.
Demande de transfert de tous tes claims (%1$s) à %2$s, avec listes d'accès et sous-profils... Déconnecte-toi pour annuler !
%1$s souhaite te transférer (%3$s) tous les claims de %2$s, avec les listes d'accès et les sous-profils !
[ACCEPTER]
Accepter et lancer le transfert des claims
L'UUID du joueur indiqué est invalide !
Le joueur à l'origine de la demande de transfert n'est plus connecté.
Tu as accepté trop rapidement ! Vérifie que tu cliques sur la bonne demande de transfert.
Cette demande de transfert a expiré. Demande au joueur de la renvoyer.
Un joueur est nécessaire pour mémoriser le sous-profil actif ! Sans joueur source, indique le sous-profil du serveur directement dans la commande de claim.
Dimension inconnue ! Indique la dimension ou exécute la commande au nom d'un joueur.
Position du chunk inconnue ! Indique la position ou exécute la commande au nom d'un joueur.
Un seul joueur peut être ciblé !
Le joueur ciblé est invalide !
Dimension inconnue ! Indique la dimension ou exécute la commande au nom d'un joueur.
Position du chunk inconnue ! Indique la position ou exécute la commande au nom d'un joueur.
Un seul joueur peut être ciblé !
Le joueur ciblé est invalide !
Une opération de claims sur une zone est déjà en cours ! Attends qu'elle se termine.
Création des claims de (%1$s, %2$s) à (%3$s, %4$s), au nom de %5$s, avec le sous-profil %6$s. Patiente... %7$s
Retrait des claims de (%1$s, %2$s) à (%3$s, %4$s), au nom de %5$s. Patiente... %6$s
Marquage du chargement forcé de (%1$s, %2$s) à (%3$s, %4$s), au nom de %5$s. Patiente... %6$s
Retrait du marquage de chargement forcé de (%1$s, %2$s) à (%3$s, %4$s), au nom de %5$s. Patiente... %6$s
Création des claims terminée de (%1$s, %2$s) à (%3$s, %4$s), au nom de %5$s, avec le sous-profil %6$s. Résultats :
Retrait des claims terminé de (%1$s, %2$s) à (%3$s, %4$s), au nom de %5$s. Résultats :
Marquage du chargement forcé terminé de (%1$s, %2$s) à (%3$s, %4$s), au nom de %5$s. Résultats :
Retrait du marquage de chargement forcé terminé de (%1$s, %2$s) à (%3$s, %4$s), au nom de %5$s. Résultats :
[INTERROMPRE]
Un seul joueur peut être ciblé !
Le joueur ciblé est invalide !
L'opération de claims sur la zone a été interrompue ! La commande « interrupt » a probablement été utilisée.
Toutes les opérations de claims sur une zone ont été interrompues pour %1$s !
Cette option ne prend pas en charge l'action demandée !
Un module complémentaire a empêché l'action sur certains chunks.
Un module complémentaire a interrompu l'action de claim.
Un module complémentaire a empêché l'action sur certains chunks. Motif : %1$s
Un module complémentaire a interrompu l'action de claim. Motif : %1$s
Motifs fournis par les modules complémentaires :
Le serveur interdit aux claims de propriétaires différents de se toucher !
''')

FR[KEYS[0]] = 'Open Parties and Claims'

OPTIONS = [
('claims.usedSub', 'Sous-profil utilisé', 'Sous-profil utilisé pour les nouveaux claims. Les claims déjà créés conservent leur profil.'),
('parties.name', 'Nom du groupe', 'Nom affiché pour ton groupe OPAC.'),
('claims.name', 'Nom du territoire', 'Nom affiché pour les claims utilisant ce profil. Un nom vide utilise le nom par défaut.'),
('claims.color', 'Couleur du territoire', 'Couleur des claims sur les cartes compatibles. Saisis une valeur hexadécimale sans # ni 0x, par exemple AA55FF pour le violet.'),
('claims.bonusChunkClaims', 'Claims supplémentaires', 'Nombre de claims supplémentaires accordés au propriétaire, en plus de sa limite habituelle.'),
('claims.bonusChunkForceloads', 'Chargements forcés en plus', 'Nombre de chunks supplémentaires que le propriétaire peut maintenir chargés, en plus de sa limite habituelle.'),
('customPlayerGroups', 'Listes d’accès personnalisées', 'Listes de joueurs utilisables pour les exceptions de protection. Gère-les avec le bouton « Listes d’accès » ou les commandes dédiées.'),
('claims.protectClaimedChunks', 'Protection des claims', 'OUI active la protection des chunks utilisant ce profil. NON désactive ces protections, même si les chunks restent claim.'),
('claims.protection.exceptions.fullAccess', 'Accès complet au claim', 'Accorde un accès complet aux membres de la liste choisie. Le propriétaire conserve son accès. « Tous » ouvre le claim à tout le monde et contourne les protections.'),
('claims.protection.exceptions.blocksByExplosions', 'Dégâts des explosions', 'OUI autorise les explosions à détruire les blocs. Les explosions de creepers dépendent aussi des règles de modification des blocs par les créatures.'),
('claims.protection.exceptions.blocksByPlayers', 'Blocs : joueurs', 'Autorise les joueurs de la liste choisie à casser des blocs et à interagir avec eux. La pose de blocs dépend généralement aussi de l’utilisation des objets.'),
('claims.protection.exceptions.blocksByMobs', 'Blocs : créatures', 'Autorise les créatures appartenant aux joueurs de la liste choisie à casser ou poser des blocs, comme les Endermen. « Tous » inclut les créatures sans propriétaire. Certaines protections s’étendent aux chunks voisins. Les créatures ajoutées par des mods peuvent ne pas être couvertes. Les creepers dépendent aussi des règles d’explosion.'),
('claims.protection.exceptions.blocksByOther', 'Blocs : autres entités', 'Autorise les entités non vivantes appartenant aux joueurs de la liste choisie à modifier les blocs. « Tous » inclut celles sans propriétaire. Les explosions disposent de réglages distincts. Le comportement des entités ajoutées par des mods peut ne pas être couvert.'),
('claims.protection.exceptions.blocksRedirect', 'Blocs : suivre le responsable', 'OUI utilise la catégorie du propriétaire de l’entité pour les actions sur les blocs. Exemple : une flèche tirée par un joueur utilise les règles « Blocs : joueurs ». Les droits d’accès au claim sont toujours vérifiés auprès du propriétaire de l’entité.'),
('claims.protection.exceptions.fireSpread', 'Propagation du feu', 'OUI autorise le feu à se propager dans ces claims.'),
('claims.protection.exceptions.blocksByEnchantments', 'Blocs : enchantements', 'Autorise les enchantements, comme Semelles givrantes, à modifier les blocs pour les joueurs de la liste choisie et les entités qui leur appartiennent.'),
('claims.protection.exceptions.cropTrample', 'Piétinement des cultures', 'OUI autorise le piétinement des terres cultivées dans ces claims.'),
('claims.protection.fluidBarrier', 'Bloquer les fluides externes', 'OUI empêche les fluides, comme l’eau ou la lave, d’entrer dans les claims protégés depuis l’extérieur. NON retire cette barrière. Cette option ne protège pas la zone sauvage.'),
('claims.protection.pistonBarrier', 'Bloquer les pistons externes', 'OUI empêche les pistons situés à l’extérieur d’agir sur les claims protégés. NON retire cette barrière. Cette option ne protège pas la zone sauvage.'),
('claims.protection.exceptions.buttonsByProjectiles', 'Boutons : projectiles', 'Autorise les projectiles appartenant aux joueurs de la liste choisie à actionner les boutons. « Tous » inclut les projectiles sans propriétaire.'),
('claims.protection.exceptions.targetsByProjectiles', 'Cibles : projectiles', 'Autorise les projectiles appartenant aux joueurs de la liste choisie à actionner les blocs cibles.'),
('claims.protection.exceptions.platesByPlayers', 'Plaques : joueurs', 'Autorise les joueurs de la liste choisie à actionner les plaques de pression.'),
('claims.protection.exceptions.platesByMobs', 'Plaques : créatures', 'Autorise les créatures appartenant aux joueurs de la liste choisie à actionner les plaques de pression. « Tous » inclut les créatures sans propriétaire.'),
('claims.protection.exceptions.platesByOther', 'Plaques : autres entités', 'Autorise les entités non vivantes appartenant aux joueurs de la liste choisie à actionner les plaques de pression. « Tous » inclut les entités sans propriétaire.'),
('claims.protection.exceptions.tripwireByPlayers', 'Fils : joueurs', 'Autorise les joueurs de la liste choisie à déclencher les fils de détection.'),
('claims.protection.exceptions.tripwireByMobs', 'Fils : créatures', 'Autorise les créatures appartenant aux joueurs de la liste choisie à déclencher les fils de détection. « Tous » inclut les créatures sans propriétaire.'),
('claims.protection.exceptions.tripwireByOther', 'Fils : autres entités', 'Autorise les entités non vivantes appartenant aux joueurs de la liste choisie à déclencher les fils de détection. « Tous » inclut les entités sans propriétaire.'),
('claims.protection.exceptions.entitiesByPlayers', 'Entités : joueurs', 'Autorise les joueurs de la liste choisie à interagir avec les créatures amicales et les autres entités protégées définies par le serveur, y compris à les attaquer.'),
('claims.protection.exceptions.entitiesByMobs', 'Entités : créatures', 'Autorise les créatures appartenant aux joueurs de la liste choisie à interagir avec les entités protégées, y compris à les attaquer. « Tous » inclut les créatures sans propriétaire. Certaines protections s’étendent aux chunks voisins.'),
('claims.protection.exceptions.entitiesByOther', 'Entités : autres entités', 'Autorise les entités non vivantes, comme les flèches, les enclumes en chute ou la TNT allumée, à agir sur les entités protégées si leur propriétaire appartient à la liste choisie. « Tous » inclut les entités sans propriétaire.'),
('claims.protection.exceptions.entitiesRedirect', 'Entités : suivre le responsable', 'OUI applique aux attaques et interactions la catégorie du propriétaire de l’entité. Exemple : la flèche d’un joueur suit les règles « Entités : joueurs ». Les droits d’accès au claim sont toujours vérifiés auprès du propriétaire de l’entité.'),
('claims.protection.exceptions.entitiesByExplosions', 'Entités : dégâts d’explosion', 'OUI autorise les explosions à affecter les créatures amicales et les autres entités protégées du claim. Les explosions déclenchées directement par le propriétaire du claim ne sont pas protégées par défaut.'),
('claims.protection.exceptions.entitiesByFire', 'Entités : dégâts du feu', 'OUI autorise le feu à blesser les créatures amicales et les autres entités protégées dans ces claims.'),
('claims.protection.exceptions.raids', 'Raids de village', 'OUI autorise les raids dans les villages de ces claims.'),
('claims.protection.exceptions.playersByPlayers', 'Joueurs : attaques de joueurs', 'OUI autorise OPAC à laisser passer les attaques et interactions entre joueurs. Les autres règles du serveur, dont le système de PvP, restent applicables.'),
('claims.protection.exceptions.playersByMobs', 'Joueurs : attaques de créatures', 'OUI autorise les créatures à attaquer les joueurs et à interagir avec eux dans ces claims.'),
('claims.protection.exceptions.playersByOther', 'Joueurs : autres dégâts', 'OUI autorise les entités non vivantes, comme les projectiles, à attaquer les joueurs ou à interagir avec eux dans ces claims.'),
('claims.protection.exceptions.playersRedirect', 'Joueurs : suivre le responsable', 'OUI applique aux attaques et interactions la catégorie du propriétaire de l’entité. Exemple : la flèche d’un joueur suit les règles des attaques entre joueurs.'),
('claims.protection.exceptions.playerLightning', 'Foudre provoquée par joueur', 'Autorise la foudre provoquée par les joueurs de la liste choisie, par exemple avec Canalisation.'),
('claims.protection.exceptions.chorusFruitTeleport', 'Téléportation par chorus', 'Autorise les joueurs de la liste choisie à entrer dans ces claims par téléportation avec un fruit de chorus.'),
('claims.protection.exceptions.netherPortalsPlayers', 'Portails Nether : joueurs', 'Autorise les joueurs de la liste choisie à utiliser les portails du Nether. Ce réglage concerne leur utilisation, pas leur construction.'),
('claims.protection.exceptions.netherPortalsMobs', 'Portails Nether : créatures', 'Autorise les créatures appartenant aux joueurs de la liste choisie à utiliser les portails du Nether. « Tous » inclut les créatures sans propriétaire.'),
('claims.protection.exceptions.netherPortalsOther', 'Portails Nether : autres', 'Autorise les entités non vivantes appartenant aux joueurs de la liste choisie à utiliser les portails du Nether. « Tous » inclut les entités sans propriétaire.'),
('claims.protection.dispenserBarrier', 'Bloquer distributeurs externes', 'OUI empêche les distributeurs situés à l’extérieur de distribuer directement dans le claim.'),
('claims.protection.exceptions.itemUse', 'Utilisation des objets', 'Autorise la liste choisie à utiliser les objets tenus en main avec un clic droit. Sous Fabric, cela peut aussi autoriser la pose de blocs sur des blocs accessibles. Certains objets peuvent casser des blocs par leur clic droit. Les protections des chunks voisins peuvent encore bloquer l’action.'),
('claims.protection.neighborChunksItemUse', 'Protéger l’usage aux abords', 'OUI étend la protection contre l’utilisation d’objets aux chunks voisins afin de limiter les actions depuis l’extérieur du claim.'),
('claims.protection.exceptions.itemTossPlayers', 'Objets jetés : joueurs', 'Autorise les joueurs de la liste choisie à jeter des objets dans ces claims.'),
('claims.protection.exceptions.itemTossMobs', 'Objets jetés : créatures', 'Autorise les créatures appartenant aux joueurs de la liste choisie à jeter des objets. « Tous » inclut les créatures sans propriétaire, comme les villageois qui partagent de la nourriture.'),
('claims.protection.exceptions.itemTossOther', 'Objets jetés : autres', 'Autorise les entités non vivantes appartenant aux joueurs de la liste choisie à déposer ou jeter des objets. « Tous » inclut les entités sans propriétaire.'),
('claims.protection.exceptions.itemTossRedirect', 'Jets : suivre le responsable', 'OUI utilise la catégorie du propriétaire de l’entité pour les objets jetés. Exemple : un objet provenant d’une entité appartenant à un joueur suit les règles des joueurs.'),
('claims.protection.exceptions.mobLoot', 'Butin des créatures', 'Autorise les créatures appartenant aux joueurs de la liste choisie à laisser leur butin. « Tous » inclut les créatures sans propriétaire.'),
('claims.protection.playerDeathLoot', 'Protéger le butin à la mort', 'Protège les objets et l’expérience perdus à la mort des joueurs de la liste choisie, même si le ramassage ordinaire est autorisé. Le joueur mort et le joueur ou l’entité qui l’a tué conservent l’accès à ce butin.'),
('claims.protection.exceptions.itemPickupPlayers', 'Ramassage : joueurs', 'Autorise les joueurs de la liste choisie à ramasser des objets qui ne leur appartiennent pas.'),
('claims.protection.exceptions.itemPickupMobs', 'Ramassage : créatures', 'Autorise les créatures à ramasser les objets qui ne leur appartiennent pas, selon la liste choisie. « Tous » inclut les villageois et les autres créatures sans propriétaire. Certaines créatures peuvent échapper à cette protection ; certains contrôles s’étendent aux chunks voisins.'),
('claims.protection.exceptions.itemPickupRedirect', 'Ramassage : suivre le maître', 'OUI applique la règle de ramassage du propriétaire de la créature. Exemple : un Allay appartenant à un joueur suit les règles « Ramassage : joueurs ».'),
('claims.protection.exceptions.xpPickup', 'Ramassage de l’expérience', 'Autorise les joueurs de la liste choisie à ramasser les orbes d’expérience qui ne leur appartiennent pas.'),
('claims.protection.overrideMobGriefingRule', 'Priorité aux règles OPAC', 'OUI remplace certains contrôles de la règle vanilla mobGriefing par les protections OPAC des blocs, entités ou objets, dans les claims et à leurs abords. La plupart utilisent la protection des blocs. Le ramassage ordinaire dispose déjà de sa propre protection. Sous Fabric, certains comportements de créatures ajoutées par des mods ne peuvent pas être remplacés.'),
('claims.protection.exceptions.naturalSpawnHostile', 'Apparition des monstres', 'OUI autorise l’apparition naturelle des créatures hostiles dans ces claims.'),
('claims.protection.exceptions.naturalSpawnFriendly', 'Apparition des animaux', 'OUI autorise l’apparition naturelle des créatures amicales dans ces claims.'),
('claims.protection.exceptions.spawnersHostile', 'Générateurs de monstres', 'OUI autorise les générateurs de créatures hostiles à fonctionner dans ces claims.'),
('claims.protection.exceptions.spawnersFriendly', 'Générateurs d’animaux', 'OUI autorise les générateurs de créatures amicales à fonctionner dans ces claims.'),
('claims.protection.exceptions.projectileHitHostileSpawn', 'Monstres issus de projectiles', 'Autorise les projectiles appartenant aux joueurs de la liste choisie à faire apparaître des créatures hostiles, par exemple un Endermite à partir d’une perle de l’Ender.'),
('claims.protection.exceptions.projectileHitFriendlySpawn', 'Animaux issus de projectiles', 'Autorise les projectiles appartenant aux joueurs de la liste choisie à faire apparaître des créatures amicales, par exemple un poussin à partir d’un œuf.'),
('claims.forceload.enabled', 'Chargement forcé des chunks', 'OUI maintient chargés les chunks marqués pour le chargement forcé. Les quotas et autres restrictions du serveur restent applicables.'),
('claims.forceload.offlineForceload', 'Chargement même hors ligne', 'OUI autorise le chargement forcé quand le propriétaire est hors ligne, dans les limites fixées par le serveur.'),
('claims.wholePartyCanClaim', 'Tout le groupe peut claim', 'OUI permet aux membres du groupe de participer aux claims de groupe selon les règles d’accès OPAC.'),
('claims.protection.exceptions.reclaimable', 'Reprise du terrain autorisée', 'Permet à la liste choisie de reprendre ces chunks par une action de claim. Cela peut transférer leur propriété : ne choisis « Tous » que si tu souhaites rendre le terrain reprenable.'),
('parties.shareLocationWithParty', 'Partager ma position : groupe', 'OUI partage ta position avec les membres de ton groupe sur les cartes compatibles.'),
('parties.shareLocationWithMutualAllyParties', 'Partager ma position : alliés', 'OUI partage ta position avec les groupes dont l’alliance est réciproque.'),
('parties.receiveLocationsFromParty', 'Voir les positions du groupe', 'OUI reçoit les positions partagées par les membres de ton groupe.'),
('parties.receiveLocationsFromMutualAllyParties', 'Voir les positions des alliés', 'OUI reçoit les positions partagées par les groupes dont l’alliance est réciproque.'),
]

for path, label, tip in OPTIONS:
    set_option(path, label, tip)

GROUP_OPTIONS = [
('block.interact', 'Utiliser (%1$s)', 'Autorise la liste choisie à interagir avec les blocs de cette catégorie.'),
('block.handInteract', 'Main vide (%1$s)', 'Autorise la liste choisie à interagir avec les blocs de cette catégorie avec la main vide.'),
('block.anyItemInteract', 'Tout objet (%1$s)', 'Autorise la liste choisie à interagir avec les blocs de cette catégorie avec n’importe quel objet tenu en main. Certaines utilisations d’objets peuvent aussi modifier ou détruire des blocs.'),
('block.break', 'Casser (%1$s)', 'Autorise la liste choisie à casser les blocs de cette catégorie.'),
('entity.interact', 'Utiliser (%1$s)', 'Autorise la liste choisie à interagir avec les entités de cette catégorie.'),
('entity.handInteract', 'Main vide (%1$s)', 'Autorise la liste choisie à interagir avec les entités de cette catégorie avec la main vide.'),
('entity.anyItemInteract', 'Tout objet (%1$s)', 'Autorise la liste choisie à interagir avec les entités de cette catégorie avec n’importe quel objet tenu en main.'),
('entity.break', 'Attaquer (%1$s)', 'Autorise la liste choisie à attaquer ou détruire les entités de cette catégorie.'),
('entity.barrier', 'Passage (%1$s)', 'Autorise les entités de cette catégorie à franchir la limite du claim selon leur propriétaire et la liste choisie. « Tous » inclut les entités sans propriétaire.'),
('entity.blockAccess', 'Blocs (%1$s)', 'Autorise les entités de cette catégorie à modifier les blocs et à interagir avec eux, selon la liste choisie. Avec Villagers et « Tous », les fermiers peuvent récolter et replanter.'),
('entity.blockBreakAccess', 'Cassage (%1$s)', 'Autorise les entités de cette catégorie à casser des blocs, selon la liste choisie.'),
('entity.blockInteractAccess', 'Usage blocs (%1$s)', 'Autorise les entités de cette catégorie à interagir avec les blocs, selon la liste choisie.'),
('entity.entityAccess', 'Entités via (%1$s)', 'Autorise les entités de cette catégorie à attaquer les entités protégées et à interagir avec elles, selon la liste choisie.'),
('entity.entityAttackAccess', 'Attaques via (%1$s)', 'Autorise les entités de cette catégorie à attaquer les entités protégées, selon la liste choisie.'),
('entity.entityInteractAccess', 'Usage entités (%1$s)', 'Autorise les entités de cette catégorie à interagir avec les entités protégées, selon la liste choisie.'),
('entity.playerAccess', 'Joueurs via (%1$s)', 'Autorise les entités de cette catégorie à attaquer les joueurs et à interagir avec eux, selon la liste choisie.'),
('entity.playerAttackAccess', 'Att. joueurs (%1$s)', 'Autorise les entités de cette catégorie à attaquer les joueurs, selon la liste choisie.'),
('entity.playerInteractAccess', 'Usage joueurs (%1$s)', 'Autorise les entités de cette catégorie à interagir avec les joueurs, selon la liste choisie.'),
('entity.droppedItemAccess', 'Ramassage (%1$s)', 'Autorise les entités de cette catégorie à ramasser les objets selon la liste choisie. Une autorisation générale de ramassage peut déjà leur donner accès ; « Personne » n’annule pas les autres autorisations.'),
('item.interact', 'Utiliser (%1$s)', 'Autorise la liste choisie à utiliser les objets de cette catégorie.'),
]
for suffix, label, tip in GROUP_OPTIONS:
    set_option('claims.protection.exceptions.groups.' + suffix, label, tip)

# The English "default" values are sentinels that expose Java comments.
# Replace every sentinel with real French help, never with "par défaut".
HELP = '\n\nHérité : valeur du profil parent. Une option grisée ne peut pas être modifiée dans ce menu.'
for key in list(FR):
    if key.startswith('gui.xaero_pac_player_config_tooltip_playerConfig.'):
        FR[key] += HELP

def build():
    missing = set(SOURCE) - set(FR)
    assert not missing, f'Missing translations: {sorted(missing)}'
    placeholders = re.compile(r'%(?:\d+\$)?[sdf]')
    for key, original in SOURCE.items():
        assert sorted(placeholders.findall(original)) == sorted(placeholders.findall(FR[key])), key
        assert FR[key] != 'default', key
    assert FR['gui.xaero_pac_title_wilderness'] == '§2Zone sauvage'
    # Keep the legacy alias already present in the production resource pack.
    FR['Wilderness'] = '§2Zone sauvage'
    assert FR['gui.xaero_pac_ui_on'] == 'OUI'
    assert FR['gui.xaero_pac_ui_off'] == 'NON'
    assert FR['gui.xaero_pac_config_option_sub_inherited'] == 'Hérité'
    assert FR['gui.xaero_pac_ui_sub_config_dropdown'] == 'Sous-profil'
    lang = (json.dumps(FR, ensure_ascii=False, indent=2) + '\n').encode('utf-8')
    (ROOT / 'fr_fr.json').write_bytes(lang)
    meta = json.loads(BASE.read('pack.mcmeta'))
    meta['pack']['description'] = 'Le Comptoir des Artisans — Grades, badges et OPAC en français'
    meta['pack']['min_format'] = 88
    meta['pack']['max_format'] = 88
    additions = {
        'pack.mcmeta': (json.dumps(meta, ensure_ascii=False, indent=2) + '\n').encode('utf-8'),
        'assets/openpartiesandclaims/lang/fr_fr.json': lang,
        # The existing server pack already translates OPAC's English fallback
        # into French. Preserve that server-wide presentation convention.
        'assets/openpartiesandclaims/lang/en_us.json': lang,
        'OPAC-FR-LISEZMOI.md': (ROOT / 'README.md').read_bytes(),
    }
    output = ROOT / 'Taverne_Ranks_MCModels_32_Badges_v7_OPAC_FR.zip'
    with zipfile.ZipFile(output, 'w', zipfile.ZIP_DEFLATED, compresslevel=9) as out:
        for info in BASE.infolist():
            out.writestr(copy.copy(info), additions.pop(info.filename, BASE.read(info.filename)))
        for name, content in additions.items():
            info = zipfile.ZipInfo(name, (2026, 9, 13, 12, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            out.writestr(info, content)
    new = zipfile.ZipFile(output)
    assert new.testzip() is None
    assert len(new.namelist()) == len(set(new.namelist()))
    changed = {'pack.mcmeta', 'assets/openpartiesandclaims/lang/fr_fr.json', 'assets/openpartiesandclaims/lang/en_us.json'}
    assert set(BASE.namelist()).issubset(new.namelist())
    for name in BASE.namelist():
        if name not in changed:
            assert BASE.read(name) == new.read(name), f'Unexpected asset change: {name}'
    for name in new.namelist():
        if name.endswith(('.json', '.mcmeta')):
            json.loads(new.read(name))
    report = {
        'filename': output.name,
        'minecraft': '26.2', 'opac': '0.31.6', 'resource_format': 88,
        'opac_source_sha256': '31897294699545a630b42c5481a67bda9072f57c1a785971a9b915f26d973ced',
        'original_pack_sha1': hashlib.sha1(BASE_PATH.read_bytes()).hexdigest(),
        'sha1': hashlib.sha1(output.read_bytes()).hexdigest(),
        'sha256': hashlib.sha256(output.read_bytes()).hexdigest(),
        'bytes': output.stat().st_size,
        'upstream_keys': len(SOURCE), 'translated_upstream_keys': len(set(SOURCE) & set(FR)),
        'output_keys': len(FR), 'translated_tooltips': sum('config_tooltip_' in k for k in FR),
        'preserved_original_entries': len(BASE.namelist()) - len(changed),
        'checks': ['all OPAC keys present', 'all format placeholders preserved', 'no default tooltip sentinel', 'all JSON valid', 'ZIP CRC valid', 'all unrelated resources byte-identical', 'dark green wilderness preserved'],
        'visual_test_in_game': False,
        'limitation': 'OPAC passes custom group IDs and profile IDs as literal strings; a resource pack cannot translate those names. Command syntax and IDs are preserved.'
    }
    (ROOT / 'validation.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps(report, ensure_ascii=False, indent=2))

if __name__ == '__main__':
    build()
