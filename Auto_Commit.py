import os
import time
import random
from datetime import datetime
from subprocess import run

# Configuration
file_path = "update_log.txt"  # Path to the file to be updated
repo_path = r"C:\Users\iante\Documents\Repos\Auto_Commit"  # Path to your local GitHub repository
commit_message = "Updated log with current timestamp"
#time_interval_min = 20 * 60 * 60  # 20 hours in seconds
time_interval_min = 5 * 60  # 5 minutes in seconds
#time_interval_max = 40 * 60 * 60  # 40 hours in seconds
time_interval_max = 20 * 60  # 20 minutes in seconds

def append_timestamp_to_file(file_path):
    """Append the current timestamp to the specified file."""
    with open(file_path, "a") as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{timestamp}\n")

def commit_and_push(repo_path, commit_message):
    """Commit and push changes to the GitHub repository."""
    run(["git", "add", file_path], cwd=repo_path)
    run(["git", "commit", "-m", commit_message], cwd=repo_path)
    run(["git", "push"], cwd=repo_path)

def main():
    while True:
        # Append the timestamp to the file
        append_timestamp_to_file(os.path.join(repo_path, file_path))

        # Commit and push changes to GitHub
        commit_and_push(repo_path, commit_message)

        # Wait for a random time interval
        time_to_wait = random.randint(time_interval_min, time_interval_max)
        print(f"Next update in {time_to_wait / 3600:.2f} hours.")
        time.sleep(time_to_wait)

if __name__ == "__main__":
    main()

