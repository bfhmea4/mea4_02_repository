from typing import Optional, List
import shortuuid
import hashlib
import time

from filerepo.webapp.repository.file.file_dto import FileDTO
from filerepo.webapp.repository.file_system import FileSystem
from filerepo.webapp.domain.file.file_repository import FileRepository
from filerepo.webapp.domain.file.file import File
from filerepo.webapp.schemas.DTO.file_upload_model import FileUploadModel


class FileRepositoryImpl(FileRepository):
    """FileRepositoryImpl implements CRUD operations related File entity using File_System."""

    def __init__(self, file_system: FileSystem):
        self.file_system: FileSystem = file_system

    def find_by_id(self, id: str) -> FileDTO:
        try:
            file_dto = FileDTO.from_entity(self.file_system.read(id))
        except:
            raise

        return file_dto

    def find_all(self) -> List[FileDTO]:
        try:
            files_list = self.file_system.list_files()
            filesDTO_list:List [FileDTO] = []
            for file in files_list:
                filesDTO_list.append(FileDTO.from_entity(file))
        except:
            raise

        return filesDTO_list

    def create(self, file_uploaded: FileUploadModel) -> File:
        try:
            id: str = shortuuid.uuid()
            file_type: str = file_uploaded.file_type
            hash = hashlib.sha256(file_uploaded.file_content).hexdigest()
            current_time = time.time()
            file = File(id,file_uploaded.file_name,len(file_uploaded.file_content),file_type,hash,file_uploaded.file_content,current_time,current_time)
            self.file_system.write(file)
            return file
        except:
            raise

    def delete_by_id(self, id: str):
        try:
            self.file_system.delete(id)
        except:
            raise

    def find_by_hash(self, hash):
        try:
            files = self.find_all()
            for file in files:
                if file.file_hash == hash:
                    return file.id
        except:
            raise
