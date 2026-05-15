from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator
from datetime import datetime

with DAG(
    dag_id="postgres_test_dag",
    start_date=datetime(2026, 1, 1),
    schedule=None,
    catchup=False,
) as dag:

    test_postgres = PostgresOperator(
        task_id="test_postgres",
        postgres_conn_id="postgres",
        sql="select * from budgetary_scheme_expenditure_details LIMIT 5;",
    )
