import subprocess
import filecmp
output = subprocess.check_output(["git", "fetch", "origin"], stderr=subprocess.STDOUT, cwd='/workspaces/learning')
with open("/workspaces/learning/output.txt","/workspaces/learning/_sources.yml") as f:  # append to file
    f.write(output)
print(f)