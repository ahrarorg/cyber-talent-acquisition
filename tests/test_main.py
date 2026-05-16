import pytest
from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "Recruitment Protocol Initialized" in response.json()["message"]

def test_get_work_roles():
    response = client.get("/work-roles")
    assert response.status_code == 200
    assert len(response.json()) > 0
    assert response.json()[0]["id"] == "OPM-541"

def test_create_mission():
    payload = {
        "codename": "OPERATION_X",
        "work_role_id": "OPM-541",
        "objective": "Compromise target network"
    }
    response = client.post("/missions", json=payload)
    assert response.status_code == 200
    assert response.json()["codename"] == "OPERATION_X"

def test_register_operative():
    payload = {
        "alias": "ZeroCool",
        "email": "zero@hacker.net"
    }
    response = client.post("/operatives", json=payload)
    assert response.status_code == 200
    assert response.json()["alias"] == "ZeroCool"
