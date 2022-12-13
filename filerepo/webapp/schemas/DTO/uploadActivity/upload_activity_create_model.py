from pydantic import BaseModel

#ToDo: rename request
class UploadActivityCreateModel(BaseModel):
    file_name: str
    file_id: int

    class Config:
        orm_mode = True
