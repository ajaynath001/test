import subprocess
from datetime import datetime

REPO_PATH = r"C:\Users\write\Desktop\delte"

def run_git(command):
    result = subprocess.run(
        command,
        cwd=REPO_PATH,
        shell=True,
        capture_output=True,
        text=True
    )
    print(result.stdout)
    print(result.stderr)

def auto_commit_push():

    run_git("git pull origin main")

    run_git("git add .")

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    run_git(f'git commit -m "Auto commit {timestamp}"')

    run_git("git push origin main")

auto_commit_push()