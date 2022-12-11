from pydantic import BaseModel

from filerepo.webapp.domain.workflow.workflow import Workflow


class WorkflowGetModel(BaseModel):
    id: int
    finished: bool
    upload_activity: int

    @staticmethod
    def from_entity(workflow: Workflow) -> "WorkflowGetModel":
        return WorkflowGetModel(
            id=workflow.id,
            finished=workflow.finished,
            upload_activity=workflow.upload_activity,
        )
