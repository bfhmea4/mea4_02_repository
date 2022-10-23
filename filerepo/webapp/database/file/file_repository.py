from typing import Optional, List

from filerepo.webapp.database.file.file_dto import FileDTO
from filerepo.webapp.database.file_system import FileSystem
from filerepo.webapp.domain.file.file_repository import FileRepository
from filerepo.webapp.domain.file.file import File


class FileRepositoryImpl(FileRepository):
    """FileRepositoryImpl implements CRUD operations related File entity using SQLAlchemy."""

    def __init__(self, file_system: FileSystem):
        self.file_system: FileSystem = file_system

    def find_by_id(self, id: str) -> FileDTO:
        try:
            file_dto = self.file_system.read(id)
        except:
            raise

        return file_dto  # muss File zurückgegeben werden: .to_entity()

    def find_all(self) -> List[FileDTO]:
        try:
            files_list = self.file_system.list_files()
        except:
            raise

        return files_list

    def create(self, file: File):
        file_dto = FileDTO.from_entity(file)
        try:
            self.file_system.write(file_dto)
        except:
            raise

    def delete_by_id(self, id: str):
        try:
            self.file_system.delete(id)
        except:
            raise
