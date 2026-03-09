import subprocess
import os

DEVNULL = {"stdout": subprocess.DEVNULL, "stderr": subprocess.DEVNULL}
PIPE = {"stdout": subprocess.PIPE, "stderr": subprocess.DEVNULL}


def git_out(cmd):
    """Run a git command and return stripped stdout."""
    r = subprocess.run(cmd, **PIPE)
    return r.stdout.strip()


def fast_commit(message):
    """Create a commit using git plumbing (much faster than 'git commit')."""
    # 1. Write the working-tree state into a tree object
    subprocess.run(["git", "add", "data.txt"], **DEVNULL)
    tree_hash = git_out(["git", "write-tree"])

    # 2. Get current HEAD
    head = git_out(["git", "rev-parse", "HEAD"])

    # 3. Create commit object directly (skips hooks, index refresh, etc.)
    commit_hash = git_out(
        ["git", "commit-tree", tree_hash, "-p", head, "-m", message]
    )

    # 4. Point HEAD / branch ref to the new commit
    subprocess.run(["git", "update-ref", "HEAD", commit_hash], **DEVNULL)


while True:
    TOTAL_COMMITS = 1000

    for i in range(TOTAL_COMMITS):
        with open("data.txt", "a") as f:
            f.write("Jai Mahakal\n")

        fast_commit(f"auto commit {i}")

        if i % 100 == 0:
            print(f"{i} commits done")

    subprocess.run(["git", "push", "-u", "origin", "main"], **DEVNULL)
    print(f"Pushed batch of {TOTAL_COMMITS}")
    print()

