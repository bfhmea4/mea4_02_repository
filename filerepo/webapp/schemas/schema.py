from typing import List, Optional
from pydantic import BaseModel

class FileUploadModel(BaseModel):
    file_name: str
    file_content: bytes

class FileListModel(BaseModel):
    file_list: [File]
       

class Upload():
    id: int
    file: str
    filename: str
    timestamp: str

    
