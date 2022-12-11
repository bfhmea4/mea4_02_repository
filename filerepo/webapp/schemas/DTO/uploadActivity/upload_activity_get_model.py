from typing import List, Optional
from pydantic import BaseModel

from filerepo.webapp.domain.uploadActivity.uploadActivity import UploadActivity


class UploadActivityGetModel(BaseModel):
    id: str
    upload_time: float
    file_name: str
    file_id: int

    class Config:
        orm_mode = True

    @staticmethod
    def from_entity(upload_activity: UploadActivity) -> "UploadActivityGetModel":
        return UploadActivityGetModel(
            id=upload_activity.id,
            upload_time=upload_activity.upload_time,
            file_name=upload_activity.file_name,
            file_id=upload_activity.file_id
        )
