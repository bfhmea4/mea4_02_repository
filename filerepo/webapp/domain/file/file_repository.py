from abc import ABC, abstractmethod
from typing import List, Optional

from .file import File
from filerepo.webapp.repository.file.file_dto import FileDTO


class FileRepository(ABC):
    """FileRepository defines a repository interface for File entity."""

    @abstractmethod
    def create(self, file: File):
        raise NotImplementedError

    @abstractmethod
    def find_all(self, file: File) -> Optional[List[FileDTO]]:
        raise NotImplementedError

    @abstractmethod
    def find_by_id(self, id: str) -> Optional[FileDTO]:
        raise NotImplementedError

    @abstractmethod
    def delete_by_id(self, id: str):
        raise NotImplementedError