from pydantic import BaseModel

from filerepo.webapp.domain.file.file import File

# Todo: Changed to response
class FileGetResponse(BaseModel):
    id: int
    file_name: str

    @staticmethod
    def from_entity(file: File) -> "FileGetResponse":
        return FileGetResponse(
            id=file.id,
            file_name=file.file_name,
        )
