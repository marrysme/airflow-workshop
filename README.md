# Airflow Hello + Stats (Codespaces)

A tiny Airflow project for a browser-only workshop: one `hello` DAG and one `stats_to_csv` DAG.

## How to use (Codespaces)
1. Create a new empty GitHub repo.
2. Upload the **contents** of this folder (not the zip) to the repo.
3. Click **Code ▸ Codespaces ▸ Create codespace on main**.
4. Wait ~1–3 minutes for setup.
5. When port **8080** appears, click **Open in Browser**.
6. Login with **admin / admin**.
7. In the UI, unpause and trigger **`hello`** and **`stats_to_csv`**.

### Download the CSV
- After running `stats_to_csv`, open `data/stats_summary.csv` in the Codespaces file explorer.
- Right-click → **Download**.

## Troubleshooting
- If the Airflow UI doesn’t auto-open, run:
  ```bash
  export AIRFLOW_HOME=$PWD/.airflow
  airflow standalone
  ```
