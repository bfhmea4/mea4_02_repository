import time
from abc import ABC, abstractmethod
from typing import List, Optional, cast

from filerepo.webapp.domain.uploadActivity.uploadActivity import UploadActivity
from filerepo.webapp.repository.file.file_repository import FileRepositoryImpl
from filerepo.webapp.schemas.DTO.uploadActivity.upload_activity_get_response import UploadActivityGetResponse
from filerepo.webapp.schemas.DTO.uploadActivity.upload_activity_create_request import UploadActivityCreateRequest
from filerepo.webapp.repository.uploadActivity.uploadActivity_repository import UploadActivityRepositoryImpl


class UploadActivityService(ABC):
    """UploadActivityService defines a query service inteface related UploadActivity entity."""

    @abstractmethod
    def find_by_id(self, id: str) -> Optional[UploadActivityGetResponse]:
        raise NotImplementedError

    @abstractmethod
    def find_all(self) -> List[UploadActivityGetResponse]:
        raise NotImplementedError

    @abstractmethod
    def create(self, uploadActivity: UploadActivity) -> UploadActivityGetResponse:
        raise NotImplementedError

    @abstractmethod
    def find_upload_activity_by_file_id(self, file_id: int) -> List[UploadActivityGetResponse]:
        raise NotImplementedError


class UploadActivityServiceImpl(UploadActivityService):
    """UploadActivityServiceImpl defines a query service inteface related UploadActivity entity."""

    def __init__(self, repository: UploadActivityRepositoryImpl, files_repository: FileRepositoryImpl):
        self.repository = repository
        self.files_repository = files_repository

    def find_by_id(self, id: str) -> Optional[UploadActivityGetResponse]:
        upload_activity: UploadActivity = self.repository.find_by_id(id)
        return UploadActivityGetResponse.from_entity(cast(UploadActivity, upload_activity))

    def find_upload_activity_by_file_id(self, file_id: int) -> List[UploadActivityGetResponse]:
        all_upload_activities = self.repository.find_all()
        list_upload_activity_by_id = []
        for uploadActivity in all_upload_activities:
            if uploadActivity.file_id == file_id:
                list_upload_activity_by_id.append(
                    UploadActivityGetResponse.from_entity(cast(UploadActivity, uploadActivity)))
        return list_upload_activity_by_id

    def find_all(self) -> List[UploadActivityGetResponse]:
        all_upload_activities = self.repository.find_all()
        list_upload_activities = []
        for uploadActivity in all_upload_activities:
            list_upload_activities.append(UploadActivityGetResponse.from_entity(cast(UploadActivity, uploadActivity)))
        return list_upload_activities

    def create(self, upload_activity_request: UploadActivityCreateRequest) -> UploadActivityGetResponse:
        upload_time: float = time.time()
        upload_file_name: str = upload_activity_request.file_name
        upload_file_id: int = upload_activity_request.file_id
        new_upload_activity = UploadActivity(upload_time=upload_time, file_name=upload_file_name, file_id=upload_file_id)
        upload_activity: UploadActivity = self.repository.create(new_upload_activity)
        return UploadActivityGetResponse.from_entity(cast(UploadActivity, upload_activity))
