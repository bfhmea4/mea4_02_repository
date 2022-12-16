from typing import List, Optional
from pydantic import BaseModel

class FileUploadModel(BaseModel):
    file_name: str
    file_type: str
    file_content: bytes

    class Config:
        orm_mode = True