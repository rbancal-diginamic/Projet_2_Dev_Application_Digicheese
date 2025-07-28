from fastapi.testclient import TestClient
from src.models.schemas.commandes import commande_post


def test_get_all_commandes(commande: TestClient):
    '''Test de la récupération de toutes les commandes'''
    response = commande.get("/commande/")
    assert response.json()['detail'] == []
    assert response.status_code == 200

def test_get_commande_by_id(id: TestClient, commande : TestClient):
    '''Test de la récupération d'une commande via son id'''
    response = commande.get("/commande/{id}")
    assert response.json()['detail'] == []
    assert response.status_code == 200

def test_create_commande(commande: TestClient ):
    '''Test de la création de la commande'''
    new_commande = commande_post.CommandePost({
        "date_commande": 2025-3-1,
        "timbre_client": 2.6,
        "timbre_commande": 2.6,
        "nombre_colis": 1,
        "cheque_client" : 10.00,
        "commentaire": "je suis le commantaire de la commande, yo",
        "barchive": 0,
        "bstock" : 0
        
    })
    response = commande.post("/commande/", new_commande)
    assert response._content == new_commande.model_dump_json()
    assert response.status_code == 201

def test_patch_commande():
    pass

def test_delete_commande():
    pass
