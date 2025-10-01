from __future__ import annotations
from datetime import datetime
from pathlib import Path
import csv, statistics as stats
from airflow.decorators import dag, task

DATA_DIR = Path(__file__).resolve().parents[1] / "data"
DATA_DIR.mkdir(parents=True, exist_ok=True)

@dag(
    dag_id="stats_to_csv",
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False,
    tags=["stats","csv"],
)
def stats_to_csv():
    @task
    def generate()->list[int]:
        return [4, 8, 15, 16, 23, 42]

    @task
    def compute(values:list[int])->dict:
        return {
            "count": len(values),
            "min": min(values),
            "max": max(values),
            "mean": round(stats.fmean(values), 3),
            "median": stats.median(values),
        }

    @task
    def write_csv(summary:dict)->str:
        out = DATA_DIR / "stats_summary.csv"
        with open(out, "w", newline="") as f:
            w = csv.DictWriter(f, fieldnames=list(summary.keys()))
            w.writeheader(); w.writerow(summary)
        print(f"Wrote CSV to: {out}")
        return str(out)

    write_csv(compute(generate()))

stats_to_csv()
