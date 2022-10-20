from typing import Union

from webapp.domain.file import File
from webapp.database.file import FileDTO


class FileSystem():

    def __init__(self, basedir: str):
        self.basedir = basedir
        self.directory = {}

    def write(file: File) -> FileDTO:
         self.directory[file.id] = file_content
         return FileDTO.from_entity(file)
    
    def read(id: int) -> bytes:
        return self.directory[id]

    def list_files() -> FileDTO



