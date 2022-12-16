from typing import Optional, List

from sqlalchemy.orm.session import Session
from filerepo.webapp.domain.file.file_repository import FileRepository
from filerepo.webapp.domain.file.file import File
from filerepo.webapp.schemas.DTO.file.file_upload_request import FileUploadRequest


class FileRepositoryImpl(FileRepository):
    """FileRepositoryImpl implements CRUD operations related File entity using SQLAlchemy."""

    def __init__(self, session: Session):
        self.session: Session = session

    def find_by_id(self, id: int) -> File:
        try:
            file: File = self.session.query(File).filter_by(id=id).one()
        except:
            raise

        return file

    def find_all(self) -> List[File]:
        try:
            file_list: List[File] = self.session.query(File).all()
        except:
            raise

        return file_list

    def create(self, file: File) -> File:
        try:
            self.session.add(file)
            self.session.commit()
            return file
        except:
            raise

    def delete_by_id(self, id: int):
        try:
            file = self.session.query(File).get(id)
            self.session.delete(file)
            self.session.commit()
        except:
            raise

    def find_by_hash(self, hash) -> int:
        try:
            file = self.session.query(File).filter(File.file_hash == hash).one_or_none()
            if (file == None):
                return None
            return file.id
        except:
            raise

