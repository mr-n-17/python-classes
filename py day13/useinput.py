import subprocess

process = subprocess.Popen(["pattern"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True,shell=True)
output, error = process.communicate(input="some input text")
print(output)