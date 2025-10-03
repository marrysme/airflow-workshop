# Airflow Workshop in Github Codespaces

A tiny Airflow project for a browser-only workshop containing starter DAGs demonstrating
basic airflow concepts.

No installations required. Works in GitHub Codespaces using a devcontainer that auto-installs Airflow and starts the webserver + scheduler.

# What you’ll learn

- What an Operator is (Python, Bash, etc.) vs a Task (operator instance)
- How to set dependencies (>>, fan-out/fan-in, branching)
- Basic retries, scheduling, catchup, and XCom (passing small values)

# Quick start (if you are starting from the owner's repo)
- Open the repo in GitHub → Code → Codespaces → Create codespace on main
- Wait for Port 8080 → Open in Browser
- Login to Airflow: admin / admin
- In the UI, unpause DAGs and run them in this order:


## Troubleshooting
- If the Airflow UI doesn’t auto-open, run:
  ```
  export AIRFLOW_HOME=$PWD/.airflow
  airflow standalone
  ```
- Port 8080 → 502 (Bad Gateway). Webserver may not be up yet. In a terminal:
  ```
  export AIRFLOW_HOME=$PWD/.airflow
  pkill -f "airflow|gunicorn" || true
  airflow webserver --hostname 0.0.0.0 --port 8080 -l info
  # start scheduler in a second terminal
  airflow scheduler -l info
  ```
- “Bad Request: referrer does not match host”
   The devcontainer exports proxy/cookie settings to fix this. If you still see it, rebuild:
   F1 → Codespaces: Rebuild Container.
  
- No DAGs visible
  Files must be in the repo’s dags/ folder at the repo root. Refresh the UI after saving.
  
- Tasks stuck in “queued”
  Give it 5–10 seconds after startup; ensure the scheduler is running (see command above).

  ## Cleanup
   - Stop your Codespace from the Codespaces menu; delete it later via Your profile → Codespaces.
   - No local dependencies to uninstall.
