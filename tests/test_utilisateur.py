import pytest
from fastapi import Response
from fastapi.testclient import TestClient

from src.models.schemas.utilisateurs.utilisateur_post import UtilisateurPost


def test_get_all_utilisateur(client: TestClient):
    response = client.get("/utilisateurs/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0


def test_post_utilisateur(client: TestClient):
    new_utilisateur = {
        "u_nom": "bancal",
        "u_prenom": "raphaël",
        "u_username": "Admin"
    }
    response = client.post("/utilisateurs/", json=new_utilisateur)
    print(response)

    print("Status code:", response.status_code)
    print("Response JSON:", response.json())

    assert response.status_code == 201
    utilisateur_created = response.json()

    # assert utilisateur_created['c_genre'] == new_utilisateur['c_genre']
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
