from typing import List, Iterator
from fastapi import File, UploadFile, status, APIRouter, Depends
from fastapi.responses import JSONResponse, Response
from sqlalchemy.orm.session import Session

from filerepo.webapp.domain.uploadActivity.uploadActivity_repository import UploadActivityRepository
from filerepo.webapp.schemas.DTO.uploadActivity.upload_activity_get_model import UploadActivityGetModel

from filerepo.webapp.repository.uploadActivity.uploadActivity_repository import UploadActivityRepositoryImpl
from filerepo.webapp.service.uploadActivity_service import UploadActivityServiceImpl

from filerepo.webapp.repository.database import SessionLocal

router = APIRouter()


def get_session() -> Iterator[Session]:
    session: Session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


def fnc_upload_activity_repository(session: Session = Depends(get_session)) -> UploadActivityRepository:
    repository: UploadActivityRepositoryImpl = UploadActivityRepositoryImpl(session)
    return repository


@router.get("/history/{file_id}", response_model=List[UploadActivityGetModel], status_code=status.HTTP_200_OK,
            tags=["upload_ctivity"])
def get_history_by_id(file_id: int,
                      upload_activity_repository: UploadActivityRepositoryImpl = Depends(fnc_upload_activity_repository)):
    try:
        upload_activity_service = UploadActivityServiceImpl(upload_activity_repository)
        return upload_activity_service.find_upload_activity_by_file_id(file_id)
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


@router.get("/uploadactivities", response_model=List[UploadActivityGetModel], status_code=status.HTTP_200_OK, tags=["upload_ctivity"])
def get_history(upload_activity_repository: UploadActivityRepositoryImpl = Depends(fnc_upload_activity_repository)):
    try:
        upload_activity_service = UploadActivityServiceImpl(upload_activity_repository)
        return upload_activity_service.find_all()
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

