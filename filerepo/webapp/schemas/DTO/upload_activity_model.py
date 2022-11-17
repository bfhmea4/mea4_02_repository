from typing import List, Optional
from pydantic import BaseModel

class UploadActivityModel(BaseModel):
    upload_time: float
    file_name: str
    file_id: str