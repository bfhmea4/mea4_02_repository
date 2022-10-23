from fastapi.testclient import TestClient
from filerepo.webapp.webserver import app
import io
from datetime import date
from pathlib import Path
import pytest

client = TestClient(app)
@pytest.mark.order(1)
def test_emtpy_file_upload():
    response = client.post("/files/upload", files={"file":None})
    assert response.status_code == 400
@pytest.mark.order(2)
def test_file_upload():
    file = io.BytesIO(bytes(str("Test file"),'utf-8'))
    response = client.post("/files/upload", files={"file":("test.file-" + str(date.today()),file,"text/plain")})
    file.close()
    assert response.status_code == 200
