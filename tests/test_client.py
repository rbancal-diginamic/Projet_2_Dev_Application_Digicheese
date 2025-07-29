import pytest
from fastapi import Response
from fastapi.testclient import TestClient

from src.models.schemas.clients.client_post import ClientPost


def test_get_all_clients(client: TestClient):
    response = client.get("/client/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0


def test_post_client(client: TestClient):
    new_client = {
        "c_genre": "M",
        "c_nom": "bancal",
        "c_prenom": "raphaël"
    }
    response = client.post("/client/", json=new_client)
    print(response)

    print("Status code:", response.status_code)
    print("Response JSON:", response.json())
    print("JE NE COMPRENDS PLUS RIEN !!!")

    assert response.status_code == 201
    client_created = response.json()

    assert client_created['c_genre'] == new_client['c_genre']
    assert client_created['c_nom'] == new_client['c_nom'].upper()
    assert client_created['c_prenom'] == new_client['c_prenom'].capitalize()

def test_post_client_422(client: TestClient):
    new_client = {
        "c_genre": "M",
        "c_nom": "bancal"
    }

    response = client.post("/client/", json=new_client)
    assert response.status_code == 422
