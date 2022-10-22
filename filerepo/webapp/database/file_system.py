from typing import TypedDict, List

from .file.file_dto import FileDTO
from ..domain.file import File


class FileSystem():

    def __init__(self):
        self.directory = {str: FileDTO}  # TypedDict[str, FileDTO] #funktioniert?

    def write(self, file: FileDTO):
        self.directory[file.id] = file.to_entity()

    def read(self, id: str) -> FileDTO:
        return FileDTO.from_entity(self.directory.get(id))

    def delete(self, id: str):
        del self.directory[id]

    def list_files(self) -> List[FileDTO]:
        return self.directory.items()
