import os
import subprocess

os.environ['PICO_SDK_PATH'] = f'{os.getcwd()}/pico-sdk'

# result = subprocess.run(['nproc'], stdout=subprocess.PIPE)
# nproc = result.stdout.decode('utf-8')
# print(nproc)

os.chdir('build')
subprocess.run(['make', '-j16'])  # TODO: Don't hardcode
os.chdir('..')
