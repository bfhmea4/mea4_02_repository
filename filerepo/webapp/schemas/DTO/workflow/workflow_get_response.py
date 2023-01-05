from pydantic import BaseModel
from typing import Optional
import datetime
from filerepo.webapp.domain.workflow.workflow import Workflow


class WorkflowGetResponse(BaseModel):
    id: int
    finished: Optional[datetime.datetime]
    upload_activity: int

    @staticmethod
    def from_entity(workflow: Workflow) -> "WorkflowGetResponse":
        return WorkflowGetResponse(
            id=workflow.id,
            finished=workflow.finished,
            upload_activity=workflow.upload_activity,
        )
