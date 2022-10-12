from fastapi.testclient import TestClient
from filerepo.webapp.webserver import app
import io
from datetime import date
from pathlib import Path
import json

client = TestClient(app)

def test_get_empty(): 
    response = client.get("/files")
    files = json.loads(response.content)
    assert response.status_code == 200
    assert len(json.loads(files['files'])) == 0


def test_get_files():
    filename = "test.file-" + str(date.today())
    file = io.BytesIO(bytes(str("Test file"),'utf-8'))
    client.post("/upload", files={"file":(filename,file,"multipart/form-data")})
    file.close()

    response = client.get("/files")
    files = json.loads(response.content)
    assert response.status_code == 200
    assert (filename in files['files']) == True