from typing import List
from fastapi import File, UploadFile, status, APIRouter
from fastapi.responses import JSONResponse, Response


from filerepo.webapp.schemas.DTO.file_get_model import FileGetModel
from filerepo.webapp.schemas.DTO.file_upload_model import FileUploadModel
from filerepo.webapp.schemas.DTO.file_info_model import FileInfoGetModel
from filerepo.webapp.service.file_service import FileServiceImpl
from filerepo.webapp.repository.file.file_repository import FileRepositoryImpl
from filerepo.webapp.repository.file_system import FileSystem



router = APIRouter()
file_system = FileSystem()
file_repository = FileRepositoryImpl(file_system)
file_service = FileServiceImpl(file_repository)


@router.post("/files/upload", response_model=FileGetModel ,tags=["files"])
async def upload(file: UploadFile = File(...)):
    try:
        uploaded_file = {
                        "file_name":file.filename,
                        "file_type":file.content_type,
                        "file_content": file.file.read()
                         }
        return file_service.create(FileUploadModel(**uploaded_file))

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


@router.get("/files", response_model=List[FileGetModel], status_code=status.HTTP_200_OK, tags=["files"])
def files():
    try:
        return file_service.find_all()
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

@router.delete("/files/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=["files"])
def delete_file(id: str):
    try:
        file_service.delete(id)
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


@router.get("/files/{id}",status_code=status.HTTP_200_OK, tags=["files"])
def download_file(id: str):
    try:
        file = file_service.download_by_id(id)
        return Response(file.file_content, media_type=file.file_type)
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



@router.get("/files/{id}/info", response_model=FileInfoGetModel, tags=["files"])
def get_file_info(id: str):
    try:
        return file_service.file_info_by_id(id)
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