from typing import Union
from fastapi import File, UploadFile, status, APIRouter
from fastapi.responses import JSONResponse, FileResponse
import aiofiles
import filerepo.algorithms.get_file_data as getFileData
from ..schemas.schema import FileBase
from pathlib import Path
import json
import os

router = APIRouter()

@router.post("/files/upload", tags=["files"])
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


@router.get("/files", tags=["files"])
def files():
    try:
        files_json = json.dumps(os.listdir("/opt/repository/"))
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


@router.delete("/files/{filename}", tags=["files"])
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

@router.get("/files/{filename}", tags=["files"])
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


@router.get("/files/{filename}/info", response_model=FileBase, tags=["files"])
async def get_file_info(filename: str):
    try:
        if Path("/opt/repository/" + filename).is_file():
            file = getFileData.get_file_information("/opt/repository/" + filename)
            return JSONResponse(
                status_code=status.HTTP_200_OK,
                content=file.dict()
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