from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator

def say_hello():
    print("👋 Hello from PythonOperator!")

with DAG(
    dag_id="00_hello_operator",
    description="Smallest possible DAG with one PythonOperator task",
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False,
    tags=["basics","operators"],
) as dag:
    hello = PythonOperator(
        task_id="say_hello",
        python_callable=say_hello,
    )
