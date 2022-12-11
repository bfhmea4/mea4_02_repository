from abc import ABC, abstractmethod
from typing import List, Optional, cast

from filerepo.webapp.domain.workflow.workflow import Workflow
from filerepo.webapp.schemas.DTO.workflow.workflow_get_model import WorkflowGetModel


class WorkflowService(ABC):
    """WorkflowService defines a query service interface to interact with the workflow engine."""

    @abstractmethod
    def find_by_id(self, id: str) -> Optional[WorkflowGetModel]:
        raise NotImplementedError

    @abstractmethod
    def create(self, workflow: Workflow) -> WorkflowGetModel:
        raise NotImplementedError

    @abstractmethod
    def find_workflow_by_upload_activity_id(self, upload_activity_id: int) -> WorkflowGetModel:
        raise NotImplementedError


class WorkflowServiceImpl(WorkflowService):
    """WorkflowServiceImpl is a query service interface to interact with the workflow engine."""

    def __init__(self, repository: WorkflowRepository):
        self.repository = repository

    def find_by_id(self, id: str) -> Optional[UploadActivityGetModel]:
        uploadActivity: UploadActivity = self.repository.find_by_id(id)
        return UploadActivityGetModel.from_entity(cast(UploadActivity, uploadActivity))

    def find_workflow_by_upload_activity_id(self, upload_activity_id: int) -> WorkflowGetModel:
        all_uploadActivities = self.repository.find_all()
        list_uploadActivity_by_id = []
        for uploadActivity in all_uploadActivities:
            if uploadActivity.file_id == file_id:
                list_uploadActivity_by_id.append(
                    UploadActivityGetModel.from_entity(cast(UploadActivity, uploadActivity)))
        return list_uploadActivity_by_id

    def create(self, new_uploadActivity: UploadActivityCreateModel) -> UploadActivityGetModel:
        uploadActivity: UploadActivity = self.repository.create(new_uploadActivity)
        return UploadActivityGetModel.from_entity(cast(UploadActivity, uploadActivity))
