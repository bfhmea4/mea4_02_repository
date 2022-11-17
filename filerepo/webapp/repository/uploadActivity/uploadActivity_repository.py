from typing import Optional, List
import shortuuid
import hashlib
import time

from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm.session import Session

from filerepo.webapp.repository.uploadActivity.uploadActivity_dto import UploadActivityDTO
from filerepo.webapp.domain.uploadActivity.uploadActivity_repository import UploadActivityRepository
from filerepo.webapp.domain.uploadActivity.uploadActivity import UploadActivity
from filerepo.webapp.schemas.DTO.upload_activity_model import UploadActivityModel


class UploadActivityRepositoryImpl(UploadActivityRepository):
    """FileRepositoryImpl implements CRUD operations related File entity using SQLAlchemy."""

    def __init__(self, session: Session):
        self.session: Session = session

    def find_by_id(self, id: str) -> UploadActivityDTO:
        try:
            uploadActivity_dto = UploadActivity.from_entity(self.session.query(UploadActivity).filter_by(id=id).one())
        except:
            raise

        return uploadActivity_dto  # muss File zurückgegeben werden: .to_entity()

    def find_all(self) -> List[UploadActivityDTO]:
        try:
            uploadActivity_list = self.session.query(UploadActivity).all()
            filesDTO_list:List [UploadActivityDTO] = []
            for uploadActivity in uploadActivity_list:
                filesDTO_list.append(UploadActivityDTO.from_entity(uploadActivity))
        except:
            raise

        return uploadActivity_list

    def create(self, uploadActivityModel: UploadActivityModel) -> UploadActivity:
        try:
            upload_time: float = uploadActivityModel.upload_time
            upload_file_name: str = uploadActivityModel.file_name
            upload_file_id: str = uploadActivityModel.file_id
            uploadActivity = UploadActivity(upload_time=upload_time,file_name=upload_file_name,file_id=upload_file_id)
            self.session.add(uploadActivity)
            return uploadActivity
        except:
            raise

    def delete_by_id(self, id: int):
        try:
            uploadActivity = self.session.query(UploadActivity).get(id)
            self.session.delete(uploadActivity)
        except:
            raise
