import time
import csv
import uuid

from pathlib import Path


def action_time_spent(action):
    start_time = time.perf_counter()
    action()
    end_time = time.perf_counter()
    return round((end_time - start_time) * 1000 , 2)

def append_performance_results_to_report(testname : str, iteration : int, step : str, duration_ms : float, execution_time: str):
    output_path = Path("reports/ui_performance_happy_path_results.csv")
    output_path.parent.mkdir(parents = True, exist_ok = True)

    file_exists = output_path.exists()

    with output_path.open("a", newline = "", encoding = "utf-8") as file:
        writer = csv.DictWriter(
            file,
            fieldnames = ["id","test_name", "iteration", "step", "duration_ms", "execution_time"]
        )
        if not file_exists:
            writer.writeheader()

        writer.writerow({
            "id" : str(uuid.uuid4()),
            "test_name": testname,
            "iteration": iteration,
            "step": step,
            "duration_ms": duration_ms,
            "execution_time": execution_time
        })
