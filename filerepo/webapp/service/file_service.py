import io
from abc import ABC, abstractmethod
from typing import List, Optional, cast

from filerepo.webapp.domain.file.file_db import File
from filerepo.webapp.schemas.DTO.file_download_model import FileDownloadModel
from filerepo.webapp.schemas.DTO.file_get_model import FileGetModel
from filerepo.webapp.schemas.DTO.file_info_model import FileInfoGetModel
from filerepo.webapp.schemas.DTO.file_upload_model import FileUploadModel
from filerepo.webapp.repository.file.file_repository_db import FileRepositoryImpl


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
    def create(self, file_uploaded: FileUploadModel) -> FileGetModel:
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
        file = self.repository.create(file_uploaded)
        return FileGetModel.from_entity(cast(File,file))

    def delete(self, id: str):
        self.repository.delete_by_id(id)

    def download_by_id(self, id: str) -> FileDownloadModel:
        file = self.repository.find_by_id(id)
        return FileDownloadModel.from_entity(cast(File, file))

    def get_file_id_by_hash(self, hash) -> str:
        file_id: str = self.repository.find_by_hash(hash)
        return file_id
