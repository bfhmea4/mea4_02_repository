from fastapi.testclient import TestClient
from filerepo.webapp.webserver import app
import io
from datetime import date
from pathlib import Path

client = TestClient(app)

def test_emtpy_file_upload():
    response = client.post("/upload", files={"file":None})
    assert response.status_code == 400

def test_file_upload():
    file = io.BytesIO(bytes(str("Test file"),'utf-8'))
    response = client.post("/upload", files={"file":("test.file-" + str(date.today()),file,"multipart/form-data")})
    file.close()
    assert response.status_code == 200
    assert Path("/opt/repository/test.file-"+str(date.today())).is_file() == True
