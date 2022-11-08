import io
from abc import ABC, abstractmethod
from typing import List, Optional, cast
import shortuuid
import hashlib
import time

from filerepo.webapp.domain.file.file import File
from filerepo.webapp.schemas.file_schema import FileUploadModel, FileGetModel, FileDownloadModel, FileInfoGetModel
from filerepo.webapp.repository.file.file_repository import FileRepositoryImpl


class FileService(ABC):
    """FileQueryService defines a query service inteface related Book entity."""

    @abstractmethod
    def find_by_id(self, id: str) -> Optional[FileGetModel]:
        raise NotImplementedError

    @abstractmethod
    def file_info_by_id(self, id: str) -> Optional[FileInfoGetModel]:
        raise NotImplementedError

    @abstractmethod
    def find_all(self) -> List[FileGetModel]:
        raise NotImplementedError

    @abstractmethod
    def create(self, file: FileUploadModel) -> FileGetModel:
        raise NotImplementedError

    @abstractmethod
    def delete(self, id: str):
        raise NotImplementedError

    @abstractmethod
    def download_by_id(self, id: str) -> FileGetModel:
        raise NotImplementedError

class FileServiceImpl(FileService):
    """FileQueryService defines a query service inteface related File entity."""

    def __init__(self, repository: FileRepositoryImpl):
        self.repository = repository

    def find_by_id(self, id: str) -> Optional[FileGetModel]:
        file = self.repository.find_by_id(id)
        return FileGetModel.from_entity(cast(File, file))

    def find_all(self) -> List[FileGetModel]:
        all_files = self.repository.find_all()
        list_files = []
        for file in all_files:
            list_files.append(FileGetModel.from_entity(cast(File,file)))
        return list_files

    def file_info_by_id(self, id: str) -> Optional[FileInfoGetModel]:
        file = self.repository.find_by_id(id)
        return FileInfoGetModel.from_entity(cast(File, file))

    def create(self, file_uploaded: FileUploadModel) -> FileGetModel:
        id: str = shortuuid.uuid()
        #file_content = io.BytesIO(file_uploaded.file_content)
        file_type: str = file_uploaded.file_type
        hash = hashlib.sha256(file_uploaded.file_content).hexdigest()
        current_time = time.time()
        file = File(id,file_uploaded.file_name,'./',len(file_uploaded.file_content),file_type,hash,file_uploaded.file_content,current_time,current_time)
        self.repository.create(file)
        return FileGetModel.from_entity(cast(File,file))

    def delete(self, id: str):
        self.repository.delete_by_id(id)

    def download_by_id(self, id: str) -> FileDownloadModel:
        file = self.repository.find_by_id(id)
        return FileDownloadModel.from_entity(cast(File, file))
