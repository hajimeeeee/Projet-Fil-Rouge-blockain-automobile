#### Un fabriquant
Une fois qu'une voiture est fabriquée, elle est ajoutée à la blockchain en fournissant des informations de base sur la voiture, son ID, son pays d'origine, son kilométrage égal à 0, etc.

#### Garage
Dans ce porjet, il existe deux types de garage :
1. Dans l'UE, il est obligatoire de se rendre (tous les 2 ans) dans un garage réglementée par le gouvernement afin de vérifier les fonctionnalités de base du véhicule.
   La station doit décider si la voiture est capable circuler en sécurité.

2. Les autres garages, qui ne sont pas tellement réglementées, s'occupent de la réparation des voitures.

Supposons que les garage de type 1 ajoutent également une vérification du kilométrage,
ce qui signifie qu'elles créent une transaction dans la blockchain qui augmentele kilométrage de la voiture. Dans la plupart des pays de l'UE, la vérification du kilométrage est effectuée par le gouvernement uniquement lorsqu'une voiture change de propriétaire.
Ainsi, si la station-service effectue des
l'intervalle entre les contrôles est réduit et, par conséquent, le tempérament
Le tempérament au kilométrage est donc moins efficace et moins attrayant.

#### Changement de propriétaire d'une voiture
Le vendeur et l'acheteur créent un contrat intelligent qui doit être validé par quelqu'un.
par quelqu'un. La validation déclenche alors le contrat intelligent. Ainsi, cette personne
doit donc vérifier que l'argent a été transféré, ce qui peut être fait par un notaire ou une banque.

#### Mineurs
Seule la blockchain elle-même serait publique, mais les mineurs resteraient privés.
Les mineurs sont des serveurs gouvernementaux et des serveurs fournis par les utilisateurs de type 2. Pour
pour motiver ces utilisateurs à fournir un serveur pour le minage, ils paieraient moins de frais
pour la gestion de leur entreprise.

Les mineurs étant privés, le réseau devrait être protégé contre une attaque de 51 % et les utilisateurs du réseau auront toujours confiance en eux.
Les utilisateurs du réseau continueront à lui faire confiance, car il est largement utilisé dans l'UE.
l'UE, de sorte que même si les utilisateurs ne font pas confiance au gouvernement du pays dans lequel ils vivent, ils croient aux données contenues dans le réseau.
dans lequel ils vivent, ils croient aux données de la blockchain parce qu'elles ont été validées par tous les pays et tous les utilisateurs de type 2.
tous les pays et tous les utilisateurs de type 2 - il est donc très peu probable que les données soient corrompues, parce que le gouvernement n'a pas le droit de les modifier.
de tempérer les données, car il est peu probable que tous les mineurs parviennent à un consensus pour le faire.

#### Contrôle de police / patrouille automobile
Un policier scanne la plaque de la voiture, découvre la clé publique du propriétaire (il s'agit d'une information publique stockée dans la blockchain).
publique du propriétaire (il s'agit d'une information publique stockée dans la blockchain) et utilise ensuite la clé publique pour rechercher le propriétaire dans la base de données de la police.
pour rechercher le propriétaire dans la base de données de la police (il s'agit d'un système privé, seule la police peut y accéder).

## Mise en œuvre de la démo

`blockchain.py` représente l'ensemble du réseau, y compris les mineurs. Le réseau est
Le réseau est implémenté comme un serveur python qui crée 3 processus indépendants (mineurs)
lorsqu'il reçoit un nouveau bloc à valider.

`block.py` contient une classe Block qui représente un bloc de la blockchain.

`miner.py` contient une classe Miner qui représente un mineur.


# Installation
Aucune installation particulière n'est nécessaire, il suffit d'avoir `python 3.6`.

# Exécuter la démo
Démarrez le réseau et initialisez la blockchain en :
``console
$ ./blockchain.py
```
Dans un second terminal, exécutez ce qui suit :
``console
$ ./manufacturer.py
```
afin de créer un bloc qui sera miné par des mineurs (processus).
Le script ci-dessus simule un fabricant. Il génère un identifiant aléatoire qui
qui est considéré comme l'ID de la voiture fabriquée. Il fixe son kilométrage à 0 et
des données supplémentaires telles que le fabricant (MINI), le modèle (Cooper S), l'année
(année en cours), pays_d'origine (France).

Exécutez le script suivant pour simuler un changement de propriétaire de la voiture.
REMARQUE : il s'agit d'une simple démo, les utilisateurs ne doivent donc pas nécessairement exister.
Vous pouvez inventer l'identifiant de l'acheteur, cependant, pour l'identifiant de la voiture, utilisez le script `manufacturer.py` généré à l'étape précédente.
généré dans l'étape précédente et comme identifiant du vendeur, utilisez l'identifiant du constructeur.
``console
$ ./seller.py <seller_ID> <buyer_ID> <car_ID>
```

Exécutez le script suivant afin de simuler une vérification lorsque le kilométrage d'une
d'une voiture.
```console
$ ./service_station.py <car_ID>
```

Essayez à nouveau de changer de propriétaire.
``console
$ ./seller.py <seller_ID> <buyer_ID> <car_ID>
```

Exécutez le script suivant pour dresser la liste de l'historique de la voiture. Il imprimera tous les blocs
blocs où l'identifiant de la voiture est trouvé.
```console
$ ./car_history.py <car_ID>