from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator

def produce_value():
    # Return value is stored in XCom automatically
    return 42

def consume_value(x):
    print(f"Got value from upstream via XComArg: {x}")

with DAG(
    dag_id="04_xcom_basics",
    description="Pass a small value between tasks without decorators",
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False,
    tags=["tasks","xcom"],
) as dag:
    t1 = PythonOperator(task_id="produce_value", python_callable=produce_value)
    t2 = PythonOperator(task_id="consume_value", python_callable=consume_value, op_args=[t1.output])
    t1 >> t2
