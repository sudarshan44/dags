from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator
from datetime import datetime

with DAG(
    dag_id="postgres_test_dag",
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False,
    tags=["postgres"],
) as dag:

    test_query = PostgresOperator(
        task_id="test_postgres_connection",
        postgres_conn_id="postgres",
        sql="""
        SELECT * FROM pg_tables LIMIT 5;
        """,
    )
