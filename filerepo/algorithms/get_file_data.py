import json
import os
from datetime import datetime


def get_file_information(file: str) -> str:
    size = os.path.getsize(file)
    last_modify= datetime.fromtimestamp(os.path.getmtime(file)).strftime('%Y-%m-%d')
    print(last_modify)
    creation_date = datetime.fromtimestamp(os.path.getctime(file)).strftime('%Y-%m-%d')
    file_type = os.path.splitext(file)

    data = {'size in bytes': size,
            'last Modify': last_modify,
            'creation Date': creation_date,
            'file typ': file_type[1]}
    json_file = json.loads(json.dumps(data))
    return json_file


