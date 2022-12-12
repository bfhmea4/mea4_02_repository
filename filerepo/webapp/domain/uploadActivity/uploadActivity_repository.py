from abc import ABC, abstractmethod
from typing import List, Optional

from filerepo.webapp.schemas.DTO.uploadActivity.upload_activity_create_model import UploadActivityCreateModel

from .uploadActivity import UploadActivity
from filerepo.webapp.repository.uploadActivity.uploadActivity_dto import UploadActivityDTO


class UploadActivityRepository(ABC):
    """UploadActivity defines a repository interface for UploadActivity entity."""

    @abstractmethod
    def create(self, uploadActivity: UploadActivityCreateModel):
        raise NotImplementedError

    @abstractmethod
    def find_all(self) -> Optional[List[UploadActivityDTO]]:
        raise NotImplementedError

    @abstractmethod
    def find_by_id(self, id: int) -> Optional[UploadActivityDTO]:
        raise NotImplementedError

    @abstractmethod
    def delete_by_id(self, id: int):
        raise NotImplementedError

