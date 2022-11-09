from typing import List, Optional
from pydantic import BaseModel

from filerepo.webapp.domain.file.file import File

class FileGetModel(BaseModel):
    id: str
    file_name: str

    @staticmethod
    def from_entity(file: File) -> "FileGetModel":
        return FileGetModel(
            id=file.id,
            file_name=file.file_name,
        )