from typing import List, Optional
from pydantic import BaseModel

class FileUploadModel(BaseModel):
    file_name: str
    file_content: bytes

class FileGetModel(BaseModel):
    id: int
    file_name: str

class FileListModel(BaseModel):
    file_list: List[FileGetModel]
       

    
