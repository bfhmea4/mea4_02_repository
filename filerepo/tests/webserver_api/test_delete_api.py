from fastapi.testclient import TestClient
from filerepo.webapp.webserver import app
import io
from datetime import date
from pathlib import Path
import pytest

client = TestClient(app)
@pytest.mark.order(6)
def test_delete_nx_file():
    response = client.delete("/files/test")
    assert response.status_code == 404

@pytest.mark.order(7)
def test_file_deletion():
    filename = "test.file-" + str(date.today())
    response = client.delete("/files/"+filename)
    assert response.status_code == 200
    assert Path("/opt/repository/"+filename).is_file() == False