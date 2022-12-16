from typing import List, Optional
from pydantic import BaseModel

from filerepo.webapp.domain.file.file import File


class FileGetRequest(BaseModel):
    id: int
    file_name: str

    @staticmethod
    def from_entity(file: File) -> "FileGetRequest":
        return FileGetRequest(
            id=file.id,
            file_name=file.file_name,
        )
