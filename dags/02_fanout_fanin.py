from datetime import datetime
from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.bash import BashOperator

with DAG(
    dag_id="02_fanout_fanin",
    description="Fan-out to run tasks in parallel, then fan-in to a join",
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False,
    tags=["dependencies","parallelism"],
) as dag:
    start = EmptyOperator(task_id="start")

    # Fan-out: three parallel tasks
    a = BashOperator(task_id="task_a", bash_command="echo A && sleep 2")
    b = BashOperator(task_id="task_b", bash_command="echo B && sleep 2")
    c = BashOperator(task_id="task_c", bash_command="echo C && sleep 2")

    # Fan-in: join after all succeed
    join = EmptyOperator(task_id="join")

    start >> [a, b, c] >> join
