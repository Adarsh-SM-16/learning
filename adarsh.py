import subprocess

def run_git_command(command):
    try:
        result = subprocess.run(command, check=True, text=True, shell=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {e}")
        return None

# Example: Get the current branch
current_branch = run_git_command("git rev-parse --abbrev-ref HEAD")
print(f"Current branch: {current_branch}")