from datetime import datetime
import random
from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import BranchPythonOperator

def choose_path():
    return "path_a" if random.random() < 0.5 else "path_b"

with DAG(
    dag_id="03_branching",
    description="Conditional paths using BranchPythonOperator",
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False,
    tags=["branching","dependencies"],
) as dag:
    start = EmptyOperator(task_id="start")
    branch = BranchPythonOperator(task_id="branch_decision", python_callable=choose_path)
    path_a = EmptyOperator(task_id="path_a")
    path_b = EmptyOperator(task_id="path_b")
    join = EmptyOperator(task_id="join", trigger_rule="none_failed_min_one_success")

    start >> branch
    branch >> [path_a, path_b] >> join
