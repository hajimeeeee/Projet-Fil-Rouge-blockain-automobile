#Description des fonctionnalitées
#### Un fabriquant
Une fois qu'une voiture est fabriquée, elle est ajoutée à la blockchain en fournissant des informations de base sur la voiture, son ID, son pays d'origine, son kilométrage égal à 0, etc.

#### Garage
Dans ce projet, il existe deux types de garage :
1. Dans l'UE, il est obligatoire de se rendre (tous les 2 ans) dans un garage réglementée par le gouvernement afin de vérifier les fonctionnalités de base du véhicule.
   La station doit décider si la voiture est capable circuler en sécurité.

2. Les autres garages, qui ne sont pas tellement réglementées, s'occupent de la réparation des voitures.

Supposons que les garage de type 1 ajoutent également une vérification du kilométrage,
ce qui signifie qu'elles créent une transaction dans la blockchain qui augmente le kilométrage de la voiture. Dans la plupart des pays de l'UE, la vérification du kilométrage est effectuée par le gouvernement uniquement lorsqu'une voiture change de propriétaire.
Par conséquent, si la station-service effectue des contrôles du kilométrage, l'intervalle entre les contrôles est réduit et, par conséquent, le tempérament avec le kilométrage est moins efficace et moins attrayant.

#### Changement de propriétaire d'une voiture
Le vendeur et l'acheteur créent un contrat intelligent qui doit être validé par quelqu'un.
La validation déclenche alors le contrat intelligent. Ainsi, cette personne doit donc vérifier que l'argent a été transféré, ce qui peut être fait par un notaire ou une banque.

#### Mineurs
Seule la blockchain elle-même serait publique, mais les mineurs resteraient privés.
Les mineurs sont des serveurs gouvernementaux et des serveurs fournis par les utilisateurs de type 2.
pour motiver ces utilisateurs à fournir un serveur pour le minage, ils paieraient moins de frais pour la gestion de leur entreprise.

Les mineurs sont privés, le réseau devrait donc être protégé contre une attaque de 51 % et les utilisateurs du réseau continueront à lui faire confiance, car il est largement utilisé dans l'UE. 
Ainsi, même si les utilisateurs ne font pas confiance au gouvernement du pays dans lequel ils vivent, ils croient aux données de la blockchain car elles ont été validées par tous les pays et tous les utilisateurs de type 2
Il est donc très peu probable que les données soient altérées, car il est peu probable que tous les mineurs parviennent à un consensus pour le faire.

#### Contrôle de police / patrouille automobile
Un policier scanne la plaque d'immatriculation, découvre la clé publique du propriétaire (il s'agit d'une information publique stockée dans la blockchain) et utilise ensuite la clé publique pour rechercher le propriétaire dans la base de données de la police (il s'agit d'un système privé, seule la police peut y accéder).

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
```
$ ./blockchain.py
```
Dans un second terminal, exécutez ce qui suit :
```
$ ./fabriquant.py
```
afin de créer un bloc qui sera miné par des mineurs (processus). Le script ci-dessus simule un fabricant. Il génère un identifiant aléatoire qui est considéré comme l'identifiant de la voiture fabriquée. Il fixe son kilométrage à 0 et définit des données supplémentaires telles que le fabricant, le modèle, l'année et le pays d'origine.

Exécutez le script suivant pour simuler un changement de propriétaire de la voiture.
REMARQUE : il s'agit d'une simple démo, les utilisateurs ne doivent donc pas nécessairement exister.
Vous pouvez inventer l'identifiant de l'acheteur, cependant, pour l'identifiant de la voiture, utilisez le script `fabriquant.py` généré à l'étape précédente.
```
$ ./vendeur.py <vendeur_ID> <acheteur_ID> <car_ID>
```

Exécutez le script suivant afin de simuler une vérification du kilométrage d'une voiture.
```
$ ./garage.py <car_ID>
```

Essayez à nouveau de changer de propriétaire.
```
$ ./vendeur.py <vendeur_ID> <acheteur_ID> <car_ID>
```

Exécutez le script suivant pour dresser la liste de l'historique de la voiture. Il imprimera tous les blocs où l'identifiant de la voiture est trouvé.
```
$ ./historique.py <car_ID>
```