from typing import Union
from fastapi import FastAPI, File, UploadFile, status
from fastapi.responses import JSONResponse
import filerepo.algorithms.fizzbuzz as fizzbuzz
import uvicorn
from pathlib import Path

app = FastAPI()

def run():
    uvicorn.run("filerepo.webapp.webserver:app", port=8000, log_level="debug")

@app.get("/{number}")
def read_item(number: int):
    return {"output": fizzbuzz.fizzbuzz(number)}

@app.delete("/files/{filename}", status_code=204)
def delete_file(filename: str):
    try:
        Path("/opt/repository/"+filename).unlink()
    except FileNotFoundError as e:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={'message': str(e)}
            )
    except Exception as e:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={'message': str(e)}
            )
    else:
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={"result": 'success'}
        )


#Kann man auch auf Command Line machen
if __name__ == "__main__":
    run()