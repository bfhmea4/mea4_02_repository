from abc import ABC, abstractmethod
from typing import List, Optional

from .file import File
from filerepo.webapp.schemas.DTO.file.file_upload_request import FileUploadRequest


class FileRepository(ABC):
    """FileRepository defines a repository interface for File entity."""

    @abstractmethod
    def create(self, file_uploaded: FileUploadRequest) -> File:
        raise NotImplementedError

    @abstractmethod
    def find_all(self) -> Optional[List[File]]:
        raise NotImplementedError

    @abstractmethod
    def find_by_id(self, id: str) -> Optional[File]:
        raise NotImplementedError

    @abstractmethod
    def delete_by_id(self, id: str):
        raise NotImplementedError

    @abstractmethod
    def find_by_hash(self, hash: str) -> int:
        raise NotImplementedError