from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator

def print_python():
    print("This ran after the Bash task.")

with DAG(
    dag_id="01_bash_and_python",
    description="Demonstrates two operators and a simple dependency",
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False,
    tags=["operators","dependencies"],
) as dag:
    t_bash = BashOperator(
        task_id="echo_in_bash",
        bash_command="echo 'Hello from BashOperator'",
    )

    t_python = PythonOperator(
        task_id="print_in_python",
        python_callable=print_python,
    )

    t_bash >> t_python  # linear dependency
