# Plugin code
import colorama
import sys
colorama.init()
sys.stdout.write('\033[2J')
sys.stdout.flush()
# End of plugin code, your code goes below
import os
import requests
import time
import shutil
import importlib
import subprocess


def download(url: str, dest_folder: str):
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)  # create folder if it does not exist

    filename = url.split('/')[-1].replace(" ", "_")  # be careful with file names
    file_path = os.path.join(dest_folder, filename)

    r = requests.get(url, stream=True)
    if r.ok:
        print("Saving to temp directory", os.path.abspath(file_path))
        with open(file_path, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024 * 8):
                if chunk:
                    f.write(chunk)
                    f.flush()
                    os.fsync(f.fileno())
    else:  # HTTP status code 4XX/5XX
        print("Download failed: status code {}\n{}".format(r.status_code, r.text))


os.chdir('..')
os.chdir('..')
cwd = os.getcwd()

print('LightOS updater')
print('Note: if you installed the stable version, updating to a beta might break things.')
chan = input('Stable or beta (s/b, enter to cancel)? ')

if chan.lower() == 's':
    print('Downloading latest stable release of LightOS...')
    download("https://github.com/theScrlLkKey/LightOS-stable/releases/latest/download/LightOS_installFiles.tar", dest_folder=cwd)
elif chan.lower() == 'b':
    print('Downloading latest beta release of LightOS...')
    download("https://github.com/theScrlLkKey/LightOS-beta/releases/latest/download/LightOS_installFiles.tar", dest_folder=cwd)
else:
    exit()


packages_to_install = ['requests', 'os', 'colorama', 'threading', 'random', 'shutil', 'pythonping', 'zipfile','yfinance', 'msvcrt', 'cryptography', 'socket', 'select', 'errno', 'urllib', 'pynput', 'sympy']



def install_and_check(package):
    try:
        importlib.import_module(package)
    except:
        subprocess.call([sys.executable, "-m", "pip", "install", package, "-U"],  stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
        sys.stdout.write('.')
        sys.stdout.flush()


sys.stdout.write('Updating packages...')
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

os.remove('LightOS.py')
shutil.move('LightOS-Files/LightOS.py', os.getcwd())
print(' Done!')

print('Close this window and re-launch LightOS to finish updating.')
while True:
    pass
