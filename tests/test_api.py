from app.api import app

def test_success():
    client = app.test_client()
    response = client.post('/reservations', json={
        "room": "A",
        "time": "14:00"
    })
    assert response.status_code == 201
def test_failure():
    client = app.test_client()
    client.post('/reservations', json={
        "room": "A",
        "time": "10:00"
    })
    response = client.post('/reservations', json={
        "room": "A",
        "time": "10:00"
    })
    assert response.status_code == 409
    assert response.json['message'] == "Room is not available"