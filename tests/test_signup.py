def test_signup_for_activity(client):
    # Arrange
    activity = "Chess Club"
    email = "newstudent@mergington.edu"

    # Act
    response = client.post(f"/activities/{activity}/signup?email={email}")

    # Assert
    assert response.status_code == 200
    data = response.json()
    assert "Signed up" in data["message"]
    # Confirm participant added
    get_resp = client.get("/activities")
    participants = get_resp.json()[activity]["participants"]
    assert email in participants


def test_signup_duplicate(client):
    # Arrange
    activity = "Chess Club"
    email = "daniel@mergington.edu"  # Already registered

    # Act
    response = client.post(f"/activities/{activity}/signup?email={email}")

    # Assert
    assert response.status_code == 400
    data = response.json()
    assert "already signed up" in data["detail"]
