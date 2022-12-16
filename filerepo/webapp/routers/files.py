import hashlib
from typing import List, Iterator, Tuple
from fastapi import File, UploadFile, status, APIRouter, Depends
from fastapi.responses import JSONResponse, Response
from sqlalchemy.orm.session import Session

from filerepo.webapp.schemas.DTO.file.file_get_request import FileGetRequest
from filerepo.webapp.schemas.DTO.file.file_info_response import FileInfoGetResponse
from filerepo.webapp.schemas.DTO.uploadActivity.upload_activity_get_model import UploadActivityGetModel
from filerepo.webapp.service.file_service import FileServiceImpl, FileService
from filerepo.webapp.repository.file.file_repository import FileRepositoryImpl

from filerepo.webapp.repository.uploadActivity.uploadActivity_repository import UploadActivityRepositoryImpl

from filerepo.webapp.repository.database import SessionLocal

router = APIRouter()


def get_session() -> Iterator[Session]:
    session: Session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


def fnc_file_service(session: Session = Depends(get_session)) -> FileService:
    repository: FileRepositoryImpl = FileRepositoryImpl(session)
    upload_repository: UploadActivityRepositoryImpl = UploadActivityRepositoryImpl(session)
    service: FileService = FileServiceImpl(repository, upload_repository)
    return service


@router.post("/files/upload", response_model=UploadActivityGetModel, tags=["files"])
def upload(file: UploadFile = File(...), file_service: FileService = Depends(fnc_file_service)):
    try:
        return file_service.upload_file(file)
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


@router.get("/files", response_model=List[FileGetRequest], status_code=status.HTTP_200_OK, tags=["files"])
def files(file_service: FileService = Depends(fnc_file_service)):
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


@router.delete("/files/{file_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["files"])
def delete_file(file_id: int, file_service: FileService = Depends(fnc_file_service)):
    try:
        file_service.delete(file_id)
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


@router.get("/files/{file_id}", status_code=status.HTTP_200_OK, tags=["files"])
def download_file(file_id: int, file_service: FileService = Depends(fnc_file_service)):
    try:
        file = file_service.download_by_id(file_id)
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


@router.get("/files/{file_id}/info", response_model=FileInfoGetResponse, tags=["files"])
def get_file_info(file_id: int, file_service: FileService = Depends(fnc_file_service)):
    try:
        return file_service.file_info_by_id(file_id)
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
