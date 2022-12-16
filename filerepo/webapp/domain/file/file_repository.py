from abc import ABC, abstractmethod
from typing import List, Optional

from filerepo.webapp.domain.file.file import File


class FileRepository(ABC):
    """FileRepository defines a repository interface for File entity."""

    @abstractmethod
    def create(self, file_uploaded: File) -> File:
        raise NotImplementedError

    @abstractmethod
    def find_all(self) -> Optional[List[File]]:
        raise NotImplementedError

    @abstractmethod
    def find_by_id(self, id: int) -> Optional[File]:
        raise NotImplementedError

    @abstractmethod
    def delete_by_id(self, id: int):
        raise NotImplementedError

    @abstractmethod
    def find_by_hash(self, hash: str) -> int:
        raise NotImplementedError