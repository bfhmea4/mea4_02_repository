from typing import Any, TypedDict

from .file.file_dto import FileDTO
from ..domain.file import File


class FileSystem():

    def __init__(self, basedir: str):
        self.basedir = basedir
        self.directory = {}  # TypedDict[str, FileDTO] #funktioniert?

    def write(self, file: FileDTO):
        self.directory[file.id] = file.to_entity()

    def read(self, id: str) -> FileDTO:
        return FileDTO.from_entity(self.directory.get(id))

    def delete(self, id: str):
        del self.directory[id]

    def list_files(self):
        return self.directory.items()
