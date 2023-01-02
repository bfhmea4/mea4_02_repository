from abc import ABC, abstractmethod
from typing import Optional

from .workflow import Workflow


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

    @abstractmethod
    def update_status(self, status: bool, workflow_id: int):
        raise NotImplementedError

