from __future__ import annotations
from datetime import datetime
from airflow.decorators import dag, task

@dag(
    dag_id="hello",
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False,
    tags=["hello"],
)
def hello():
    @task
    def say_hello():
        print("Hello from Airflow in Codespaces!")
    say_hello()

hello()
