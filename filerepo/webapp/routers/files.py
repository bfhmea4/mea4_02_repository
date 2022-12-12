import hashlib
from typing import List, Iterator
from fastapi import File, UploadFile, status, APIRouter, Depends
from fastapi.responses import JSONResponse, Response
from sqlalchemy.orm.session import Session

from filerepo.webapp.schemas.DTO.file_get_model import FileGetModel
from filerepo.webapp.schemas.DTO.file_upload_model import FileUploadModel
from filerepo.webapp.schemas.DTO.file_info_model import FileInfoGetModel
from filerepo.webapp.service.file_service import FileServiceImpl
from filerepo.webapp.repository.file.file_repository import FileRepositoryImpl
from filerepo.webapp.domain.file.file_repository import FileRepository

from filerepo.webapp.repository.uploadActivity.uploadActivity_repository import UploadActivityRepositoryImpl
from filerepo.webapp.domain.uploadActivity.uploadActivity_repository import UploadActivityRepository
from filerepo.webapp.service.uploadActivity_service import UploadActivityServiceImpl
from filerepo.webapp.schemas.DTO.uploadActivity.upload_activity_create_model import UploadActivityCreateModel

from filerepo.webapp.repository.workflow.workflow_repository import WorkflowRepositoryImpl
from filerepo.webapp.repository.workflow.workflow_repository import WorkflowRepository
from filerepo.webapp.service.workflow_service import WorkflowServiceImpl

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


def fnc_file_repository(session: Session = Depends(get_session)) -> FileRepository:
    repository: FileRepositoryImpl = FileRepositoryImpl(session)
    return repository

def fnc_workflow_repository(session: Session = Depends(get_session)) -> WorkflowRepository:
    repository: WorkflowRepositoryImpl = WorkflowRepositoryImpl(session)
    return repository


# Use FileSystem to write blob data to file system separate from meta data
# This functionality can be migrated into the file repository later on ToDo: Split file and blobData to store blob on FS
# file_system = FileSystem()
# file_repository = FileRepositoryImpl(file_system)
# file_service = FileServiceImpl(file_repository)

@router.post("/files/upload", response_model=FileGetModel, tags=["files"])
async def upload(file: UploadFile = File(...),
           upload_activity_repository: UploadActivityRepositoryImpl = Depends(fnc_upload_activity_repository),
           file_repository: FileRepositoryImpl = Depends(fnc_file_repository),
           workflow_repository: WorkflowRepositoryImpl = Depends(fnc_workflow_repository)):
    try:
        file_service = FileServiceImpl(file_repository)
        upload_activity_service = UploadActivityServiceImpl(upload_activity_repository)
        workflow_service = WorkflowServiceImpl(workflow_repository)
        uploaded_file = {
            "file_name": file.filename,
            "file_type": file.content_type,
            "file_content": file.file.read()
        }
        file_hash = hashlib.sha256(uploaded_file['file_content']).hexdigest()
        file_id: int = file_service.get_file_id_by_hash(file_hash)
        if file_id is not None:
            upload_activity = {
                "file_name": uploaded_file['file_name'],
                "file_id": file_id
            }
            upload_activity_result = upload_activity_service.create(UploadActivityCreateModel(**upload_activity))
            return upload_activity_service.find_by_id(upload_activity_result.id)
        else:
            file_get_model = file_service.create(FileUploadModel(**uploaded_file))
            upload_activity = {
                "file_name": file_get_model.file_name,
                "file_id": file_get_model.id
            }
            upload_activity = upload_activity_service.create(UploadActivityCreateModel(**upload_activity))
        await workflow_service.create(upload_activity, file_repository.find_by_id(file_get_model.id))
        return file_get_model

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
