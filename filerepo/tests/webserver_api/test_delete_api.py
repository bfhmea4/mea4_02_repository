from fastapi.testclient import TestClient
from filerepo.webapp.webserver import app
import json
from datetime import date
import pytest

client = TestClient(app)
@pytest.mark.order(6)
def test_delete_nx_file():
    response = client.delete("/files/0")
    assert response.status_code == 400

@pytest.mark.order(7)
def test_file_deletion():
    filename = "test.file-" + str(date.today())
    response = json.loads(client.get("/files").content)
    file_id = response[0]['id']
    response = client.delete("/files/"+file_id)
    assert response.status_code == 204