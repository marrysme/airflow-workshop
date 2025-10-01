#!/usr/bin/env bash
set -euo pipefail

python -V
export AIRFLOW_HOME="$PWD/.airflow"
export AIRFLOW__CORE__LOAD_EXAMPLES=False
export AIRFLOW__WEBSERVER__EXPOSE_CONFIG=False

mkdir -p "$AIRFLOW_HOME"
ln -sfn "$PWD/dags" "$AIRFLOW_HOME/dags"

python -m pip install --upgrade pip wheel setuptools
PY=$(python -c "import sys; print(f'{sys.version_info[0]}.{sys.version_info[1]}')")
AF_VER=2.9.2
python -m pip install "apache-airflow==${AF_VER}"   --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-${AF_VER}/constraints-${PY}.txt"

airflow db init
airflow users create   --username admin --firstname Admin --lastname User   --role Admin --email admin@example.com --password admin

airflow webserver --hostname 0.0.0.0 --port 8080 -D
airflow scheduler -D

echo "Airflow is starting on port 8080. Login: admin / admin"
