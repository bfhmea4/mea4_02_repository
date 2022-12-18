from pydantic import BaseModel

from filerepo.webapp.domain.file.file import File


class FileDownloadResponse(BaseModel):
    file_name: str
    file_type: str
    file_content: bytes

    @staticmethod
    def from_entity(file: File) -> "FileDownloadResponse":
        return FileDownloadResponse(
            file_name=file.file_name,
            file_type=file.file_type,
            file_content=file.file_content,
        )
