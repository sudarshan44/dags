from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.amazon.aws.hooks.s3 import S3Hook
from datetime import datetime

def test_minio():
    hook = S3Hook(aws_conn_id="minio")

    client = hook.get_conn()

    response = client.list_buckets()

    print("Buckets:")
    for bucket in response["Buckets"]:
        print(bucket["Name"])

with DAG(
    dag_id="test_minio_connection",
    start_date=datetime(2026, 1, 1),
    schedule=None,
    catchup=False,
) as dag:

    test = PythonOperator(
        task_id="test_connection",
        python_callable=test_minio
    )
