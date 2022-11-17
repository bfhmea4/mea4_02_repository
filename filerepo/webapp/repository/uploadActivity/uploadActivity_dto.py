from filerepo.webapp.domain.uploadActivity.uploadActivity import UploadActivity


class UploadActivityDTO():
    """FileDTO is a data transfer object associated with File entity."""

    def __init__(self, uploadActivity):

        self.id: str = uploadActivity.id
        self.file_name: str = uploadActivity.file_name
        self.upload_time: float = uploadActivity.upload_time
        self.file_id: str = uploadActivity.file_id


    def to_entity(self) -> UploadActivity:
        return UploadActivity(
            id=self.id,
            file_name=self.file_name,
            upload_time=self.upload_time,
            file_id=self.file_id,
        )

    @staticmethod
    def from_entity(uploadActivity: UploadActivity) -> "UploadActivityDTO":
        return UploadActivityDTO(uploadActivity)