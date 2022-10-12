from typing import Union
from fastapi import FastAPI, File, UploadFile, status
from fastapi.responses import JSONResponse
import aiofiles
import filerepo.algorithms.fizzbuzz as fizzbuzz
import uvicorn
from pathlib import Path

app = FastAPI()

Path("/opt/repository").mkdir(parents=True, exist_ok=True)

def run():
    uvicorn.run("filerepo.webapp.webserver:app", port=8000, log_level="debug")

@app.get("/{number}")
def read_item(number: int):
    return {"output": fizzbuzz.fizzbuzz(number)}

@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    try:
        async with aiofiles.open("/opt/repository/"+file.filename, 'wb') as out_file:
            content = await file.read()  # async read
            await out_file.write(content)  # async write

    except FileNotFoundError as e:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={'message': str(e)}
            )
    except Exception as e:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
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