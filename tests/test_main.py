from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_cronjob():
    response = client.post(
        "/cronjobs/",
        json={"cron_expression": "0 12 * * *", "name": "daily_backup", "utility": "avisame", "llm": "ollama/some_model"}
    )
    assert response.status_code == 200
    assert response.json()["name"] == "daily_backup"

def test_read_cronjobs():
    response = client.get("/cronjobs/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_delete_cronjob():
    response = client.post(
        "/cronjobs/",
        json={"cron_expression": "0 12 * * *", "name": "daily_cleanup", "utility": "revisa", "llm": "ollama/another_model"}
    )
    cronjob_id = response.json()["id"]
    delete_response = client.delete(f"/cronjobs/{cronjob_id}")
    assert delete_response.status_code == 200
