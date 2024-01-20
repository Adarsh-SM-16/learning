import subprocess

def run_git_command(command):
    try:
        result = subprocess.run(command, check=True, text=True, shell=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {e}")
        return None

# Example: Get the current branch
open("changes_path","w") 
run_git_command("git checkout asm1")
changes_path= run_git_command("git diff asm asm1 -- _sorces.yml > changes.path")
log=open("changes_path", "r")
content=log.read()
print(content)
