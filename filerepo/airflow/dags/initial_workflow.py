import time
from datetime import datetime
from textwrap import dedent
from typing import List

from airflow import DAG
from airflow.operators.python import PythonVirtualenvOperator

# ToDo: Clean up DAG
# ToDo: Figure out how to trigger DAGs in a clean way
# ToDo: Check if pandas are the best way
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'start_date' : datetime(2021, 1,1),
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    # 'end_date': datetime(2016, 1, 1),
    # 'wait_for_downstream': False,
    # 'dag': dag,
    # 'sla': timedelta(hours=2),
    # 'execution_timeout': timedelta(seconds=300),
    # 'on_failure_callback': some_function,
    # 'on_success_callback': some_other_function,
    # 'on_retry_callback': another_function,
    # 'sla_miss_callback': yet_another_function,
    # 'trigger_rule': 'all_success'
}


def black_white_ratio():
    from typing import Iterator
    import sqlalchemy as db
    import numpy as np
    import pandas as pd
    engine = db.create_engine('sqlite:///../db/sqlite.db')
    files=pd.read_sql('select * from Files',engine)
    entries=files.values
    perform_analyse = []
    for entry in entries:
        if "image" in entry[3]:
            nparr = np.frombuffer(entry[5], np.uint8)
            print("Black: " + str(np.sum(nparr == 255)))
            print("White: " + str(np.sum(nparr == 0)))
            print("Black/White ratio: " + str(np.sum(nparr == 255)/np.sum(nparr == 0)))

    #     if upload.upload_time > time.time()-300:
    #         perform_analyse+=upload
    # files: List[FileDTO] = []
    #file = requests.get("http://0.0.0.0:8000/files/2")


with DAG(
    'BlackWhitePixels',
    default_args=default_args,
    description='A DAG kick off different analyses',
    start_date=datetime(2021, 1,1),
    catchup=False,
    schedule_interval=('*/5 * * * *'),
    tags=['pixels'],
) as dag:
    t1 = PythonVirtualenvOperator(
    task_id="check_new_entries",
    python_callable=black_white_ratio,
    requirements=["sqlalchemy", "pandas"],
    system_site_packages=False,
)