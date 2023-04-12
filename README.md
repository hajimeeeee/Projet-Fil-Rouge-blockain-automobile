# Projet-Fil-Rouge-blockain-automobile
## Introduction

Depuis des décennies, les particuliers et les entreprises sont confrontés au même dilemme lors de l'achat d'un véhicule d'occasion. Comment l'acheteur peut-il s'assurer qu'un véhicule est réellement dans les conditions exactes décrites par le vendeur ? Comment l'acheteur peut-il avoir confiance lorsqu'il achète un véhicule d'occasion sans avoir à se soucier de son histoire, de son kilométrage, de son historique d'entretien, de son historique d'inspection et de nombreux autres facteurs essentiels pour évaluer l'état d'un véhicule ?

---

## Objectif 
### Transparence 
L'objectif est d'atteindre une transparence totale au niveau des véhicules. Grâce à la blockchain les historiques de transaction du véhicule deviennent transparents afin que les futurs acheteur connaissent l'intégralité des transaction lié à son véhicule.

### Tracabilité et sécurité
Les transactions pourront se faire via la blockchain afin de savoir qui à acheter le véhicule et quand.La blockchain fournit un mécanisme de chriffrage pour approuver les transactions. Dans l'industrie automobile, l'achat d'un véhicule doit passer par une chaîne de processus et il peut être très coûteux et fastidieux de retracer un article depuis son origine. C'est pourquoi nous allons mettre en place la blochain afin d'avoir de la tracabilité à ce niveau là.

L'objectif de la mise en place d'une Blockchain pour le monde automobile est de pouvoir suivre ces points suivant :

* Suivi entretien des véhicules
* Certification du kilométrage
* Véhicule accidenté ou non
* Nombre de propriétaire 
* Provenance du véhicule

### Supply Chain Managament

La chaîne d'approvisionnement de l'industrie automobile est un dispositif logistique massif qui fait partie intégrante de toute entreprise de construction automobile. Elle sert d'intermédiaire entre de multiples parties et optimise la création et la distribution des ressources, mais la présence de nombreuses parties en interaction, les différences de prix et les problèmes de qualité et de complexité créent un cauchemar logistique qui entraîne un gaspillage de temps et de ressources.



## Proof of Concept

### 1. Créer une blockchain privée
Tout d'abord, créer une blockchain privée permettra de limiter l'accès aux informations uniquement aux parties autorisées, telles que les propriétaires du véhicule, les concessionnaires automobiles et les organismes gouvernementaux.

### 2. Identifier les informations clés à stocker sur la blockchain
Les informations à stocker sur la blockchain pour suivre un véhicule comprennent le kilométrage, le nombre de propriétaires, les entretiens et réparations effectués, les accidents impliquant le véhicule et tout autre détail important.

### 3. Créer des smart contracts
Les smart contracts sont des programmes autonomes qui s'exécutent automatiquement lorsqu'une condition spécifique est remplie. Ils peuvent être utilisés pour automatiser la gestion des informations de suivi de véhicule sur la blockchain. Par exemple, un smart contract pourrait être utilisé pour déclencher une notification à un propriétaire de véhicule lorsque le kilométrage de son véhicule atteint un certain seuil.

### 4. Enregistrer les informations de suivi sur la blockchain
Une fois que les informations clés ont été identifiées et les smart contracts créés, les données de suivi peuvent être enregistrées sur la blockchain à l'aide d'un protocole de consensus tel que la preuve de travail ou la preuve d'enjeu.

### 5. Créer une interface utilisateur pour accéder aux informations de suivi
Une interface utilisateur conviviale peut être créée pour permettre aux parties autorisées d'accéder facilement aux informations de suivi du véhicule. Cette interface peut être utilisée pour vérifier l'historique du véhicule, les propriétaires précédents, les entretiens et réparations effectués, etc.

### 6. Tester le système 
Pour s'assurer que le système fonctionne correctement, il est important de le tester en simulant différents scénarios d'utilisation. Les tests doivent inclure la vérification de l'exactitude et de l'intégrité des données stockées sur la blockchain, ainsi que la vérification de la capacité du système à gérer différents cas d'utilisation.

En utilisant cette approche, il est possible de créer un système de suivi de véhicule sécurisé, précis et transparent basé sur la blockchain. Ce système peut être utilisé pour suivre les informations importantes liées à un véhicule tout au long de sa durée de vie, ce qui peut aider à améliorer la confiance des acheteurs et des vendeurs dans le marché des voitures d'occasion.

## Compte rendu 
### 25/01 : Idée de projet 
- Recherche de l'idée de projet Blockchain 
- Veille et recherche sur les Blockchain automobile

### 08/02 : Mise en place de l'infrastructure de la blockchain
- Création de la base de la blockchain en python -> Création "Block.py" & "Blockchain.py" utilisée pour créer, manipuler et vérifier des blocs de données.
- Implémentation d'un réseau blockchain simulé en utilisant des processus indépendants pour simuler les mineurs.

### 01/03 : 
- Ajustement et améliorations des fichiers "Block.py" & "Blockchain.py"
- Ajout d'une classe "Miner.py" qui implémente les méthodes associées au rôle de mineur dans une blockchain

### 15/03 :
- Veille & recherche sur les différentes fonctionnalités que l'ont pourrait ajouter au projet
- Ajout du fichier fabricant.py, ou dans ce fichier sera contenu chaque nouvelle voiture produite -> Clé publique : plaque d'immatriculation
- Ajout du vendeur.py, qui sera utilisé pour une transaction d'une voiture d'un vendeur, à un acheteur
### 29/03 :
- Ajout garage.py, peremettant de vérifier le kilométrage d'une voiture. (aléatoire pour la démo)
- Mise à jour global du dépot, avec description des fonctionnalités
### 12/03 : 
- Tentative d'ajout d'un fichier permettant de conserver l'historique d'une voiture. 
- Correction des bugs

