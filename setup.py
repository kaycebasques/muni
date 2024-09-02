import os
import subprocess

pico_sdk_path = f'{os.getcwd()}/pico-sdk'
picotool_dir = f'{os.getcwd()}/bin/picotool'

subprocess.run([
    'sudo', 'apt', 'install', 'cmake', 'gcc-arm-none-eabi',
    'libnewlib-arm-none-eabi', 'build-essential', 'g++',
    'libstdc++-arm-none-eabi-newlib', 'pkg-config',
    'libusb-1.0-0-dev'
])

if not os.path.isdir('pico-sdk'):
    print('pico-sdk')
    subprocess.run([
        'git', 'clone', 'git@github.com:kaycebasques/pico-sdk.git'
    ])
    subprocess.run([
        'git', '-C', 'pico-sdk', 'remote', 'add', 'upstream',
        'git@github.com:raspberrypi/pico-sdk.git'
    ])

if not os.path.isdir('picotool'):
    print('picotool')
    # Don't use --recursive because we don't need mbedtls
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
        'cmake', '..', f'-DPICO_SDK_PATH={pico_sdk_path}',
        '-DCMAKE_INSTALL_PREFIX=../../bin', '-DPICOTOOL_FLAT_INSTALL=1'
    ])
    subprocess.run(['make', '-j16'])
    subprocess.run(['make', 'install'])
    os.chdir('../..')

if not os.path.isdir('build'):
    print('build')
    os.mkdir('build')
    os.chdir('build')
    subprocess.run([
        'cmake', '..', f'-DPICO_SDK_PATH={pico_sdk_path}',
        '-DPICO_PLATFORM=rp2040',
        '-DPICO_BOARD=pico', '-DPICO_COMPILER=pico_arm_cortex_m0plus_gcc',
        '-DPICO_GCC_TRIPLE=arm-none-eabi', f'-Dpicotool_DIR={picotool_dir}'
    ])
    os.chdir('..')
