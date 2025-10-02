from datetime import datetime, timedelta
import random
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.empty import EmptyOperator

def unstable_step():
    x = random.random()
    print(f"Random value: {x}")
    if x < 0.5:
        raise Exception("Simulated intermittent failure — retry me!")
    print("Success on this attempt.")

default_args = {
    "owner": "workshop",
    "retries": 2,
    "retry_delay": timedelta(seconds=10)
}

with DAG(
    dag_id="05_fail_and_retry",
    description="Demonstrates task failure & automatic retries (no decorators)",
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False,
    default_args=default_args,
    tags=["retries","errors","basics"],
) as dag:
    start = EmptyOperator(task_id="start")
    flaky = PythonOperator(task_id="flaky_task", python_callable=unstable_step)
    done = EmptyOperator(task_id="done")
    start >> flaky >> done
