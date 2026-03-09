import subprocess
import os

DEVNULL = {"stdout": subprocess.DEVNULL, "stderr": subprocess.DEVNULL}

while True:
    TOTAL_COMMITS = 100

    for i in range(TOTAL_COMMITS):
        with open("data.txt", "a") as f:
            f.write("Jai Mahakal\n")

        # single call instead of separate add + commit
        subprocess.run(["git", "commit", "-am", f"auto commit {i}"], **DEVNULL)

        # if i % 100 == 0:
        print(f"{i} commits done")
        print()
        print()

    subprocess.run(["git", "push", "-u", "origin", "main"], **DEVNULL)
    print("Pushed batch")


# import subprocess
# import os
# import time

# REPO_PATH = r"C:\Users\write\Desktop\delte"
# FILE_NAME = "hello.txt"

# TOTAL_PUSHES = 1000000   # change this to control pushes


# def run(cmd):
#     subprocess.run(cmd, cwd=REPO_PATH, shell=True)


# file_path = os.path.join(REPO_PATH, FILE_NAME)

# for i in range(1, TOTAL_PUSHES + 1):

#     # append text
#     with open(file_path, "a") as f:
#         f.write("Hello World\n")

#     # git commands
#     run("git add hello.txt")
#     run(f'git commit -m "commit {i}"')
#     run("git push origin main")

#     print(f"Push {i} completed")
#     print(i)
#     print()
#     print()
#     print()
#     print()

#     # time.sleep(2)  # optional delay