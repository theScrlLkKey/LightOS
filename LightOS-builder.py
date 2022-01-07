import shutil
import sys
import os


files_to_zip = ['LightOS.py', 'LightOS_main.py', 'griffin_quest.py', 'lightbreakout.py', 'lightbrowse.py', 'lightcalc.py', 'lightdocmsg.py', 'LightEncrypter.py', 'Lightirc.py', 'lightmail.py', 'LightMan.py', 'LightPIM.py', 'LightStonks.py', 'LightType.py', 'Lightvideo.py', 'maps.txt']
dirs_to_zip = ['apps', 'chatpy', 'plugins', 'startup']

f = 0
d = 0

sys.stdout.write('Copying dirs')
sys.stdout.flush()
while True:
    try:
        shutil.copytree(dirs_to_zip[d], f'tmp/{dirs_to_zip[d]}')
        d += 1
        sys.stdout.write('.')
        sys.stdout.flush()
    except IndexError:
        print(' Done!')
        break
    except Exception as err:
        print(' : ' + str(err))
        print('Continuing with packaging as error was non-fatal')
        break

sys.stdout.write('Copying files')
sys.stdout.flush()
while True:
    try:
        shutil.copy2(files_to_zip[f], 'tmp')
        f += 1
        sys.stdout.write('.')
        sys.stdout.flush()
    except IndexError:
        print(' Done!')
        break
    except Exception as err:
        print(' : ' + str(err))
        print('Continuing with packaging as error was non-fatal')
        break

input('Make any changes needed to tmp, and press enter to continue... ')
buildnum = input('Input version string: ')

sys.stdout.write('Compressing to LightOS_installFiles.tar...')
sys.stdout.flush()
shutil.make_archive(f'output/v{buildnum}/LightOS_installFiles', 'tar', 'tmp')
print(' Done!')

sys.stdout.write('Making Zip')
sys.stdout.flush()
shutil.copy2('LightOS_setup.py', f'output/v{buildnum}')
sys.stdout.write('.')
sys.stdout.flush()

shutil.make_archive(f'output/ztmp/LightOS-v{buildnum}', 'zip', f'output/v{buildnum}')
sys.stdout.write('.')
sys.stdout.flush()

shutil.move(f'output/ztmp/LightOS-v{buildnum}.zip', f'output/v{buildnum}')
sys.stdout.write('.')
sys.stdout.flush()
print(' Done!')

sys.stdout.write('Cleaning up')
sys.stdout.flush()
os.rmdir('output/ztmp')
sys.stdout.write('.')
sys.stdout.flush()

os.remove(f'output/v{buildnum}/LightOS_setup.py')
sys.stdout.write('.')
sys.stdout.flush()

shutil.copy2('LightOS_Online-installer.py', f'output/v{buildnum}')
sys.stdout.write('.')
sys.stdout.flush()

shutil.rmtree('tmp')
sys.stdout.write('.')
sys.stdout.flush()
print(' Done!')

print(f'Done packaging LightOS, check output/v{buildnum}/ for files.')


