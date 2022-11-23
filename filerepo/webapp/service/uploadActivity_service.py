import io
from abc import ABC, abstractmethod
from typing import List, Optional, cast

from filerepo.webapp.domain.uploadActivity.uploadActivity import UploadActivity
from filerepo.webapp.repository.uploadActivity.uploadActivity_repository import UploadActivityRepository


class UploadActivityService(ABC):
    """UploadActivityService defines a query service inteface related UploadActivity entity."""

    @abstractmethod
    def find_by_id(self, id: str) -> Optional[UploadActivityGetModel]: #Todo: Create GetModel
        raise NotImplementedError

    @abstractmethod
    def find_all(self) -> List[UploadActivityGetModel]:
        raise NotImplementedError

    @abstractmethod
    def create(self, uploadActivity: UploadActivity) -> UploadActivityGetModel:
        raise NotImplementedError

class UploadActivityServiceImpl(UploadActivityService):
    """UploadActivityServiceImpl defines a query service inteface related UploadActivity entity."""

    def __init__(self, repository: UploadActivityRepository):
        self.repository = repository

    def find_by_id(self, id: str) -> Optional[UploadActivityGetModel]:
        uploadActivity: UploadActivity = self.repository.find_by_id(id)
        return UploadActivityGetModel.from_entity(cast(UploadActivity, uploadActivity))

    def find_all(self) -> List[UploadActivityGetModel]:
        all_uploadActivities = self.repository.find_all()
        list_uploadActivities = []
        for uploadActivity in all_uploadActivities:
            list_uploadActivities.append(UploadActivityGetModel.from_entity(cast(UploadActivity,uploadActivity)))
        return list_uploadActivities

    def create(self, new_uploadActivity: UploadActivityModel) -> UploadActivityModel: #Todo: create new Model
        uploadActivity: UploadActivity = self.repository.create(new_uploadActivity)
        return UploadActivityGetModel.from_entity(cast(UploadActivity,uploadActivity))
