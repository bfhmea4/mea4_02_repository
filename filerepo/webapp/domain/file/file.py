from typing import Optional

class File:
    """File represents your collection of files as an entity."""

    def __init__(
        self,
        id: str,
        file_name: str,
        file_path: str,
        file_size: float,
        file_type: str,
        file_hash: str,
        file_content: Optional[bytes] = None,
        file_creation_time: Optional[int] = None,
        file_update_time: Optional[int] = None,
    ):
        self.id: str = id
        self.file_name: str = file_name
        self.file_path: str = file_path
        self.file_size: float = file_size
        self.file_type: str = file_type
        self.file_hash: str = file_hash
        self.file_content: Optional[bytes] = file_content
        self.file_creation_time: Optional[int] = file_creation_time
        self.file_update_time: Optional[int] = file_update_time

    def __eq__(self, o: object) -> bool:
        if isinstance(o, Book):
            return self.id == o.id

        return False