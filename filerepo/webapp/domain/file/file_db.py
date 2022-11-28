from typing import Optional
from sqlalchemy import Column, Float, Integer, String, LargeBinary
from filerepo.webapp.repository.database import Base

class File(Base):

    """File represents your collection of files as an entity."""
    __tablename__ = "Files"
    id: int = Column(Integer, primary_key=True, nullable=False)
    file_name: str = Column(String, nullable=False)
    file_size: float = Column(Float, nullable=False)
    file_type: str = Column(String, nullable=False)
    file_hash: str = Column(String, nullable=False)
    file_content: Optional[bytes] = Column(LargeBinary,nullable=False)
    file_creation_time: Optional[float] = Column(Float, nullable=False)
    file_update_time: Optional[float] = Column(Float, nullable=False)

    def __eq__(self, o: object) -> bool:
        if isinstance(o, File):
            return self.id == o.id

        return False