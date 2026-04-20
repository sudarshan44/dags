
from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    "owner": "airflow",
    "retries": 1,
    "retry_delay": timedelta(minutes=1),
}

with DAG(
    dag_id="test_dag",
    default_args=default_args,
    description="Simple test DAG to verify Airflow setup",
    start_date=datetime(2024, 1, 1),
    schedule_interval=None,   # manual trigger
    catchup=False,
    tags=["test"],
) as dag:

    print_date = BashOperator(
        task_id="print_date",
        bash_command="date"
    )

    print_message = BashOperator(
        task_id="print_message",
        bash_command="echo 'Airflow DAG is working successfully!'"
    )

    print_date >> print_message
