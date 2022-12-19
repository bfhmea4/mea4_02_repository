import io
import json
from datetime import date

import pytest
from starlette.testclient import TestClient

from filerepo.webapp.webserver import app

client = TestClient(app)


@pytest.fixture
def starter():
    file = io.BytesIO(bytes(str("Test file"), 'utf-8'))
    response = client.post("/files/upload", files={"file": ("test.file-" + str(date.today()), file, "text/plain")})
    file.close()
    return response


def test_upload(starter):
    assert starter.status_code == 200


def test_get_file(starter):
    filename = "test.file-" + str(date.today())

    response = client.get("/files")
    files = json.loads(response.content)
    assert response.status_code == 200
    assert filename == files[0]['file_name']
    assert response.status_code == 200
    assert len(files) == 0


def test_fileinfo(starter):
    filename = "test.file-" + str(date.today())
    response = json.loads(client.get("/files").content)
    file_id = str(response[0]['id'])
    response = client.get("/files/" + file_id + "/info")
    file_info = json.loads(response.content)
    assert response.status_code == 200
    assert file_info['file_name'] == filename
    assert file_info['file_type'] == "text/plain"


def test_download_file(starter):
    response = json.loads(client.get("/files").content)
    file_id = str(response[0]['id'])
    response = client.get("/files/" + file_id)

    assert response.status_code == 200
    assert response.headers['content-type']

