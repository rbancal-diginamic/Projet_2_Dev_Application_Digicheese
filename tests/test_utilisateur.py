import pytest
from fastapi import Response
from fastapi.testclient import TestClient

from src.models.schemas.utilisateurs.utilisateur_post import UtilisateurPost


def test_post_utilisateur(client: TestClient):
    new_utilisateur = {
        "u_nom": "bancal",
        "u_prenom": "raphaël",
        "u_username": "rbancal"
    }
    response = client.post("/utilisateurs/", json=new_utilisateur)

    assert response.status_code == 201
    utilisateur_created = response.json()

    assert utilisateur_created['u_nom'] == new_utilisateur['u_nom'].upper()
    assert utilisateur_created['u_prenom'] == new_utilisateur['u_prenom'].capitalize()
    assert utilisateur_created['u_username'] == new_utilisateur['u_username'].lower()

# def test_post_client_422(client: TestClient):
#     new_client = {
#         "c_genre": "M",
#         "c_nom": "bancal"
#     }

#     response = client.post("/client/", json=new_client)
#     assert response.status_code == 422

def test_get_utilisateur_by_id(client: TestClient):
    response = client.get("/utilisateurs/2")
    assert response.status_code == 200
    data = response.json()
    assert data['u_username'] == "rbancal"
    assert data['u_nom'] == "BANCAL"
    assert data['u_prenom'] == "Raphaël"


def test_get_all_utilisateur(client: TestClient):
    response = client.get("/utilisateurs/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0


def test_patch_utilisateur(client: TestClient):
    modified_utilisateur = {
        "u_username": "Saint",
        "u_prenom": "Barthelemy"
    }
    response = client.patch("/utilisateurs/1", json=modified_utilisateur)

    assert response.status_code == 200
    utilisateur_updated = response.json()

    assert utilisateur_updated['u_username'] == modified_utilisateur['u_username']
    assert utilisateur_updated['u_prenom'] == modified_utilisateur['u_prenom']


def test_delete_utilisateur(client: TestClient):
    response = client.delete("/utilisateurs/1")
    assert response.status_code == 200