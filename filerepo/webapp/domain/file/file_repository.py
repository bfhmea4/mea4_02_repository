from abc import ABC, abstractmethod
from typing import List, Optional

from .file import File


class FileRepository(ABC):
    """FileRepository defines a repository interface for File entity."""

    @abstractmethod
    def create(self, file: File) -> Optional[File]:
        raise NotImplementedError

    @abstractmethod
    def find_by_id(self, id: str) -> Optional[File]:
        raise NotImplementedError

    @abstractmethod
    def update(self, file: File) -> Optional[File]:
        raise NotImplementedError

    @abstractmethod
    def delete_by_id(self, id: str):
        raise NotImplementedError