from sqlalchemy.orm.session import Session

from filerepo.webapp.repository.workflow.workflow_dto import WorkflowDTO
from filerepo.webapp.domain.workflow.workflow_repository import WorkflowRepository
from filerepo.webapp.domain.workflow.workflow import Workflow
from filerepo.webapp.schemas.DTO.workflow.workflow_create_model import WorkflowCreateModel


class WorkflowRepositoryImpl(WorkflowRepository):
    """WorkflowRepositoryImpl implements CRUD operations related Workflow entity using SQLAlchemy."""

    def __init__(self, session: Session):
        self.session: Session = session

    def find_by_id(self, id: int) -> WorkflowDTO:
        try:
            NotImplementedError
        except:
            raise
        return NotImplementedError
    
    def find_workflow_by_upload_activity_id(self, upload_activity_id: int) -> WorkflowDTO:
        try:
            workflowDTO: WorkflowDTO = WorkflowDTO.from_entity(self.session.query(Workflow).filter_by(upload_activity_id=upload_activity_id).one())
        except:
            raise
        return workflowDTO

    def create(self, workflow_create_model: WorkflowCreateModel) -> Workflow:
        try:
            workflow = Workflow(finished=False, upload_activity=workflow_create_model.upload_activity)
            self.session.add(workflow)
            self.session.commit()
            return workflow
        except:
            raise

    def delete_by_id(self, id: int):
        try:
            NotImplementedError
        except:
            raise

    def update_status(self, status: bool, workflow_id: int):
        try:
            workflow: Workflow = self.session.query(Workflow).get(workflow_id)
            workflow.finished = status
            self.session.commit()
        except:
            raise
