from airflow import DAG
from airflow.providers.cncf.kubernetes.operators.pod import KubernetesPodOperator
from datetime import datetime

with DAG(
    dag_id="k8s_test",
    start_date=datetime(2026, 1, 1),
    schedule=None,
    catchup=False,
) as dag:

    test = KubernetesPodOperator(
        task_id="test_pod",
        namespace="default",
        image="busybox",
        cmds=["sh", "-c"],
        arguments=["echo 'Airflow can connect to Kubernetes successfully'"],
        get_logs=True,
    )
