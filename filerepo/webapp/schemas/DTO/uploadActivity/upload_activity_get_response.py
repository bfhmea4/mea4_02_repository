from pydantic import BaseModel

from filerepo.webapp.domain.uploadActivity.uploadActivity import UploadActivity


class UploadActivityGetResponse(BaseModel):
    id: str
    upload_time: float
    file_name: str
    file_id: int

    class Config:
        orm_mode = True

    @staticmethod
    def from_entity(uploadActivity: UploadActivity) -> "UploadActivityGetResponse":
        return UploadActivityGetResponse(
            id=uploadActivity.id,
            upload_time=uploadActivity.upload_time,
            file_name=uploadActivity.file_name,
            file_id=uploadActivity.file_id
        )
