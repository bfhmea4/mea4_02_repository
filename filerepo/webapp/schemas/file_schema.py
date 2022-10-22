from typing import List, Optional
from pydantic import BaseModel

from filerepo.webapp.domain.file.file import File

class FileUploadModel(BaseModel):
    file_name: str
    file_type: str
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

class FileInfoGetModel(BaseModel):
    id: str
    file_name: str
    file_size: float
    file_type: str
    file_hash: str
    file_creation_time: str
    file_update_time: str

    @staticmethod
    def from_entity(file: File) -> "FileInfoGetModel":
        return FileInfoGetModel(
            id=file.id,
            file_name=file.file_name,
            file_size=file.file_size,
            file_type=file.file_type,
            file_hash=file.file_hash,
            file_creation_time=file.file_creation_time,
            file_update_time=file.file_update_time,
        )

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
       

    
