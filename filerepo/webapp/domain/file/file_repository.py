from abc import ABC, abstractmethod
from typing import List, Optional

from .file import File
from filerepo.webapp.repository.file.file_dto import FileDTO
from filerepo.webapp.schemas.DTO.file_upload_model import FileUploadModel


class FileRepository(ABC):
    """FileRepository defines a repository interface for File entity."""

    @abstractmethod
    def create(self, file_uploaded: FileUploadModel):
        raise NotImplementedError

    @abstractmethod
    def find_all(self) -> Optional[List[FileDTO]]:
        raise NotImplementedError

    @abstractmethod
    def find_by_id(self, id: int) -> Optional[FileDTO]:
        raise NotImplementedError

    @abstractmethod
    def delete_by_id(self, id: int):
        raise NotImplementedError

    @abstractmethod
    def find_by_hash(self, hash: int):
        raise NotImplementedError