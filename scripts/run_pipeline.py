import subprocess
import sys
import schedule
import time 
from pathlib import Path



BASE_DIR = Path(__file__).resolve().parent.parent

scripts = [
    "ingest.py",
    "transform.py",
    "monitor.py"
]

def run_pipeline():
    print("\nStarting pipeline...")
    for script in scripts:
        script_path = BASE_DIR / "scripts" / script
    
        print(f"\nRunning {script}...")
        
        result = subprocess.run(
            [sys.executable, str(script_path)],
            capture_output=True,
            text=True
        )
        
        print(result.stdout)
        
        if result.stderr:
            print("ERROR:")
            print(result.stderr)

        if result.returncode != 0:
            print(f"Script {script} failed with exit code {result.returncode}. Stopping pipeline.")
            break
    else:
        print("Pipeline completed successfully")
    
schedule.every(10).seconds.do(run_pipeline)

while True:
    schedule.run_pending()
    time.sleep(1)