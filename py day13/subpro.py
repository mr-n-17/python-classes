import subprocess 

# p=subprocess.Popen('python testit.py',
#                    stdin=subprocess.PIPE,
#                    stdout=subprocess.PIPE,
#                    stderr=subprocess.PIPE,
#                    shell=True)

# o,e=p.communicate(input='sultan\n'.encode())
# if p.returncode !=0:
#     print(o)
#     print(e)


p=subprocess.run(['python','testit.py'],  #faster than Popen
                 capture_output=True,
                 shell=True,
                 text=True,
                 input='gpay',check=True)

if p.returncode!=0:
    print(p.stdout)
    print(p.stderr)