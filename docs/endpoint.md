## Client
- POST '/client'            -> Crée un nouveau client dans la base de données.
- POST '/client_422'        -> Soulève une erreur 422 (champ obligatoire manquant), et bloque la création.
- GET '/client/{id}'        -> Récupère le client par id dans la base de données.
- GET '/clients'            -> Récupère l'ensemble des clients dans la base de données.
- PATCH '/client/{id}'      -> Permet la modification du client par id dans la base de données.
- DELETE '/client/{id}'     -> Permet la suppression du client par id dans la base de données.

## Commande
- POST '/commande'          -> Crée une nouvelle commande dans la base de données.
- POST '/commande_422'      -> Soulève une erreur 422 (champ obligatoire manquant), et bloque la création.
- GET '/commande/{id}'      -> Récupère la commande par id dans la base de données.
- GET '/commandes'          -> Récupère l'ensemble des commandes dans la base de données.
- PATCH '/commande/{id}'    -> Permet la modification de la commande par id dans la base de données.
- DELETE '/commande/{id}'   -> Permet la suppression de la commande par id dans la base de données.

## Utilisateur
- POST '/utilisateur'       -> Crée un nouvel utilisateur dans la base de données.
- POST '/utilisateur_422'   -> Soulève une erreur 422 (champ obligatoire manquant), et bloque la création.
- GET '/utilisateur/{id}'   -> Récupère l'utilisateur par id dans la base de données.
- GET '/utilisateurs'       -> Récupère l'ensemble des utilisateurs dans la base de données.
- PATCH '/utilisateur/{id}' -> Permet la modification de l'utilisateur par id dans la base de données.
- DELETE '/utilisateur/{id}'-> Permet la suppression de l'utilisateur par id dans la base de données.


## Global POST HTTP CODE
| Code | Signification             | Exemple de contenu   |
| ---- | ------------------------- | -------------------- |
| 200  | OK (réponse normale)      | JSON avec données    |
| 201  | Created (ressource créée) | ID ou données créées |
| 422  | Unprocessable Entity      | Erreur de validation |
| 500  | Server Error              | Problème inattendu   |


## Global GET HTTP CODE
| Code | Signification             | Exemple de contenu   |
| ---- | ------------------------- | -------------------- |
| 200  | OK (réponse normale)      | JSON avec données    |
| 404  | Not Found                 | Objet non trouvé     |
| 500  | Server Error              | Problème inattendu   |


## Global PATCH HTTP CODE
| Code | Signification             | Exemple de contenu   |
| ---- | ------------------------- | -------------------- |
| 200  | OK (réponse normale)      | JSON avec données    |
| 422  | Unprocessable Entity      | Erreur de validation |
| 500  | Server Error              | Problème inattendu   |


## Global DELETE HTTP CODE
| Code | Signification             | Exemple de contenu   |
| ---- | ------------------------- | -------------------- |
| 200  | OK (réponse normale)      | JSON avec données    |
| 404  | Not Found                 | Objet non trouvé     |
| 500  | Server Error              | Problème inattendu   |
