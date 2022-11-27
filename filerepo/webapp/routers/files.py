import hashlib
from typing import List, Iterator
from fastapi import File, UploadFile, status, APIRouter, Depends
from fastapi.responses import JSONResponse, Response
import traceback
from sqlalchemy.orm.session import Session

from filerepo.webapp.domain.uploadActivity.uploadActivity_repository import UploadActivityRepository
from filerepo.webapp.schemas.DTO.file_get_model import FileGetModel
from filerepo.webapp.schemas.DTO.file_upload_model import FileUploadModel
from filerepo.webapp.schemas.DTO.file_info_model import FileInfoGetModel
from filerepo.webapp.service.file_service import FileServiceImpl
from filerepo.webapp.repository.file.file_repository import FileRepositoryImpl
from filerepo.webapp.repository.file_system import FileSystem

from filerepo.webapp.repository.uploadActivity.uploadActivity_repository import UploadActivityRepositoryImpl
from filerepo.webapp.service.uploadActivity_service import UploadActivityServiceImpl
from filerepo.webapp.schemas.DTO.uploadActivity.upload_activity_create_model import UploadActivityCreateModel

from filerepo.webapp.repository.database import SessionLocal

router = APIRouter()


def get_session() -> Iterator[Session]:
    session: Session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


def upload_activity_repository(session: Session = Depends(get_session)) -> UploadActivityRepository:
    repository: UploadActivityRepositoryImpl = UploadActivityRepositoryImpl(session)
    return repository


file_system = FileSystem()
file_repository = FileRepositoryImpl(file_system)
file_service = FileServiceImpl(file_repository)
#upload_activity_repository = upload_activity_repository()
#upload_activity_service = UploadActivityServiceImpl(upload_activity_repository)


@router.post("/files/upload", response_model=FileGetModel, tags=["files"])
def upload(file: UploadFile = File(...), upload_activity_repository: UploadActivityRepositoryImpl = Depends(upload_activity_repository)):
    try:
        upload_activity_service = UploadActivityServiceImpl(upload_activity_repository)
        uploaded_file = {
            "file_name": file.filename,
            "file_type": file.content_type,
            "file_content": file.file.read()
        }
        hash = hashlib.sha256(uploaded_file['file_content']).hexdigest()
        id: str = file_service.get_file_id_by_hash(hash)
        if(id != None):
            upload_activity = {
                "file_name": uploaded_file['file_name'],
                "file_id": id
            }
            upload_activity_result = upload_activity_service.create(UploadActivityCreateModel(**upload_activity))
            return upload_activity_service.find_by_id(upload_activity_result.id)
        else:
            file_get_model = file_service.create(FileUploadModel(**uploaded_file))
            upload_activity = {
                "file_name": file_get_model.file_name,
                "file_id": file_get_model.id
            }
            upload_activity_service.create(UploadActivityCreateModel(**upload_activity))
        return file_get_model

    except FileNotFoundError as e:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={'message': str(e)}
        )
    except Exception as e:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={'message': str(traceback.print_exec())}

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


@router.get("/files/{id}", status_code=status.HTTP_200_OK, tags=["files"])
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
