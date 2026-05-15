from airflow import DAG
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator
from datetime import datetime

with DAG(
    dag_id="postgres_test_dag",
    start_date=datetime(2025, 1, 1),
    schedule=None,
    catchup=False,
) as dag:

    test_postgres = SQLExecuteQueryOperator(
        task_id="test_postgres",
        conn_id="postgres",
        sql="SELECT * FROM budgetary_scheme_expenditure_details LIMIT 5;",
        show_return_value_in_logs=True,
    )
