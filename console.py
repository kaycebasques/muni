import subprocess

subprocess.run([
    'minicom', '-D', '/dev/ttyACM0', '-b', '115200'
])
