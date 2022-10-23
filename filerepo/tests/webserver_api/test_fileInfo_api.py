from fastapi.testclient import TestClient
from filerepo.webapp.webserver import app
from datetime import date
import json

import pytest

client = TestClient(app)


@pytest.mark.order(5)
def test_get_file_info():
    filename = "test.file-" + str(date.today())
    response = json.loads(client.get("/files").content)
    file_id = response[0]['id']
    response = client.get("/files/" + file_id + "/info")
    file_info = json.loads(response.content)
    assert response.status_code == 200
    assert file_info['file_name'] == filename
    assert file_info['file_type'] == "text/plain"
