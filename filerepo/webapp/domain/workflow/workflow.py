from sqlalchemy import Column, Integer, DateTime
import datetime
from filerepo.webapp.repository.database import Base


class Workflow(Base):
    """Workflow represents each workflow triggered by a uploadActivitx."""
    __tablename__ = "Workflow"
    id: int = Column(Integer, primary_key=True, nullable=False)
    finished: datetime = Column(DateTime(timezone=True), nullable=True)
    upload_activity: int = Column(Integer, nullable=False)

    def __eq__(self, o: object) -> bool:
        if isinstance(o, Workflow):
            return self.id == o.id
        return False
