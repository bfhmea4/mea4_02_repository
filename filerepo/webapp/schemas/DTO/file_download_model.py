from typing import List, Optional
from pydantic import BaseModel

from filerepo.webapp.domain.file.file import File

class FileDownloadModel(BaseModel):
    file_name: str
    file_type: str
    file_content: bytes

    @staticmethod
    def from_entity(file: File) -> "FileDownloadModel":
        return FileDownloadModel(
            file_name=file.file_name,
            file_type=file.file_type,
            file_content=file.file_content,
        )