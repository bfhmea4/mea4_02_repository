from abc import ABC, abstractmethod
from typing import List, Optional

from filerepo.webapp.schemas.DTO.workflow.workflow_create_model import WorkflowCreateModel

from .workflow import Workflow
from filerepo.webapp.repository.workflow.workflow_dto import WorkflowDTO


class WorkflowRepository(ABC):
    """WorkflowRepository defines a repository interface for Workflow entity."""

    @abstractmethod
    def create(self, workflow: Workflow):
        raise NotImplementedError

    @abstractmethod
    def find_by_id(self, id: int) -> Optional[Workflow]:
        raise NotImplementedError

    @abstractmethod
    def delete_by_id(self, id: int):
        raise NotImplementedError

    @abstractmethod
    def find_workflow_by_upload_activity_id(self, id: int):
        raise NotImplementedError

