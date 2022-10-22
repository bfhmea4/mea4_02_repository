from typing import Union, Dict, Any

from .file.file_dto import FileDTO
from ..domain.file import File


class FileSystem():

    def __init__(self, basedir: str):
        self.basedir = basedir
        self.directory = {}

    def write(self, file: FileDTO) -> File: #Upload
         self.directory[file.id] = file
         return FileDTO.to_entity(file)
    
    def read(self, id: str) -> bytes:
        return self.directory[id]

    def list_files(self) -> dict[Any, Any]:
        return self.directory




