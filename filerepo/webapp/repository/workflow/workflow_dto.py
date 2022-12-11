from filerepo.webapp.domain.workflow.workflow import Workflow


class WorkflowDTO():
    """WorkflowDTO is a data transfer object associated with Workflow entity. Represented as entity in the DB using SQLAlchemy"""

    def __init__(self, workflow: Workflow):

        self.id: int = workflow.id
        self.finished: bool = workflow.finished
        self.upload_activity: int = workflow.upload_activity


    def to_entity(self) -> Workflow:
        return Workflow(
            id=self.id,
            finished=self.finished,
            upload_activity=self.upload_activity,
        )

    @staticmethod
    def from_entity(workflow: Workflow) -> "WorkflowDTO":
        return WorkflowDTO(workflow)