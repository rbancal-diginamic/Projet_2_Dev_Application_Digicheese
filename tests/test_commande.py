from fastapi.testcommande import TestCommande
from models.schemas.commandes.commande_post import CommandePost


def test_get_all_commandes(commande: TestCommande):
    '''Test de la récupération de toutes les commandes'''
    response = commande.get("/commande/")
    assert response.json()['detail'] == []
    assert response.status_code == 200

def test_get_commande_by_id(id: TestCommande, commande : TestCommande):
    '''Test de la récupération d'une commande via son id'''
    response = commande.get("/commande/{id}")
    assert response.json()['detail'] == []
    assert response.status_code == 200

def test_create_commande(commande: TestCommande ):
    '''Test de la création de la commande'''
    new_commande = CommandePost({
        "c_datcdee": "2025-03-01",
        "c_timbre_client": "2.6",
        
    })
    response = commande.post("/commande/")
    assert response.json()['detail'] == []
    assert response.status_code == 200

def test_patch_commande():
    pass

def test_delete_commande():
    pass
