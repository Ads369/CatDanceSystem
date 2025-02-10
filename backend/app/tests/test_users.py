def test_create_user(client):
    response = client.post(
        "/users/",
        json={"name": "Test User", "description": "Test Description"},
    )
    assert response.status_code == 200
    assert response.json()["name"] == "Test User"


def test_get_user(client):
    response = client.post(
        "/users/",
        json={"name": "Test User", "description": "Test Description"},
    )
    user_id = response.json()["id"]
    response = client.get(f"/users/{user_id}")
    assert response.status_code == 200
    assert response.json()["name"] == "Test User"


def test_update_user(client):
    response = client.post(
        "/users/",
        json={"name": "Test User", "description": "Test Description"},
    )
    user_id = response.json()["id"]
    response = client.put(
        f"/users/{user_id}", json={"name": "Updated User"}
    )
    assert response.status_code == 200
    assert response.json()["name"] == "Updated User"


def test_delete_user(client):
    response = client.post(
        "/users/",
        json={"name": "Test User", "description": "Test Description"},
    )
    user_id = response.json()["id"]
    response = client.delete(f"/users/{user_id}")
    assert response.status_code == 200
    assert response.json()["message"] == "User deleted"
