import os
import time
import random
from datetime import datetime
from subprocess import run, CalledProcessError

# Configuration
file_path = "update_log.txt"  # Path to the file to be updated
repo_path = r"/repo/Auto_Commit"  # Path to your local GitHub repository
commit_message = "Updated log with current timestamp"

# New interval: 3 to 30 hours
time_interval_min = 3 * 60 * 60   # 3 hours in seconds
time_interval_max = 30 * 60 * 60  # 30 hours in seconds

def append_timestamp_to_file(file_path):
    """Append the current timestamp to the specified file."""
    with open(file_path, "a") as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{timestamp}\n")

def commit_and_push(repo_path, commit_message):
    """Commit and push changes to the GitHub repository."""
    try:
        run(["git", "add", file_path], cwd=repo_path, check=True)
        run(["git", "commit", "-m", commit_message], cwd=repo_path, check=True)
        run(["git", "push"], cwd=repo_path, check=True)
    except CalledProcessError as e:
        print(f"[ERROR] Git operation failed: {e}")

def main():
    while True:
        try:
            append_timestamp_to_file(os.path.join(repo_path, file_path))
            commit_and_push(repo_path, commit_message)
            time_to_wait = random.randint(time_interval_min, time_interval_max)
            print(f"Next update in {time_to_wait / 3600:.2f} hours.")
            time.sleep(time_to_wait)
        except Exception as e:
            print(f"[ERROR] Unexpected failure: {e}")
            time.sleep(60)  # wait a minute before retrying

if __name__ == "__main__":
    main()
