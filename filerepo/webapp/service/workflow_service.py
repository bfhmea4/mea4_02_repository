from abc import ABC, abstractmethod
from typing import List, Optional, cast
import asyncio

from filerepo.webapp.domain.workflow.workflow import Workflow
from filerepo.webapp.schemas.DTO.workflow.workflow_create_model import WorkflowCreateModel
from filerepo.webapp.schemas.DTO.workflow.workflow_get_model import WorkflowGetModel

from filerepo.webapp.repository.workflow.workflow_repository import WorkflowRepositoryImpl

from filerepo.algorithms.workflow_handler import WorkflowHandler
from filerepo.webapp.schemas.DTO.uploadActivity.upload_activity_get_model import UploadActivityGetModel
from filerepo.webapp.repository.file.file_dto import FileDTO


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

    def __init__(self, repository: WorkflowRepositoryImpl):
        self.repository = repository
        self.workflow_handler = None

    def find_by_id(self, id: str) -> Optional[WorkflowGetModel]:
        workflow: Workflow = self.repository.find_by_id(id)
        return WorkflowGetModel.from_entity(cast(Workflow, workflow))

    def find_workflow_by_upload_activity_id(self, upload_activity_id: int) -> WorkflowGetModel:
        workflow = self.repository.find_workflow_by_upload_activity_id(upload_activity_id)
        return WorkflowGetModel.from_entity(cast(Workflow, workflow))

    async def create(self, upload_activity: UploadActivityGetModel, file: FileDTO) -> WorkflowGetModel:
        new_workflow = WorkflowCreateModel(False,upload_activity.id)
        workflow: Workflow = self.repository.create(new_workflow)
        self.workflow_handler = WorkflowHandler(workflow=workflow,file=file)
        await self.workflow_handler.kickoff(workflow,file)
        return WorkflowGetModel.from_entity(cast(Workflow, workflow))
