from fastapi.testclient import TestClient
from filerepo.webapp.webserver import app
from datetime import date
import filerepo.algorithms.get_file_data as getFileData
import json

import pytest

client = TestClient(app)


@pytest.mark.order(5)
def test_get_file_info():
    filename = "test.file-" + str(date.today())
    response = client.get("/files/" + filename + "/info")
    file_info_correct = getFileData.get_file_information("/opt/repository/" + filename)
    file_info = json.loads(response.content)
    assert response.status_code == 200
    assert file_info['file Infos'] == file_info_correct
