from filerepo.webapp.domain.uploadActivity.uploadActivity import UploadActivity


class UploadActivityDTO():
    """FileDTO is a data transfer object associated with File entity. Represented as entity in the DB using SQLAlchemy"""

    def __init__(self, uploadActivity):

        self.id: str = uploadActivity.id
        self.upload_time: float = uploadActivity.upload_time
        self.file_name: str = uploadActivity.file_name
        self.file_id: int = uploadActivity.file_id


    def to_entity(self) -> UploadActivity:
        return UploadActivity(
            id=self.id,
            upload_time=self.upload_time,
            file_name=self.file_name,
            file_id=self.file_id,
        )

    @staticmethod
    def from_entity(uploadActivity: UploadActivity) -> "UploadActivityDTO":
        return UploadActivityDTO(uploadActivity)