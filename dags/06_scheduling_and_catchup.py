from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator

# NOTE:
# - schedule runs every 15 minutes
# - catchup=False means Airflow will NOT backfill old runs between start_date and now
with DAG(
    dag_id="06_scheduling_and_catchup",
    description="Show scheduling (cron) and discuss catchup behavior (no decorators)",
    start_date=datetime(2024, 1, 1),
    schedule="*/15 * * * *",
    catchup=False,
    tags=["schedule","catchup","basics"],
) as dag:
    stamp = BashOperator(
        task_id="stamp_run",
        bash_command="echo 'Run for {{ ds }} at {{ ts }}' >> $AIRFLOW_HOME/scheduled_runs.log",
    )
