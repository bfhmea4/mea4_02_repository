import json
import os
from datetime import datetime
import magic
from ..webapp.schemas.schema import FileBase


def get_file_information(file_path: str) -> FileBase:
        file_size = os.path.getsize(file_path)
        file_name = os.path.basename(file_path)
        file_last_modified= datetime.fromtimestamp(os.path.getmtime(file_path)).strftime('%Y-%m-%d %H:%M')
        file_creation_time = datetime.fromtimestamp(os.path.getctime(file_path)).strftime('%Y-%m-%d %H:%M')

        data = {
        'file_name': file_name,
        'file_path': file_path,
        'file_size': file_size,
        'file_last_modified': file_last_modified,
        'file_creation_time': file_creation_time,
        'file_type': magic.from_file(file_path, mime=True)
        }

        file = FileBase(**data)

        return file


