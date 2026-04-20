from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator

with DAG(
    dag_id="test_dag",
    start_date=datetime(2024, 1, 1),
    schedule=None,   # ✅ correct for Airflow 3
    catchup=False,
) as dag:

    t1 = BashOperator(
        task_id="print_date",
        bash_command="date",
    )

    t2 = BashOperator(
        task_id="hello",
        bash_command="echo 'Hello Airflow'",
    )

    t1 >> t2
