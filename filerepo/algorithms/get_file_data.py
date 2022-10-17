import json
import os


def get_file_informations(file: str) -> str:
    size = os.path.getsize(file)
    lastModify= os.path.getmtime(file)
    creationDate = os.path.getctime(file)
    fileType = os.path.splitext(file)

    data = {"size: ": size,
            "last Modify: ": lastModify,
            "creation Date: ": creationDate,
            "file typ: ": fileType}
    json_file = json.loads(json.dumps(data))
    return json_file


