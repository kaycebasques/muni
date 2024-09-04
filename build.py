import json
import os
import subprocess
import sys

try:
    with open('.env', 'r') as f:
        env = json.load(f)
except FileNotFoundError as e:
    sys.exit('FileNotFoundError: .env')

PICO_SDK_PATH = f'{os.getcwd()}/pico-sdk'
WIFI_SSID = env['WIFI_SSID']
WIFI_PASSWORD = env['WIFI_PASSWORD']
PICOTOOL_DIR = f'{os.getcwd()}/bin/picotool'

os.chdir('build')
subprocess.run([
    'cmake', '..', f'-DPICO_SDK_PATH={PICO_SDK_PATH}',
    '-DPICO_PLATFORM=rp2040',
    '-DPICO_BOARD=pico_w', '-DPICO_COMPILER=pico_arm_cortex_m0plus_gcc',
    '-DPICO_GCC_TRIPLE=arm-none-eabi', f'-Dpicotool_DIR={PICOTOOL_DIR}',
    f'-DWIFI_SSID={WIFI_SSID}', f'-DWIFI_PASSWORD={WIFI_PASSWORD}'
])
subprocess.run(['make', '-j16'])
os.chdir('..')
