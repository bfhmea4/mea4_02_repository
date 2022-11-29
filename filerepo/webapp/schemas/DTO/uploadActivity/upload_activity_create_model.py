from typing import List, Optional
from pydantic import BaseModel


class UploadActivityCreateModel(BaseModel):
    file_name: str
    file_id: int

    class Config:
        orm_mode = True
