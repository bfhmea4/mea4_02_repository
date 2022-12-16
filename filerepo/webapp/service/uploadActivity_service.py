import io
from abc import ABC, abstractmethod
from typing import List, Optional, cast

from filerepo.webapp.domain.file.file_repository import FileRepository
from filerepo.webapp.domain.uploadActivity.uploadActivity import UploadActivity
from filerepo.webapp.repository.file.file_repository import FileRepositoryImpl
from filerepo.webapp.schemas.DTO.uploadActivity.upload_activity_get_model import UploadActivityGetModel
from filerepo.webapp.schemas.DTO.uploadActivity.upload_activity_create_model import UploadActivityCreateModel
from filerepo.webapp.repository.uploadActivity.uploadActivity_repository import UploadActivityRepository, \
    UploadActivityRepositoryImpl


class UploadActivityService(ABC):
    """UploadActivityService defines a query service inteface related UploadActivity entity."""

    @abstractmethod
    def find_by_id(self, id: str) -> Optional[UploadActivityGetModel]:
        raise NotImplementedError

    @abstractmethod
    def find_all(self) -> List[UploadActivityGetModel]:
        raise NotImplementedError

    @abstractmethod
    def create(self, uploadActivity: UploadActivity) -> UploadActivityGetModel:
        raise NotImplementedError

    @abstractmethod
    def find_upload_activity_by_file_id(self, file_id: int) -> List[UploadActivityGetModel]:
        raise NotImplementedError


class UploadActivityServiceImpl(UploadActivityService):
    """UploadActivityServiceImpl defines a query service inteface related UploadActivity entity."""

    def __init__(self, repository: UploadActivityRepositoryImpl, files_repository: FileRepositoryImpl):
        self.repository = repository
        self.files_repository = files_repository

    def find_by_id(self, id: str) -> Optional[UploadActivityGetModel]:
        upload_activity: UploadActivity = self.repository.find_by_id(id)
        return UploadActivityGetModel.from_entity(cast(UploadActivity, upload_activity))

    def find_upload_activity_by_file_id(self, file_id: int) -> List[UploadActivityGetModel]:
        all_upload_activities = self.repository.find_all()
        list_upload_activity_by_id = []
        for uploadActivity in all_upload_activities:
            if uploadActivity.file_id == file_id:
                list_upload_activity_by_id.append(
                    UploadActivityGetModel.from_entity(cast(UploadActivity, uploadActivity)))
        return list_upload_activity_by_id

    def find_all(self) -> List[UploadActivityGetModel]:
        all_uploadActivities = self.repository.find_all()
        list_uploadActivities = []
        for uploadActivity in all_uploadActivities:
            list_uploadActivities.append(UploadActivityGetModel.from_entity(cast(UploadActivity, uploadActivity)))
        return list_uploadActivities

    def create(self, new_uploadActivity: UploadActivityCreateModel) -> UploadActivityGetModel:
        uploadActivity: UploadActivity = self.repository.create(new_uploadActivity)
        return UploadActivityGetModel.from_entity(cast(UploadActivity, uploadActivity))
