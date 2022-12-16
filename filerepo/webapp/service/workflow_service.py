from abc import ABC, abstractmethod
from typing import List, Optional, cast
import asyncio

from filerepo.webapp.domain.file.file import File
from filerepo.webapp.domain.uploadActivity.uploadActivity import UploadActivity
from filerepo.webapp.domain.workflow.workflow import Workflow
from filerepo.webapp.schemas.DTO.workflow.workflow_create_model import WorkflowCreateModel
from filerepo.webapp.schemas.DTO.workflow.workflow_get_model import WorkflowGetModel

from filerepo.webapp.repository.workflow.workflow_repository import WorkflowRepositoryImpl
from filerepo.webapp.repository.workflow.workflow_dto import WorkflowDTO

from filerepo.algorithms.workflow_handler import WorkflowHandler




class WorkflowService(ABC):
    """WorkflowService defines a query service interface to interact with the workflow engine."""

    @abstractmethod
    def find_by_id(self, id: str) -> Optional[WorkflowGetModel]:
        raise NotImplementedError

    @abstractmethod
    def start_file_analysis_request(self, upload_activity: UploadActivity, file: File) -> WorkflowGetModel:
        raise NotImplementedError

    @abstractmethod
    def find_workflow_by_upload_activity_id(self, upload_activity_id: int) -> WorkflowGetModel:
        raise NotImplementedError

    def update_status(self, status: bool, workflow_id: int):
        raise NotImplementedError


class WorkflowServiceImpl(WorkflowService):
    """WorkflowServiceImpl is a query service interface to interact with the workflow engine."""

    def __init__(self, repository: WorkflowRepositoryImpl):
        self.repository = repository
        self.workflow_handler = None

    def find_by_id(self, id: int) -> Optional[WorkflowGetModel]:
        workflow: WorkflowDTO = self.repository.find_by_id(id)
        return WorkflowGetModel.from_entity(cast(Workflow, workflow))

    def find_workflow_by_upload_activity_id(self, upload_activity_id: int) -> WorkflowGetModel:
        workflow = self.repository.find_workflow_by_upload_activity_id(upload_activity_id)
        return WorkflowGetModel.from_entity(cast(Workflow, workflow))

    #Todo: param: start_file_analysis_request
    def start_file_analysis_request(self, upload_activity: UploadActivity, file: File) -> WorkflowGetModel:
        new_workflow = WorkflowCreateModel(**{"finished":False,"upload_activity":upload_activity.id})
        workflow: Workflow = self.repository.create(new_workflow)
        self.workflow_handler = WorkflowHandler(workflow=workflow,file=file)
        self.workflow_handler.kickoff()
        return WorkflowGetModel.from_entity(cast(Workflow, workflow))

    def update_status(self, status: bool, workflow_id: int):
        self.repository.update_status(status, workflow_id)
