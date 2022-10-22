from typing import List, Optional
from pydantic import BaseModel

from ..domain.file.file import File

class FileUploadModel(BaseModel):
    file_name: str
    file_content: bytes

class FileGetModel(BaseModel):
    id: str
    file_name: str

    @staticmethod
    def from_entity(file: File) -> "FileGetModel":
        return FileGetModel(
            id=file.id,
            file_name=file.file_name,
        )

class FileListModel(BaseModel):
    file_list: List[FileGetModel]

class FileDownloadModel(BaseModel):
    file_name: str
    file_content: bytes

    @staticmethod
    def from_entity(file: File) -> "FileDownloadModel":
        return FileDownloadModel(
            file_name=file.file_name,
            file_content=file.file_content,
        )
       

    
