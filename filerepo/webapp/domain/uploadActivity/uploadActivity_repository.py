from abc import ABC, abstractmethod
from typing import List, Optional

from .uploadActivity import UploadActivity
from filerepo.webapp.repository.uploadActivity.uploadActivity_dto import UploadActivityDTO


class UploadActivityRepository(ABC):
    """FileRepository defines a repository interface for File entity."""

    @abstractmethod
    def create(self, uploadActivity: UploadActivityDTO):
        raise NotImplementedError

    @abstractmethod
    def find_all(self) -> Optional[List[UploadActivityDTO]]:
        raise NotImplementedError

    @abstractmethod
    def find_by_id(self, id: str) -> Optional[UploadActivityDTO]:
        raise NotImplementedError

    @abstractmethod
    def delete_by_id(self, id: str):
        raise NotImplementedError

