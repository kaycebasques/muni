import os
import subprocess

PICO_SDK_PATH = f'{os.getcwd()}/pico-sdk'

subprocess.run([
    'sudo', 'apt', 'install', 'cmake', 'gcc-arm-none-eabi',
    'libnewlib-arm-none-eabi', 'build-essential', 'g++',
    'libstdc++-arm-none-eabi-newlib', 'pkg-config',
    'libusb-1.0-0-dev'
])

if not os.path.isdir('pico-sdk'):
    subprocess.run([
        'git', 'clone', '--recursive', 'git@github.com:kaycebasques/pico-sdk.git'
    ])
    subprocess.run([
        'git', '-C', 'pico-sdk', 'remote', 'add', 'upstream',
        'git@github.com:raspberrypi/pico-sdk.git'
    ])

if not os.path.isdir('picotool'):
    # Don't use --recursive because we don't need mbedtls (...?)
    subprocess.run([
        'git', 'clone', 'git@github.com:kaycebasques/picotool.git'
    ])
    subprocess.run([
        'git', '-C', 'picotool', 'remote', 'add', 'upstream',
        'git@github.com:raspberrypi/picotool.git'
    ])
    os.chdir('picotool')
    os.mkdir('build')
    os.chdir('build')
    subprocess.run([
        'cmake', '..', f'-DPICO_SDK_PATH={PICO_SDK_PATH}',
        '-DCMAKE_INSTALL_PREFIX=../../bin', '-DPICOTOOL_FLAT_INSTALL=1'
    ])
    subprocess.run(['make', '-j16'])
    subprocess.run(['make', 'install'])
    os.chdir('../..')

if not os.path.isdir('build'):
    os.mkdir('build')
