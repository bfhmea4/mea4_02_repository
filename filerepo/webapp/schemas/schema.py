from typing import List, Optional
from pydantic import BaseModel

class FileBase(BaseModel):
    file_name: str
    file_path: str
    file_size: float
    file_type: str
    file_hash: Optional[str] = None
    file_creation_time: str
    file_last_modified: str
       

class Upload():
    id: int
    file: str
    filename: str
    timestamp: str

    
