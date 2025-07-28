from fastapi.testclient import TestClient


def test_get_all_clients(client: TestClient):
    response = client.get("/client/")
    assert response.json()['detail'] == []
    assert response.status_code == 200

