import time
from typing import Optional, List
from sqlalchemy import Column, Float, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class UploadActivity(Base):

    """Upload represents each upload performed by user."""
    __tablename__ = "UploadActivities"
    id: str = Column(Integer, primary_key=True, nullable=False)
    upload_time: float = Column(Float,nullable=False)
    file_name: str = Column(String,nullable=False)
    file_id: int = Column(Integer,nullable=False)

    def __eq__(self, o: object) -> bool:
        if isinstance(o, UploadActivity):
            return self.id == o.id

        return False