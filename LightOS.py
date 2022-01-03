import subprocess
import time
import os

release = False
logging = False


try:
    os.chdir('LightOS-Files')
except:
    print('The LightOS-Files folder needs to be in the same directory as LightOS.py. If LightOS was installed correctly, contact the developer.')
    if not release:
        ch = input('Press enter to exit, or C to try to continue: ')
        if ch not in ('c','C'):
            exit()
    else:
        time.sleep(2)
        exit()

if not release:
    print('LightOS ~dev console~')
    print('console will be removed in final release')
    print("Press ctrl + c within three seconds to specify a init string (default: py -3 LightOS_main.py)")
    try:
        time.sleep(3)
    except KeyboardInterrupt:
        custinit = input('Custom init string: ')
        print('Starting LightOS...')
        subprocess.call(custinit, creationflags=subprocess.CREATE_NEW_CONSOLE)
        exit()


print('Starting LightOS...')
if not release:
    try:
        with open('log/ll.bat', 'r') as data:
            data.read()
    except:
        os.mkdir('log')
        with open('log/ll.bat', 'w+') as data:
            data.write('echo off\npowershell -nologo "& "get-content log\log.txt -wait -tail 1"\npause')

        os.chdir('plugins')
        os.mkdir('log')
        os.chdir('..')
        with open('plugins/log/ll.bat', 'w+') as data:
            data.write('echo off\npowershell -nologo "& "get-content plugins\log\log.txt -wait -tail 1"\npause')

        with open('plugins/log/log.txt', 'w+') as log:
            log.write('')


    # with open('log.txt', 'w+') as log:
    #     log.write('')

    if logging:
        os.startfile('log\ll.bat')
        os.startfile('plugins\log\ll.bat')


try:
    if logging and not release:
        subprocess.call(['py', '-3', 'LightOS_main.py', 'enableconsolelog'], creationflags=subprocess.CREATE_NEW_CONSOLE)
    else:
        subprocess.call(['py', '-3', 'LightOS_main.py'], creationflags=subprocess.CREATE_NEW_CONSOLE)


except AttributeError:
    print('This version of LightOS is incompatible with your operating system. '
          'Please ask for a supported version if a version for your OS does not exist.')
    input('Press enter...')
    exit()

except KeyboardInterrupt:
    print('~devConsole~ test log')

except Exception as err:
    if release:
        print('A error occurred. Please contact the developer and include this error code: ')
        print(str(err))
        input('Press enter...')
        exit()
    else:
        print('AAAAAAAAAA something happened please tell the person who gave you this')
        print('and please tell them this: ' + str(err))
        input('Press enter...')
        exit()
