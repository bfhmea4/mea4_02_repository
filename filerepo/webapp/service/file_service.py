import hashlib
import time
from abc import ABC, abstractmethod
from typing import List, Optional, cast

from fastapi import UploadFile

from filerepo.webapp.domain.file.file import File
from filerepo.webapp.domain.file.file_repository import FileRepository
from filerepo.webapp.domain.uploadActivity.uploadActivity_repository import UploadActivityRepository
from filerepo.webapp.schemas.DTO.file.file_download_response import FileDownloadResponse
from filerepo.webapp.schemas.DTO.file.file_get_request import FileGetRequest
from filerepo.webapp.schemas.DTO.file.file_info_response import FileInfoGetResponse
from filerepo.webapp.schemas.DTO.file.file_upload_request import FileUploadRequest
from filerepo.webapp.repository.file.file_repository import FileRepositoryImpl

from filerepo.webapp.schemas.DTO.uploadActivity.upload_activity_create_request import UploadActivityCreateRequest
from filerepo.webapp.domain.uploadActivity.uploadActivity import UploadActivity
from filerepo.webapp.repository.uploadActivity.uploadActivity_repository import UploadActivityRepositoryImpl
from filerepo.webapp.schemas.DTO.uploadActivity.upload_activity_get_response import UploadActivityGetResponse
from filerepo.webapp.service.workflow_service import WorkflowService


class FileService(ABC):
    """FileQueryService defines a query service inteface related Book entity."""

    @abstractmethod
    def find_by_id(self, file_id: int) -> Optional[FileGetRequest]:
        raise NotImplementedError

    @abstractmethod
    def file_info_by_id(self, file_id: int) -> Optional[FileInfoGetResponse]:
        raise NotImplementedError

    @abstractmethod
    def find_all(self) -> List[FileGetRequest]:
        raise NotImplementedError

    @abstractmethod
    def delete(self, file_id: int):
        raise NotImplementedError

    @abstractmethod
    def download_by_id(self, file_id: int) -> FileDownloadResponse:
        raise NotImplementedError

    @abstractmethod
    def get_file_id_by_hash(self, file_hash) -> int:
        raise NotImplementedError

    @abstractmethod
    def upload_file(self, file: UploadFile) -> UploadActivityGetResponse:
        raise NotImplementedError


class FileServiceImpl(FileService):
    """FileQueryService defines a query service inteface related File entity."""

    def __init__(self, repository: FileRepositoryImpl, upload_activity_repository: UploadActivityRepositoryImpl, workflow_service: WorkflowService):
        self.repository: FileRepository = repository
        self.upload_activity_repository: UploadActivityRepository = upload_activity_repository
        self.workflow_service: WorkflowService = workflow_service

    def find_by_id(self, file_id: int) -> Optional[FileGetRequest]:
        file = self.repository.find_by_id(file_id)
        return FileGetRequest.from_entity(cast(File, file))

    async def upload_file(self, file: UploadFile):
        uploaded_file = {
            "file_name": file.filename,
            "file_type": file.content_type,
            "file_content": file.file.read()
        }
        file_hash = hashlib.sha256(uploaded_file['file_content']).hexdigest()
        file_id: int = self.get_file_id_by_hash(file_hash)
        if file_id is not None:
            upload_activity_dict = {
                "file_name": uploaded_file['file_name'],
                "file_id": file_id
            }
        else:
            upload: FileUploadRequest = FileUploadRequest(**uploaded_file)
            file = File(file_name=upload.file_name, file_size=len(upload.file_content),
                        file_type=upload.file_type, file_hash=file_hash, file_content=upload.file_content,
                        file_creation_time=time.time(), file_update_time=time.time())
            file_get_model = self.repository.create(file)
            upload_activity_dict = {
                "file_name": file_get_model.file_name,
                "file_id": file_get_model.id
            }
        upload_activity_request: UploadActivityCreateRequest = UploadActivityCreateRequest(**upload_activity_dict)
        upload_activity: UploadActivity = UploadActivity(upload_time=time.time(),
                                                         file_name=upload_activity_request.file_name,
                                                         file_id=upload_activity_request.file_id)
        upload_activity_result = self.upload_activity_repository.create(upload_activity)
        await self.workflow_service.start_file_analysis_request(upload_activity_result, self.repository.find_by_id(upload_activity_result.file_id))
        return UploadActivityGetResponse.from_entity(upload_activity_result)

    def find_all(self) -> List[FileGetRequest]:
        all_files: List[File] = self.repository.find_all()
        list_files: List[FileGetRequest] = []
        for file in all_files:
            list_files.append(FileGetRequest.from_entity(cast(File, file)))
        return list_files

    def file_info_by_id(self, file_id: int) -> Optional[FileInfoGetResponse]:
        file: File = self.repository.find_by_id(file_id)
        return FileInfoGetResponse.from_entity(cast(File, file))

    def delete(self, file_id: int):
        self.repository.delete_by_id(file_id)

    def download_by_id(self, file_id: int) -> FileDownloadResponse:
        file: File = self.repository.find_by_id(file_id)
        return FileDownloadResponse.from_entity(cast(File, file))

    def get_file_id_by_hash(self, file_hash) -> int:
        file_id: int = self.repository.find_by_hash(file_hash)
        return file_id
