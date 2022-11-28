from typing import List
import time

from sqlalchemy.orm.session import Session

from filerepo.webapp.repository.uploadActivity.uploadActivity_dto import UploadActivityDTO
from filerepo.webapp.domain.uploadActivity.uploadActivity_repository import UploadActivityRepository
from filerepo.webapp.domain.uploadActivity.uploadActivity import UploadActivity
from filerepo.webapp.schemas.DTO.uploadActivity.upload_activity_create_model import UploadActivityCreateModel


class UploadActivityRepositoryImpl(UploadActivityRepository):
    """FileRepositoryImpl implements CRUD operations related File entity using SQLAlchemy."""

    def __init__(self, session: Session):
        self.session: Session = session

    def find_by_id(self, id: str) -> UploadActivityDTO:
        try:
            uploadActivity_dto = UploadActivityDTO.from_entity(self.session.query(UploadActivity).filter_by(id=id).one())
        except:
            raise

        return uploadActivity_dto

    def find_all(self) -> List[UploadActivityDTO]:
        try:
            uploadActivity_list = self.session.query(UploadActivity).all()
            filesDTO_list:List [UploadActivityDTO] = []
            for uploadActivity in uploadActivity_list:
                filesDTO_list.append(UploadActivityDTO.from_entity(uploadActivity))
        except:
            raise

        return uploadActivity_list

    def create(self, uploadActivityCreateModel: UploadActivityCreateModel) -> UploadActivity:
        try:
            upload_time: float = time.time()
            upload_file_name: str = uploadActivityCreateModel.file_name
            upload_file_id: str = uploadActivityCreateModel.file_id
            uploadActivity = UploadActivity(upload_time=upload_time,file_name=upload_file_name,file_id=upload_file_id)
            self.session.add(uploadActivity)
            self.session.commit()
            return uploadActivity
        except:
            raise

    def delete_by_id(self, id: int):
        try:
            uploadActivity = self.session.query(UploadActivity).get(id)
            self.session.delete(uploadActivity)
            self.session.commit()
        except:
            raise
