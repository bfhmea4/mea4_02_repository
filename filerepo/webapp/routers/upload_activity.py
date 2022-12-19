from typing import List, Iterator
from fastapi import status, APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm.session import Session
from starlette.exceptions import HTTPException

from filerepo.webapp.repository.file.file_repository import FileRepositoryImpl

from filerepo.webapp.repository.uploadActivity.uploadActivity_repository import UploadActivityRepositoryImpl
from filerepo.webapp.service.uploadActivity_service import UploadActivityServiceImpl, UploadActivityService
from filerepo.webapp.schemas.DTO.uploadActivity.upload_activity_get_response import UploadActivityGetResponse

from filerepo.webapp.repository.database import SessionLocal

router = APIRouter()


def get_session() -> Iterator[Session]:
    session: Session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


def fnc_upload_activity_service(session: Session = Depends(get_session)) -> UploadActivityService:
    repository: UploadActivityRepositoryImpl = UploadActivityRepositoryImpl(session)
    files_repository: FileRepositoryImpl = FileRepositoryImpl(session)
    service: UploadActivityService = UploadActivityServiceImpl(repository, files_repository)
    return service


@router.get("/uploadactivities/{file_id}/history", response_model=List[UploadActivityGetResponse],
            status_code=status.HTTP_200_OK,
            tags=["upload_activity"])
def get_history_by_id(file_id: int,
                      upload_activity_service: UploadActivityService = Depends(fnc_upload_activity_service)):
    try:
        return upload_activity_service.find_upload_activity_by_file_id(file_id)
    except FileNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/uploadactivities", response_model=List[UploadActivityGetResponse], status_code=status.HTTP_200_OK,
            tags=["upload_activity"])
def get_history(upload_activity_service: UploadActivityService = Depends(fnc_upload_activity_service)):
    try:
        return upload_activity_service.find_all()
    except FileNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
