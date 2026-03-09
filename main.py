import subprocess
import os

DEVNULL = {"stdout": subprocess.DEVNULL, "stderr": subprocess.DEVNULL}

while True:
    TOTAL_COMMITS = 1000

    for i in range(TOTAL_COMMITS):
        with open("data.txt", "a") as f:
            f.write("Jai Mahakal\n")

        # single call instead of separate add + commit
        subprocess.run(["git", "commit", "-am", f"auto commit {i}"], **DEVNULL)

        # if i % 100 == 0:
        print(f"{i} commits done")

    subprocess.run(["git", "push", "-u", "origin", "main"], **DEVNULL)
    print()
    print()
    print()
