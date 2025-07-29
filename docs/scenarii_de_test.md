# Scenarii de test :

## Client

### TC01 - Création client avec données valides

- **Préconditions** : Aucun client existant requis
- **Étapes** :
  1. Requête `POST /client/`
  2. Données :  
     ```json
     {
       "c_nom": "Bancal",
       "c_prenom": "Raphaël",
       "c_genre": "M"
     }
     ```
- **Résultat attendu** : HTTP 201, retour JSON contenant `c_id`, `c_nom`, `c_prenom`, `c_genre`
- **Résultat obtenu** : *(à remplir après exécution)*
- **Statut** : ✅ / ❌


### TC02 - Création client avec données invalides

- **Préconditions** : Aucun client existant requis
- **Étapes** :
  1. Requête `POST /client/`
  2. Données :  
     ```json
     {
       "c_nom": "Bancal",
       "c_genre": "M"
     }
     ```
- **Résultat attendu** : HTTP 422, " Un paramètre obligatoire n'est pas renseigné : [c_nom, c_prenom]"
- **Résultat obtenu** : *(à remplir après exécution)*
- **Statut** : ✅ / ❌


### TC03 - Récupération données client avec l'id

- **Préconditions** : Au moins 1 client existant requis
- **Étapes** :
  1. Requête `GET /client/1`

- **Résultat attendu** : HTTP 200, retour JSON contenant `c_id`, `c_nom`, `c_prenom`, `c_genre` pour tous les clients
- **Résultat obtenu** : *(à remplir après exécution)*
- **Statut** : ✅ / ❌


### TC04 - Récupération de toutes les données client

- **Préconditions** : Au moins 1 client existant requis
- **Étapes** :
  1. Requête `GET /client/`

- **Résultat attendu** : HTTP 200, retour JSON contenant `c_id`, `c_nom`, `c_prenom`, `c_genre`
- **Résultat obtenu** : *(à remplir après exécution)*
- **Statut** : ✅ / ❌


### TC05 - Modification des données client avec l'id

- **Préconditions** : Au moins 1 client existant requis
- **Étapes** :
  1. Requête `PATCH /client/1`
  2. Données :  
     ```json
     {
       "c_prenom": "Frederique",
       "c_genre": "F"
     }
     ```
- **Résultat attendu** : HTTP 200, retour JSON contenant `c_id`, `c_nom`, `c_prenom`, `c_genre`
- **Résultat obtenu** : *(à remplir après exécution)*
- **Statut** : ✅ / ❌


### TC06 - Suppression client avec l'id

- **Préconditions** : Au moins 1 client existant requis
- **Étapes** :
  1. Requête `DELETE /client/1`
  
- **Résultat attendu** : HTTP 200, "Le client a été supprimé"
- **Résultat obtenu** : *(à remplir après exécution)*
- **Statut** : ✅ / ❌



## Commandes

### TCO01 - Création commande avec données valides

- **Préconditions** : Aucune commande existante requis
- **Étapes** :
  1. Requête `POST /commande/`
  2. Données :  
     ```json
     {
       "c_date_commande": "2025-07-29T14:32:10.123000",
       "c_timbre_client": 2.6,
       "c_timbre_commande": 2.6,
       "c_nombre_colis": 1,
       "c_cheque_client": 10.00,
       "c_commentaire": "je suis le commentaire de la commande, yo",
       "c_barchive": 0,
       "c_bstock": 0
     }
     ```
- **Résultat attendu** : HTTP 201, retour JSON contenant `c_date_commande`, `c_timbre_client`, `c_timbre_commande`, `c_nombre_colis`, `c_cheque_client`, `c_commentaire`, `c_barchive`, `c_bstock`
- **Résultat obtenu** : *(à remplir après exécution)*
- **Statut** : ✅ / ❌


### TCO02 - Création commande avec données invalides

- **Préconditions** : Aucune commande existante requis
- **Étapes** :
  1. Requête `POST /commande/`
  2. Données :  
     ```json
     {
       "c_nombre_colis": "UN",
       "c_commentaire": "Nouveau commentaire "
     }
     ```
- **Résultat attendu** : HTTP 422
- **Résultat obtenu** : *(à remplir après exécution)*
- **Statut** : ✅ / ❌


### TCO03 - Récupération données commande avec l'id

- **Préconditions** : Au moins 1 commande existante requis
- **Étapes** :
  1. Requête `GET /commande/1`

- **Résultat attendu** : HTTP 200, retour JSON contenant `c_date_commande`, `c_timbre_client`, `c_timbre_commande`, `c_nombre_colis`, `c_cheque_client`, `c_commentaire`, `c_barchive`, `c_bstock`
- **Résultat obtenu** : *(à remplir après exécution)*
- **Statut** : ✅ / ❌


