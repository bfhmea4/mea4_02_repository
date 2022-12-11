from pydantic import BaseModel


class WorkflowCreateModel(BaseModel):
    finished: bool
    upload_activity: int

    class Config:
        orm_mode = True
