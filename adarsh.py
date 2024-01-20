import subprocess
import filecmp
output = subprocess.check_output(["git", "fetch", "origin"], stderr=subprocess.STDOUT, cwd='/workspaces/learning')
with open("/workspaces/learning/_sources.yml","ab") as f:  # append to file
    f.write(output)
