# Run an oracle cli Command
import subprocess
def runCLI(pCommand):
    command=pCommand
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = process.communicate()
    return out.decode('utf-8'),  err.decode('utf-8')
