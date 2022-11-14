import time
from typing import Optional, List

class Upload:

    """Upload represents each upload performed by user."""

    def __init__(self,id: str, file_name: str, file_hash: str, file_id):
        self.id: str = id
        self.file_hash: str = file_hash
        self.file_name: List[str] = file_name
        self.upload_time: List[float] = [time.time()]
        self.file: str = file_id

    def addFile(self, file_name):
        self.file_name.append(file_name)
        self.upload_time.append(time.time())

    def __eq__(self, o: object) -> bool:
        if isinstance(o, Upload):
            return self.id == o.id

        return False