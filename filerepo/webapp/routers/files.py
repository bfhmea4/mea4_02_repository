from typing import Union
from fastapi import File, UploadFile, status, APIRouter
from fastapi.responses import JSONResponse, FileResponse
import aiofiles
import filerepo.algorithms.get_file_data as getFileData

from ..schemas.file_schema import FileGetModel, FileUploadModel, FileDownloadModel, FileListModel
from ..service.file_service import FileServiceImpl
from ..database.file.file_repository import FileRepositoryImpl
from ..database.file_system import FileSystem

import json

router = APIRouter()
file_system = FileSystem()
file_repository = FileRepositoryImpl(file_system)
file_service = FileServiceImpl(file_repository)


@router.post("/files/upload", response_model=FileGetModel ,tags=["files"])
async def upload(file: UploadFile = File(...)):
    try:

        file_service.create(FileUploadModel())

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