from fastapi.testclient import TestClient
from filerepo.webapp.webserver import app
from datetime import date
import json

import pytest

client = TestClient(app)
@pytest.mark.order(4)
def test_download_file():
    response = json.loads(client.get("/files").content)
    file_id = str(response[0]['id'])
    response = client.get("/files/"+file_id)

    assert response.status_code == 200
    assert response.headers['content-type']