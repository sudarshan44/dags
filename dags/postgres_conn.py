from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id="postgres_test_dag",
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False,
) as dag:

    test_task = BashOperator(
        task_id="test_task",
        bash_command="echo PostgreSQL DAG Loaded Successfully"
    )