### TCO04 - Récupération de toutes les données commandes

- **Préconditions** : Au moins 1 commande existante requis
- **Étapes** :
  1. Requête `GET /commande/`

- **Résultat attendu** : HTTP 200, retour JSON contenant `c_date_commande`, `c_timbre_client`, `c_timbre_commande`, `c_nombre_colis`, `c_cheque_client`, `c_commentaire`, `c_barchive`, `c_bstock`
- **Résultat obtenu** : *(à remplir après exécution)*
- **Statut** : ✅ / ❌


### TCO05 - Modification des données commande avec l'id

- **Préconditions** : Au moins 1 commande existante requis
- **Étapes** :
  1. Requête `PATCH /commande/1`
  2. Données :  
     ```json
     {
       "c_commentaire": "JSON TATANE !!!"
     }
     ```
- **Résultat attendu** : HTTP 200, retour JSON contenant `c_date_commande`, `c_timbre_client`, `c_timbre_commande`, `c_nombre_colis`, `c_cheque_client`, `c_commentaire`, `c_barchive`, `c_bstock`
- **Résultat obtenu** : *(à remplir après exécution)*
- **Statut** : ✅ / ❌


### TCO06 - Suppression commande avec l'id

- **Préconditions** : Au moins 1 commande existante requis
- **Étapes** :
  1. Requête `DELETE /commande/1`
  
- **Résultat attendu** : HTTP 200, "La commande a été supprimée"
- **Résultat obtenu** : *(à remplir après exécution)*
- **Statut** : ✅ / ❌



## Utilisateur

### TU01 - Création utilisateur avec données valides

- **Préconditions** : Aucun utilisateur existant requis
- **Étapes** :
  1. Requête `POST /utilisateurs/`
  2. Données :  
     ```json
     {
       "u_nom": "Bancal",
       "u_prenom": "Raphaël",
       "u_username": "rbancal"
     }
     ```
- **Résultat attendu** : HTTP 201, retour JSON contenant `id`, `u_nom`, `u_prenom`, `u_username`
- **Résultat obtenu** : *(à remplir après exécution)*
- **Statut** : ✅ / ❌


### TU02 - Création utilisateur avec données invalides

- **Préconditions** : Aucun utilisateur existant requis
- **Étapes** :
  1. Requête `POST /utilisateurs/`
  2. Données :  
     ```json
     {
       "u_nom": "Durand",
       "u_prenom": "Paul"
     }
     ```
- **Résultat attendu** : HTTP 422, "Un paramètre obligatoire n'est pas renseigné: [u_username]"
- **Résultat obtenu** : *(à remplir après exécution)*
- **Statut** : ✅ / ❌


### TU03 - Récupération données utilisateur avec l'id

- **Préconditions** : Au moins 1 utilisateur existant requis
- **Étapes** :
  1. Requête `GET /utilisateurs/1`
  
- **Résultat attendu** : HTTP 200, retour JSON contenant `id`, `u_nom`, `u_prenom`, `u_username`
- **Résultat obtenu** : *(à remplir après exécution)*
- **Statut** : ✅ / ❌


### TU04 - Récupération de toutes les données utilisateur

- **Préconditions** : Au moins 1 utilisateur existant requis
- **Étapes** :
  1. Requête `GET /utilisateurs/`
  
- **Résultat attendu** : HTTP 200, retour JSON contenant `id`, `u_nom`, `u_prenom`, `u_username` pour tous les utilisateurs
- **Résultat obtenu** : *(à remplir après exécution)*
- **Statut** : ✅ / ❌


### TU05 - Modification des données utilisateur avec l'id

- **Préconditions** : Au moins 1 utilisateur existant requis
- **Étapes** :
  1. Requête `PATCH /utilisateurs/1`
  2. Données :  
     ```json
     {
       "u_prenom": "Barthelemy",
       "u_username": "Saint"
     }
     ```
- **Résultat attendu** : HTTP 200, retour JSON contenant `id`, `u_nom`, `u_prenom`, `u_username`
- **Résultat obtenu** : *(à remplir après exécution)*
- **Statut** : ✅ / ❌


### TU06 - Suppression utilisateur avec l'id

- **Préconditions** : Au moins 1 utilisateur existant requis
- **Étapes** :
  1. Requête `POST /utilisateurs/1`
  
- **Résultat attendu** : HTTP 200, "L'utilisateur a été supprimé"
- **Résultat obtenu** : *(à remplir après exécution)*
- **Statut** : ✅ / ❌
