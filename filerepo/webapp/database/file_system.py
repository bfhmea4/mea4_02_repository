from typing import Union

from webapp.domain.file import File
from webapp.database.file import FileDTO


class FileSystem():

    def __init__(self, basedir: str):
        self.basedir = basedir
        self.directory = {}

    def write(self, file: File) -> FileDTO:
         self.directory[file.id] = file.file_content
         return FileDTO.from_entity(file)
    
    def read(self, id: int) -> bytes:
        return self.directory[id]

    def list_files(self) -> FileDTO:




