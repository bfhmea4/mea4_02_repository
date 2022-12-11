from sqlalchemy import Column, Boolean, Integer
from filerepo.webapp.repository.database import Base


class Workflow(Base):
    """Workflow represents each workflow triggered by a uploadActivitx."""
    __tablename__ = "workflow"
    id: int = Column(Integer, primary_key=True, nullable=False)
    finished: bool = Column(Boolean, nullable=False)
    upload_activity: int = Column(Integer, nullable=False)

    def __eq__(self, o: object) -> bool:
        if isinstance(o, Workflow):
            return self.id == o.id
        return False
