def test_list_activities(client):
    # Arrange
    # (client fixture provides FastAPI test client)

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert "Chess Club" in data
