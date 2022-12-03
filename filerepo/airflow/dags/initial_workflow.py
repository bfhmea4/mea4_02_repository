import time
from datetime import datetime
from textwrap import dedent
from typing import List

from airflow import DAG
from airflow.operators.python import PythonVirtualenvOperator

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
    import requests
    import numpy as np

    # def get_session() -> Iterator[Session]:
    #     session: Session = SessionLocal()
    #     try:
    #         yield session
    #     finally:
    #         session.close()
    #
    # def fnc_upload_activity_repository(session: Session = get_session) -> UploadActivityRepository:
    #     repository: UploadActivityRepositoryImpl = UploadActivityRepositoryImpl(session)
    #     return repository
    #
    # def fnc_file_repository(session: Session = get_session) -> FileRepository:
    #     repository: FileRepositoryImpl = FileRepositoryImpl(session)
    #     return repository
    #
    # file_repository = fnc_file_repository()
    # upload_activity_repository = fnc_upload_activity_repository()
    #
    # uploads: List[UploadActivityDTO] = upload_activity_repository.find_all()
    # perform_analyse: List[UploadActivityDTO] = []
    # for upload in uploads:
    #     if upload.upload_time > time.time()-300:
    #         perform_analyse+=upload
    # files: List[FileDTO] = []
    file = requests.get("http://0.0.0.0:8000/files/2")
    nparr = np.frombuffer(file.content, np.uint8)
    print("Black: " + np.sum(nparr == 255))
    print("White: " + np.sum(nparr == 0))
    print("Black/White ratio: " + np.sum(nparr == 255)/np.sum(nparr == 0))

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
    requirements=["requests<=2.28.1", "opencv-python"],
    system_site_packages=False,
)