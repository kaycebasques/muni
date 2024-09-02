import os
import subprocess

if not os.path.isdir('pico-sdk'):
    subprocess.run([
        'git', 'clone', 'git@github.com:kaycebasques/pico-sdk.git'
    ])
    subprocess.run([
        'git', '-C', 'pico-sdk', 'remote', 'add', 'upstream',
        'git@github.com:raspberrypi/pico-sdk.git'
    ])

subprocess.run([
    'sudo', 'apt', 'install', 'cmake', 'gcc-arm-none-eabi',
    'libnewlib-arm-none-eabi', 'build-essential', 'g++',
    'libstdc++-arm-none-eabi-newlib'
])

if not os.path.isdir('build'):
    os.mkdir('build')
    os.chdir('build')
    subprocess.run(['cmake', '..'])
    os.chdir('..')
