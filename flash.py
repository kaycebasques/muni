import os
import subprocess

PICOTOOL_EXECUTABLE = f'{os.getcwd()}/bin/picotool/picotool'

os.chdir('build')
subprocess.run([
    PICOTOOL_EXECUTABLE, 'load', '-x', 'app.elf'
])
os.chdir('..')
