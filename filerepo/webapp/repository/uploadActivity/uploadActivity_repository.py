from typing import List

from sqlalchemy.orm.session import Session

from filerepo.webapp.domain.uploadActivity.uploadActivity_repository import UploadActivityRepository
from filerepo.webapp.domain.uploadActivity.uploadActivity import UploadActivity


class UploadActivityRepositoryImpl(UploadActivityRepository):
    """FileRepositoryImpl implements CRUD operations related File entity using SQLAlchemy."""

    def __init__(self, session: Session):
        self.session: Session = session

    def find_by_id(self, id: str) -> UploadActivity:
        try:
            upload_activity: UploadActivity = self.session.query(UploadActivity).filter_by(id=id).one()
        except:
            raise

        return upload_activity

    def find_all(self) -> List[UploadActivity]:
        try:
            return self.session.query(UploadActivity).all()
        except:
            raise

    def create(self, upload_activity: UploadActivity) -> UploadActivity:
        try:
            self.session.add(upload_activity)
            self.session.commit()
            return upload_activity
        except:
            raise

    def delete_by_id(self, id: int):
        try:
            uploadActivity = self.session.query(UploadActivity).get(id)
            self.session.delete(uploadActivity)
            self.session.commit()
        except:
            raise
