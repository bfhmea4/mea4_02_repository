from datetime import timedelta
from textwrap import dedent

from airflow import DAG
from airflow.operators.python import PythonVirtualenvOperator

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
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
    """
    Example function that will be performed in a virtual environment.

    Importing at the module level ensures that it will not attempt to import the
    library before it is installed.
    """
    from time import sleep

    from colorama import Back, Fore, Style

    print(Fore.RED + 'some red text')
    print(Back.GREEN + 'and with a green background')
    print(Style.DIM + 'and in dim text')
    print(Style.RESET_ALL)
    for _ in range(10):
        print(Style.DIM + 'Please wait...', flush=True)
        sleep(10)
    print('Finished')

with DAG(
    'image',
    default_args=default_args,
    description='A DAG for analysing images',
    schedule_interval=timedelta(days=1),
    start_date=days_ago(2),
    tags=['example'],
) as dag:
    t1 = PythonVirtualenvOperator(
    task_id="black_white_ratio",
    python_callable=black_white_ratio,
    requirements=["colorama==0.4.0"],
    system_site_packages=False,
)