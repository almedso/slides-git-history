import argparse
import subprocess

parser = argparse.ArgumentParser()
parser.add_argument("--b", type=int, default=-1, help="Value for B")
parser.add_argument("--max-commits", default=1000, type=int, help="maximum number of commits to generate")
args = parser.parse_args()

def generate_commit(commit_no, a, b):
    file_name = f"modules/p{commit_no}.py"

    # write the file
    with open(file_name, "w") as f:
        f.write(f"A = {a}\n")
        f.write(f"B = {b}\n\n")
        f.write("def add():\n")
        f.write(f"    return A + B\n\n")
        f.write("def subtract():\n")
        f.write(f"    return A - B\n")

    # commit the file

    subprocess.run(["git", "add", file_name], check=True)
    subprocess.run(["git", "commit", "-m", f"Add module p{commit_no}.py"], check=True)


def generate_commits(b, max_commits):
    a = 1 - b * 3
    commit_no = a + 3 * b
    while commit_no < max_commits:
        print (f'Generating commit {commit_no} with A={a} and B={b}')
        generate_commit(commit_no, a, b)

        # increment stuff
        a += 1
        if a % 3 == 0:
            a -= 3
            b += 1
        commit_no = a + 3 * b


if __name__ == "__main__":
    generate_commits(args.b, args.max_commits)