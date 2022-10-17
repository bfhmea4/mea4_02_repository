from typing import Union
from fastapi import FastAPI, File, UploadFile, status
from fastapi.responses import JSONResponse, FileResponse
import aiofiles
import filerepo.algorithms.fizzbuzz as fizzbuzz
import filerepo.algorithms.get_file_data as getFileData
import uvicorn
from pathlib import Path
import json
import os

app = FastAPI()

Path("/opt/repository").mkdir(parents=True, exist_ok=True)


def run():
    uvicorn.run("filerepo.webapp.webserver:app", port=8000, log_level="debug")


@app.get("/fizzbuzz/{number}")
def read_item(number: int):
    return {"output": fizzbuzz.fizzbuzz(number)}


@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    try:
        async with aiofiles.open("/opt/repository/" + file.filename, 'wb') as out_file:
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


@app.get("/files")
def files():
    try:
        files_json = json.dumps(os.listdir("C:/Users/naeby/Documents/BFH/Project1"))
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={"files": files_json}
        )

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


@app.delete("/files/{filename}", status_code=204)
def delete_file(filename: str):
    try:
        Path("/opt/repository/" + filename).unlink()
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

@app.get("/files/{filename}", status_code=200)
async def download_file(filename: str):
    try:
        if Path("/opt/repository/"+filename).is_file():
            return FileResponse("/opt/repository/"+filename, media_type='application/octet-stream',filename=filename)
        else:
            raise FileNotFoundError
    except FileNotFoundError as e:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={'message': "FileNotFound"}
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

@app.get("/files/{filename}", status_code=200)
async def download_file(filename: str):
    try:
        if Path("C:/Users/naeby/Documents/BFH/Project1/" + filename).is_file():
            return FileResponse("C:/Users/naeby/Documents/BFH/Project1/" + filename,
                                media_type='application/octet-stream', filename=filename)
        else:
            raise FileNotFoundError
    except FileNotFoundError as e:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={'message': "FileNotFound"}
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


@app.get("/files/{filename}/info", status_code=200)
async def get_file_info(filename: str):
    try:
        if Path("C:/Users/naeby/Documents/BFH/Project1/" + filename).is_file():
            file_json = getFileData.get_file_informations("C:/Users/naeby/Documents/BFH/Project1/" + filename)
            return JSONResponse(
                status_code=status.HTTP_200_OK,
                content={"file Infos": file_json}
            )
        else:
            raise FileNotFoundError
    except FileNotFoundError as e:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={'message': "FileNotFound"}
        )
    except Exception as e:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={'message': str(e)}
        )
    else:
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={"files": file_json}
        )


# Kann man auch auf Command Line machen
if __name__ == "__main__":
    run()
