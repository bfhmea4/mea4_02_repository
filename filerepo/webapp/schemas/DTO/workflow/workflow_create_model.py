from pydantic import BaseModel
from typing import Optional
import datetime

class WorkflowCreateModel(BaseModel):
    finished: Optional[datetime.datetime]
    upload_activity: int

    class Config:
        orm_mode = True
