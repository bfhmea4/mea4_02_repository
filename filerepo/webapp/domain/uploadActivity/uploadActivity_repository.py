from abc import ABC, abstractmethod
from typing import List, Optional

from filerepo.webapp.domain.uploadActivity.uploadActivity import UploadActivity


class UploadActivityRepository(ABC):
    """UploadActivityRepository defines a repository interface for UploadActivity entity."""

    @abstractmethod
    def create(self, uploadActivity: UploadActivity) -> UploadActivity:
        raise NotImplementedError

    @abstractmethod
    def find_all(self) -> Optional[List[UploadActivity]]:
        raise NotImplementedError

    @abstractmethod
    def find_by_id(self, id: int) -> Optional[UploadActivity]:
        raise NotImplementedError

    @abstractmethod
    def delete_by_id(self, id: str):
        raise NotImplementedError

