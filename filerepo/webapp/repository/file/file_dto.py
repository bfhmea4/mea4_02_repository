from filerepo.webapp.domain.file.file import File


class FileDTO():
    """FileDTO is a data transfer object associated with File entity."""

    def __init__(self, file):
        self.id = file.id
        self.file_name = file.file_name
        self.file_size = file.file_size
        self.file_type = file.file_type
        self.file_hash = file.file_hash
        self.file_content = file.file_content
        self.file_creation_time = file.file_creation_time
        self.file_update_time = file.file_update_time

    def to_entity(self) -> File:
        return File(
            id=self.id,
            file_name=self.file_name,
            file_size=self.file_size,
            file_type=self.file_type,
            file_hash=self.file_hash,
            file_content=self.file_content,
            file_creation_time=self.file_creation_time,
            file_update_time=self.file_update_time,
        )

    @staticmethod
    def from_entity(file: File) -> "FileDTO":
        return FileDTO(file)