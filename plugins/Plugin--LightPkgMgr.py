# Plugin code
import colorama
import sys
colorama.init()
sys.stdout.write('\033[2J')
sys.stdout.flush()
# End of plugin code, your code goes below
import os
from os import walk
import subprocess
import shutil


def inputchar(key):
    sys.stdout.write(key)
    sys.stdout.flush()


def installpkg():
    os.chdir('..')
    os.chdir('..')
    pkgs = []
    cwd = os.getcwd()
    for (dirpath, dirnames, filenames) in walk(cwd):
        pkgs.extend(filenames)
        break
    pkgnumls = {}
    j = 1
    for pkg in pkgs:
        if '.tar' in pkg:
            pkgnumls[str(j)] = pkg
            j += 1
        else:
            continue
    j = 3
    i = 1
    for pkg in pkgs:
        try:
            plugn = pkgnumls[str(i)]
            plugntr = plugn.replace(".tar", "")
            print(f'{j - 2}. {plugntr}')
            j += 1
            i += 1
        except:
            i += 1

    ussl = input('Enter selection (nothing to cancel): ')
    if ussl == '':
        pass
    elif ussl in pkgnumls:
        print(f'Installing {pkgnumls[ussl]}...')
        try:
            shutil.unpack_archive(pkgnumls[ussl], 'LightOS-Files/apps', 'tar')
            try:
                os.remove(f'{pkgnumls[ussl]}')
            except Exception as err:
                print('Could not remove installed package. Here is why, press enter to dismiss.')
                input(err)

        except Exception as err:
            print('Package could not be installed. Here is why, press enter to dismiss.')
            input(err)

    else:
        pass



def delpkg():
    dirs = []
    cwd = os.getcwd()
    for (dirpath, dirnames, filenames) in walk(cwd):
        dirs.extend(dirnames)
        break
    dirnumls = {}
    j = 1
    for dir in dirs:
        dirnumls[str(j)] = dir
        j += 1
    j = 3
    i = 1
    for dir in dirs:
        try:
            plugn = dirnumls[str(i)]
            print(f'{j - 2}. {plugn}') # tr
            j += 1
            i += 1
        except:
            i += 1

    ussl = input('Enter selection (nothing to cancel): ')
    if ussl == '':
        pass
    elif ussl in dirnumls:
        print(f'Deleting {dirnumls[ussl]}...')
        try:
            shutil.rmtree(dirnumls[ussl])
        except:
            pass
        try:
            os.remove(f'App--{dirnumls[ussl]}.py')
        except:
            print('Could not be deleted.')

    else:
        pass




os.chdir('..')
os.chdir('apps')
cwd = os.getcwd()
files = []

while True:
    sys.stdout.write('\033[2J')
    files = []
    print('1. Install package')
    print('2. Delete package')
    for (dirpath, dirnames, filenames) in walk(cwd):
        files.extend(filenames)
        break
    filenumls = {}
    j = 3
    for file in files:
        filenumls[str(j)] = file
        j += 1
    j = 6
    i = 3
    for file in files:
        try:
            dummy, plugn = filenumls[str(i)].split('--')
            plugntr = plugn.replace(".py", "")
            print(f'{j - 3}. {plugntr}')
            j += 1
            i += 1
        except:
            i += 1
    print('Exit to quit')


    ussl = input('Enter selection: ')
    if ussl == '1':
        installpkg()
        os.chdir('LightOS-Files/apps')
        input('Done! Press enter...')
    elif ussl == '2':
        delpkg()
        input('Done! Press enter...')
    elif ussl.upper() == 'EXIT':
        exit()
    elif ussl in filenumls:
        inputchar('\033[2J')
        try:
            subprocess.call(['python', filenumls[ussl]])
        except:
            continue
    else:
        continue