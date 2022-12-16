from sqlalchemy import Column, Float, Integer, String
from filerepo.webapp.repository.database import Base


class UploadActivity(Base):

    """Upload represents each upload performed by user."""
    __tablename__ = "UploadActivities"
    id: int = Column(Integer, primary_key=True, nullable=False)
    upload_time: float = Column(Float,nullable=False)
    file_name: str = Column(String,nullable=False)
    file_id: int = Column(Integer,nullable=False)

    def __eq__(self, o: object) -> bool:
        if isinstance(o, UploadActivity):
            return self.id == o.id

        return False