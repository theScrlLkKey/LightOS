import os
import sys
import time
import shutil
import importlib
import subprocess


packages_to_install = ['requests', 'os', 'colorama', 'threading', 'random', 'shutil', 'pythonping', 'zipfile','yfinance', 'msvcrt', 'cryptography', 'socket', 'select', 'errno', 'urllib', 'pynput', 'sympy']



def install_and_check(package):
    try:
        importlib.import_module(package)
    except:
        subprocess.call([sys.executable, "-m", "pip", "install", package],  stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
        sys.stdout.write('.')
        sys.stdout.flush()


sys.stdout.write('Checking requirements...')
sys.stdout.flush()
while packages_to_install:
    sys.stdout.write('.')
    sys.stdout.flush()
    install_and_check(packages_to_install[0])
    packages_to_install.pop(0)
print(' Done!')
time.sleep(0.5)
sys.stdout.write('Unzipping...')
sys.stdout.flush()

shutil.unpack_archive('LightOS_installFiles.tar', 'LightOS-Files')
os.remove('LightOS_installFiles.tar')

print(' Done!')
time.sleep(0.5)
sys.stdout.write('Making files executable...')
sys.stdout.flush()

shutil.move('LightOS-Files/LightOS.py', os.getcwd())
print(' Done!')
print('This program can now be deleted.')
time.sleep(1)
exit()
