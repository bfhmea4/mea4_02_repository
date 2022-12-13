from typing import Optional, List
import shortuuid
import hashlib
import time

from filerepo.webapp.repository.file.file_dto import FileDTO
from sqlalchemy.orm.session import Session
from filerepo.webapp.domain.file.file_repository import FileRepository
from filerepo.webapp.domain.file.file import File
from filerepo.webapp.schemas.DTO.file_upload_model import FileUploadModel


class FileRepositoryImpl(FileRepository):
    """FileRepositoryImpl implements CRUD operations related File entity using SQLAlchemy."""

    def __init__(self, session: Session):
        self.session: Session = session

    #ToDo: Repositories do not return DTO
    def find_by_id(self, id: int) -> FileDTO:
        try:
            file_dto = FileDTO.from_entity(self.session.query(File).filter_by(id=id).one())
        except:
            raise

        return file_dto

    def find_all(self) -> List[FileDTO]:
        try:
            file_list = self.session.query(File).all()
            fileDTO_list: List[FileDTO] = []
            for file in file_list:
                fileDTO_list.append(FileDTO.from_entity(file))
        except:
            raise

        return fileDTO_list

    #ToDo: File in not Model
    def create(self, file_uploaded: FileUploadModel) -> File:
        try:
            hash = hashlib.sha256(file_uploaded.file_content).hexdigest()
            current_time = time.time()
            file = File(file_name=file_uploaded.file_name, file_size=len(file_uploaded.file_content),
                        file_type=file_uploaded.file_type, file_hash=hash, file_content=file_uploaded.file_content,
                        file_creation_time=current_time, file_update_time=current_time)
            self.session.add(file)
            self.session.commit()
            return file
        except:
            raise

    def delete_by_id(self, id: int):
        try:
            uploadActivity = self.session.query(File).get(id)
            self.session.delete(uploadActivity)
            self.session.commit()
        except:
            raise

    def find_by_hash(self, hash):
        try:
            file = self.session.query(File).filter(File.file_hash == hash).one_or_none()
            if (file == None):
                return None
            return file.id
        except:
            raise
