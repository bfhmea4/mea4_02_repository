from fastapi.testclient import TestClient
from filerepo.webapp.webserver import app
import io
from datetime import date
from pathlib import Path
import json

import pytest

client = TestClient(app)
@pytest.mark.order(8)
def test_get_empty(): 
    response = client.get("/files")
    files = json.loads(response.content)
    assert response.status_code == 200
    assert len(files) == 0

@pytest.mark.order(3)
def test_get_files():
    filename = "test.file-" + str(date.today())

    response = client.get("/files")
    files = json.loads(response.content)
    assert response.status_code == 200
    assert filename == files[0]['file_name']
