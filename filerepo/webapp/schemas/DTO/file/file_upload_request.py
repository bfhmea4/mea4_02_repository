from pydantic import BaseModel


class FileUploadRequest(BaseModel):
    file_name: str
    file_type: str
    file_content: bytes

    class Config:
        orm_mode = True
