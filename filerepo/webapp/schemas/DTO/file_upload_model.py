from typing import List, Optional
from pydantic import BaseModel

from filerepo.webapp.domain.file.file import File

class FileUploadModel(BaseModel):
    file_name: str
    file_type: str
    file_content: bytes