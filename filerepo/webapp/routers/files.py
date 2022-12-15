import hashlib
from typing import List, Iterator, Tuple
from fastapi import File, UploadFile, status, APIRouter, Depends
from fastapi.responses import JSONResponse, Response
from sqlalchemy.orm.session import Session

from filerepo.webapp.domain.uploadActivity.uploadActivity_repository import UploadActivityRepository
from filerepo.webapp.routers.upload_activity import get_session
from filerepo.webapp.schemas.DTO.file_get_model import FileGetModel
from filerepo.webapp.schemas.DTO.file_upload_model import FileUploadModel
from filerepo.webapp.schemas.DTO.file_info_model import FileInfoGetModel
from filerepo.webapp.service.file_service import FileServiceImpl, FileService
from filerepo.webapp.repository.file.file_repository import FileRepositoryImpl
from filerepo.webapp.domain.file.file_repository import FileRepository

from filerepo.webapp.repository.uploadActivity.uploadActivity_repository import UploadActivityRepositoryImpl
from filerepo.webapp.service.uploadActivity_service import UploadActivityServiceImpl, UploadActivityService
from filerepo.webapp.schemas.DTO.uploadActivity.upload_activity_create_model import UploadActivityCreateModel

from filerepo.webapp.repository.database import SessionLocal

router = APIRouter()


def generator() -> Iterator[Session]:
    session: Session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


#def fnc_file_repository(session: Session = Depends(get_session)) -> tuple[FileServiceImpl, UploadActivityServiceImpl]:
    #    repository: FileRepositoryImpl = FileRepositoryImpl(session)
    #    upload_repository: UploadActivityRepositoryImpl = UploadActivityRepositoryImpl(session)
    #   service: FileServiceImpl = FileServiceImpl(repository)
    #   upload_activity_service: UploadActivityServiceImpl = UploadActivityServiceImpl(upload_repository)
#   return service, upload_activity_service


def fnc_file_repository(session: Session = Depends(get_session)) -> FileService:
    repository: FileRepositoryImpl = FileRepositoryImpl(session)
    upload_repository: UploadActivityRepositoryImpl = UploadActivityRepositoryImpl(session)
    upload_activity_service: UploadActivityServiceImpl = UploadActivityServiceImpl(upload_repository)
    service: FileService = FileServiceImpl(repository, upload_repository)
    return service


# Use FileSystem to write blob data to file system separate from meta data
# This functionality can be migrated into the file repository later on ToDo: Split file and blobData to store blob on FS
# file_system = FileSystem()
# file_repository = FileRepositoryImpl(file_system)
# file_service = FileServiceImpl(file_repository)

@router.post("/files/upload", response_model=FileGetModel, tags=["files"])
def upload(file: UploadFile = File(...), file_service: FileService = Depends(fnc_file_repository)):
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


@router.get("/files", response_model=List[FileGetModel], status_code=status.HTTP_200_OK, tags=["files"])
def files(file_repository: FileRepositoryImpl = Depends(fnc_file_repository)):
    try:
        file_service = FileServiceImpl(file_repository)
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
def delete_file(file_id: int, file_repository: FileRepositoryImpl = Depends(fnc_file_repository)):
    try:
        file_service = FileServiceImpl(file_repository)
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
def download_file(file_id: int, file_repository: FileRepositoryImpl = Depends(fnc_file_repository)):
    try:
        file_service = FileServiceImpl(file_repository)
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


@router.get("/files/{file_id}/info", response_model=FileInfoGetModel, tags=["files"])
def get_file_info(file_id: int, file_repository: FileRepositoryImpl = Depends(fnc_file_repository)):
    try:
        file_service = FileServiceImpl(file_repository)
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
