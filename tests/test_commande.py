from datetime import datetime
from fastapi.testclient import TestClient


def test_post_commande(client: TestClient):
    new_commande = {
        "c_date_commande": "2025-07-29T14:32:10.123000",
        "c_timbre_client": float(2.6),
        "c_timbre_commande": 2.6,
        "c_nombre_colis": 1,
        "c_cheque_client": 10.00,
        "c_commentaire": "je suis le commantaire de la commande, yo",
        "c_barchive": 0,
        "c_bstock": 0
    }
    print("HELO HELO HELO", new_commande["c_date_commande"])
    response = client.post("/commande/", json=new_commande)
    print(response)

    print("Status code:", response.status_code)
    print("Response JSON:", response.json())
    print("TROP BIEN  !!!")

    assert response.status_code == 201
    commande_created = response.json()

    assert commande_created['c_date_commande'] == new_commande['c_date_commande']
    assert commande_created['c_timbre_client'] == new_commande['c_timbre_client']
    assert commande_created['c_timbre_commande'] == new_commande['c_timbre_commande']
    assert commande_created['c_nombre_colis'] == new_commande['c_nombre_colis']
    assert commande_created['c_cheque_client'] == new_commande['c_cheque_client']
    assert commande_created['c_commentaire'] == new_commande['c_commentaire']
    assert commande_created['c_barchive'] == new_commande['c_barchive']
    assert commande_created['c_bstock'] == new_commande['c_bstock']


def test_post_commande_422(client: TestClient):
    new_commande = {
        "c_nombre_colis": "UN",
        "c_commentaire": "Nouveau commentaire ",
    }

    response = client.post("/commande/", json=new_commande)
    assert response.status_code == 422


def test_get_commande_by_id(client: TestClient):
    response = client.get("/commande/1")
    assert response.status_code == 200
    commande = response.json()


def test_get_all_commandes(client: TestClient):
    # on parle du client ordi
    response = client.get("/commande/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0


def test_patch_commande(client: TestClient):
    modified_commande = {
        "c_commentaire": "JSON TATANE !!!",
    }
    response = client.patch("/commande/2", json=modified_commande)

    assert response.status_code == 200
    commande_updated = response.json()
    assert commande_updated['c_commentaire'] == modified_commande['c_commentaire']


def test_delete_commande(client: TestClient):
    response = client.delete("/commande/1")
    assert response.status_code == 204
