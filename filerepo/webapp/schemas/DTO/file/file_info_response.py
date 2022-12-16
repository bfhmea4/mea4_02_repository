from pydantic import BaseModel

from filerepo.webapp.domain.file.file import File


class FileInfoGetResponse(BaseModel):
    id: str
    file_name: str
    file_size: float
    file_type: str
    file_hash: str
    file_creation_time: str
    file_update_time: str

    @staticmethod
    def from_entity(file: File) -> "FileInfoGetResponse":
        return FileInfoGetResponse(
            id=file.id,
            file_name=file.file_name,
            file_size=file.file_size,
            file_type=file.file_type,
            file_hash=file.file_hash,
            file_creation_time=file.file_creation_time,
            file_update_time=file.file_update_time,
        )
