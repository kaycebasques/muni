import os
import subprocess

PICOTOOL_EXECUTABLE = f'{os.getcwd()}/bin/picotool/picotool'

os.chdir('build')
subprocess.run([
    PICOTOOL_EXECUTABLE, 'load', '-x', 'picow_tls_client_poll.elf'
])
os.chdir('..')
