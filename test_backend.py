import subprocess
import time
import pytest
import requests

@pytest.fixture(scope="module", autouse=True)
def backend_server():
    proc = subprocess.Popen(["python", "rest_app.py"])  # start backend
    time.sleep(1)  # give server time to start
    yield
    proc.terminate()
    proc.wait()

BASE_URL = "http://127.0.0.1:5000/users"


def test_create_user():
    url = f"{BASE_URL}/9999"
    resp = requests.post(url, json={"user_name": "pytest"})
    assert resp.status_code == 200
    data = resp.json()
    assert data["status"] == "ok"
    assert data["user_added"] == "pytest"


def test_get_user():
    url = f"{BASE_URL}/9999"
    resp = requests.get(url)
    assert resp.status_code == 200
    data = resp.json()
    assert data["status"] == "ok"


def test_update_user():
    url = f"{BASE_URL}/9999"
    resp = requests.put(url, json={"user_name": "updated"})
    assert resp.status_code == 200
    data = resp.json()
    assert data["status"] == "ok"
    assert data["user_name"] == "updated"


def test_delete_user():
    url = f"{BASE_URL}/9999"
    resp = requests.delete(url)
    assert resp.status_code == 200
    data = resp.json()
    assert data["status"] == "ok"
    assert data["user_deleted"] == "9999"
