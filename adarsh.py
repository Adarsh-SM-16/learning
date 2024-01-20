import subprocess
import filecmp
output = subprocess.check_output(["git", "fetch", "origin"], stderr=subprocess.STDOUT, cwd='/workspaces/learning/_sources.yml')
with open("/workspaces/learning","ab") as f:  # append to file
    f.write(output)
