import hashlib
import io
from abc import ABC, abstractmethod
from typing import List, Optional, cast, Iterator

from fastapi import Depends, UploadFile
from sqlalchemy.orm import Session

from filerepo.webapp.domain.file.file import File
from filerepo.webapp.domain.file.file_repository import FileRepository
from filerepo.webapp.domain.uploadActivity.uploadActivity_repository import UploadActivityRepository
from filerepo.webapp.repository.database import SessionLocal
from filerepo.webapp.routers.upload_activity import get_session
from filerepo.webapp.schemas.DTO.file_download_model import FileDownloadModel
from filerepo.webapp.schemas.DTO.file_get_model import FileGetModel
from filerepo.webapp.schemas.DTO.file_info_model import FileInfoGetModel
from filerepo.webapp.schemas.DTO.file_upload_model import FileUploadModel
from filerepo.webapp.repository.file.file_repository import FileRepositoryImpl
from filerepo.webapp.schemas.DTO.uploadActivity.upload_activity_create_model import UploadActivityCreateModel
from filerepo.webapp.service.uploadActivity_service import UploadActivityServiceImpl, UploadActivityService
from filerepo.webapp.repository.uploadActivity.uploadActivity_repository import UploadActivityRepositoryImpl


class FileService(ABC):
    """FileQueryService defines a query service inteface related Book entity."""

    @abstractmethod
    def find_by_id(self, file_id: int) -> Optional[FileGetModel]:
        raise NotImplementedError

    @abstractmethod
    def file_info_by_id(self, file_id: int) -> Optional[FileInfoGetModel]:
        raise NotImplementedError

    @abstractmethod
    def find_all(self) -> List[FileGetModel]:
        raise NotImplementedError

    @abstractmethod
    def create(self, file_uploaded: FileUploadModel) -> FileGetModel:
        raise NotImplementedError

    @abstractmethod
    def delete(self, file_id: int):
        raise NotImplementedError

    @abstractmethod
    def download_by_id(self, file_id: int) -> FileDownloadModel:
        raise NotImplementedError

    @abstractmethod
    def get_file_id_by_hash(self, file_hash) -> int:
        raise NotImplementedError

    @abstractmethod
    def upload_file(self, file: UploadFile) -> FileUploadModel:
        raise NotImplementedError


class FileServiceImpl(FileService):
    """FileQueryService defines a query service inteface related File entity."""

    def __init__(self, repository: FileRepositoryImpl, upload_activity_repository: UploadActivityRepositoryImpl):
        self.repository = repository
        self.upload_activity_repository = upload_activity_repository

    def find_by_id(self, file_id: int) -> Optional[FileGetModel]:
        file = self.repository.find_by_id(file_id)
        return FileGetModel.from_entity(cast(File, file))

    def upload_file(self, file: UploadFile):
        uploaded_file = {
            "file_name": file.filename,
            "file_type": file.content_type,
            "file_content": file.file.read()
        }
        file_hash = hashlib.sha256(uploaded_file['file_content']).hexdigest()
        file_id: int = self.get_file_id_by_hash(file_hash)
        if file_id is not None:
            upload_activity = {
                "file_name": uploaded_file['file_name'],
                "file_id": file_id
            }
        else:
            file_get_model = self.repository.create(FileUploadModel(**uploaded_file))
            upload_activity = {
                "file_name": file_get_model.file_name,
                "file_id": file_get_model.id
            }
        upload_activity_result = self.upload_activity_repository.create(UploadActivityCreateModel(**upload_activity))
        return upload_activity_result

    def find_all(self) -> List[FileGetModel]:
        all_files = self.repository.find_all()
        list_files = []
        for file in all_files:
            list_files.append(FileGetModel.from_entity(cast(File, file)))
        return list_files

    def file_info_by_id(self, file_id: int) -> Optional[FileInfoGetModel]:
        file = self.repository.find_by_id(file_id)
        return FileInfoGetModel.from_entity(cast(File, file))

    def create(self, file_uploaded: FileUploadModel) -> FileGetModel:
        file = self.repository.create(file_uploaded)
        return FileGetModel.from_entity(cast(File, file))

    def delete(self, file_id: int):
        self.repository.delete_by_id(file_id)

    def download_by_id(self, file_id: int) -> FileDownloadModel:
        file = self.repository.find_by_id(file_id)
        return FileDownloadModel.from_entity(cast(File, file))

    def get_file_id_by_hash(self, file_hash) -> int:
        file_id: int = self.repository.find_by_hash(file_hash)
        return file_id
