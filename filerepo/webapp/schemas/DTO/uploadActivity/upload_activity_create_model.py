from typing import List, Optional
from pydantic import BaseModel

class UploadActivityCreateModel(BaseModel):
    upload_time: float
    file_name: str
    file_id: str