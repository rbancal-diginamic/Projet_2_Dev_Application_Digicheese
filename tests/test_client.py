from fastapi import Response
from fastapi.testclient import TestClient

from src.models.schemas.clients.client_post import ClientPost


def test_get_all_clients(client: TestClient):
    response = client.get("/client/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0

def test_post_clients(client: TestClient):
    new_client = {
        "c_genre": "M",
        "c_nom": "bancal",
        "c_prenom": "raphaël"
    }
    response: Response = client.post("/client/", json=new_client)
    assert response.status_code == 201
    created_client = response.json()
    assert created_client['c_genre'] == new_client['c_genre']
    assert created_client['c_nom'] == new_client['c_nom'].upper()
    assert created_client['c_prenom'] == new_client['c_prenom'].capitalize()