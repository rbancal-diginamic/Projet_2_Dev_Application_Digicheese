from fastapi.testclient import TestClient


def test_post_client(client: TestClient):
    new_client = {
        "c_genre": "M",
        "c_nom": "bancal",
        "c_prenom": "raphaël"
    }
    response = client.post("/client/", json=new_client)

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


def test_get_client_by_id(client: TestClient):
    response = client.get("/client/2")
    assert response.status_code == 200
    data = response.json()
    assert data['c_genre'] == "M"
    assert data['c_nom'] == "BANCAL"
    assert data['c_prenom'] == "Raphaël"


def test_get_all_clients(client: TestClient):
    response = client.get("/client/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0


def test_patch_client(client: TestClient):
    modified_client = {
        "c_genre": "Mme",
        "c_prenom": "Frédérique"
    }
    response = client.patch("/client/2", json=modified_client)

    assert response.status_code == 200
    client_updated = response.json()

    assert client_updated['c_genre'] == modified_client['c_genre']
    assert client_updated['c_prenom'] == modified_client['c_prenom']


def test_delete_client(client: TestClient):
    response = client.delete("/client/1")
    assert response.status_code == 204
