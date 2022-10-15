from fastapi.testclient import TestClient
from filerepo.webapp.webserver import app
from datetime import date
import json

import pytest

client = TestClient(app)
@pytest.mark.order(4)
def test_download_file():
    filename = "test.file-" + str(date.today())
    response = client.get("/files/"+filename)

    assert response.status_code == 200
    assert response.headers['content-type']