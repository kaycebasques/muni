import os
import subprocess

# result = subprocess.run(['nproc'], stdout=subprocess.PIPE)
# nproc = result.stdout.decode('utf-8')
# print(nproc)

os.chdir('build')
subprocess.run(['make', '-j16'])
os.chdir('..')
