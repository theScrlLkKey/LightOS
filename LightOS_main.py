import time
import random
from os import walk
import os
import zlib
import shutil
import subprocess
import sys
from pynput.keyboard import Listener, Key
import colorama
import threading
from cryptography.fernet import Fernet


#menus

main_menu = '''███████████████████████████████████████████████████████████████████
█00:00 AM       WELCOME,                        LIGHT OS MAIN MENU█  
███████████████████████████████████████████████████████████████████
█MENUS:                                                           █
█1. MAIN MENU                                                     █
█2. PROGRAMS                                           7. DEBUG   █
█3. GAMES                                              6. PLUGINS █
█4. DOCUMENTS                                          5. SETTINGS█
███████████████████████████████████████████████████████████████████
█                                                                 █
███████████████████████████████████████████████████████████████████ 
'''
usenmpw_menu = '''███████████████████████████████████████████████████████████████████
█                       ENTER LOGIN DETAILS                       █  
███████████████████████████████████████████████████████████████████
█                                                                 █
█                                                                 █
█                                                                 █
█                                                                 █
█                                                                 █
█                                                                 █ 
█                                                                 █
███████████████████████████████████████████████████████████████████ 
'''
prog_menu = '''███████████████████████████████████████████████████████████████████
█00:00 AM                                                 LIGHT OS█  
███████████████████████████████████████████████████████████████████
█PROGRAMS:                                                        █
█1. MAIN MENU           5. LIGHTTYPE                              █
█2. CHATPY              6. LIGHTCALC                              █
█3. LIGHTMAN            7. LIGHTSTOCKS                            █
█4. LIGHTCRYPTER                                                  █
███████████████████████████████████████████████████████████████████
█                                                                 █
███████████████████████████████████████████████████████████████████ 
'''
games_menu = '''███████████████████████████████████████████████████████████████████
█00:00 AM                                                 LIGHT OS█  
███████████████████████████████████████████████████████████████████
█GAMES:                                                           █
█1. MAIN MENU                                                     █
█2. LIGHTDRAW                                                     █
█                                                                 █
█                                                                 █
███████████████████████████████████████████████████████████████████ 
█                                                                 █
███████████████████████████████████████████████████████████████████
'''
settings_menu = '''███████████████████████████████████████████████████████████████████
█00:00 AM                                                 LIGHT OS█  
███████████████████████████████████████████████████████████████████
█SETTINGS:                                                        █
█1. RETURN TO MAIN MENU                                           █
█2. ON/OFF TOGGLE               CURRENT VALUE:                    █
█3. FOUR LEVEL SLIDER           CURRENT VALUE:                    █
█4. CUSTOM MESSAGE              CURRENT VALUE:                    █
███████████████████████████████████████████████████████████████████ 
█                                                                 █
███████████████████████████████████████████████████████████████████
'''
setting_submenu = '''███████████████████████████████████████████████████████████████████
█00:00 AM                                                 LIGHT OS█  
███████████████████████████████████████████████████████████████████
█                                                                 █
█                                                                 █
█                                                                 █
█                                                                 █
█                                                                 █
███████████████████████████████████████████████████████████████████ 
█                                                                 █
███████████████████████████████████████████████████████████████████
'''
loadingscr = '''███████████████████████████████████████████████████████████████████
█                            LIGHT OS                             █  
███████████████████████████████████████████████████████████████████
█                                                                 █
█                                                                 █
█        LIGHT OS HAS NOT CRASHED, DO NOT CLOSE THIS WINDOW       █
█                                                                 █
█                                                                 █
███████████████████████████████████████████████████████████████████ 
█                           LOADING...                            █
███████████████████████████████████████████████████████████████████
'''

doc_menu = '''███████████████████████████████████████████████████████████████████
█00:00 AM                                                 LIGHT OS█  
███████████████████████████████████████████████████████████████████
█OPTIONS:                                                         █
█1. RETURN TO MAIN MENU                                           █
█2. NEW                                                           █
█3. EDIT                                                          █
█4. DELETE                                                        █
███████████████████████████████████████████████████████████████████
█                                                                 █
███████████████████████████████████████████████████████████████████ 
'''

plugin_menu = '''███████████████████████████████████████████████████████████████████
█00:00 AM                                                 LIGHT OS█  
███████████████████████████████████████████████████████████████████
█PLUGINS:                                                         █
█                                                                 █
█                                                                 █
█                                                                 █
█                                           1. RETURN TO MAIN MENU█
███████████████████████████████████████████████████████████████████ 
█                                                                 █
███████████████████████████████████████████████████████████████████
'''

external_prog = '''███████████████████████████████████████████████████████████████████
█00:00 AM                                                 LIGHT OS█  
███████████████████████████████████████████████████████████████████
'''
#defs
name = 'USER'
colorama.init()
def write_key():
    """
    Generates a key and save it into a file
    """
    k = Fernet.generate_key()
    nbkey = k.decode("utf-8")
    return k
enckey = write_key()


def console_log(log_text):
    try:
        with open('log.txt', 'a+') as data:
            data.write(log_text + '\n')
    except:
        pass


def on_press(key):
    global key_jp
    if hasattr(key, 'char'):  # Write the character pressed if available
         key_jp = str(key.char)
    # elif key == Key.space:  # If space was pressed, write a space
    #     inputchar(' ')
    # elif key == Key.enter:  # If enter was pressed, write a new line
    #     key_jp = 'select'
    # elif key == Key.tab:  # If tab was pressed, write a tab
    #     inputchar('\t')
    # elif key == Key.left:
    #     inputchar('\033[1D')
    # elif key == Key.right:
    #     inputchar('\033[1C')
    # elif key == Key.up:
    #     inputchar('\033[1A')
    # elif key == Key.down:
    #     inputchar('\033[1B')
    elif key == Key.menu:
        switchscr('1')
    # elif key == Key.backspace:
    #     inputchar('\033[1D \033[1D')
    # elif key == Key.delete:
    #     inputchar('\b\27[127\b')
    # else:  # If anything else was pressed, write [<key_name>]
    #     pass

def getact(snm):
    rtrn = input(snm)
    return rtrn

def switchscr(scrnum):
    global curmen
    global tuploc
    global prognm
    global mes_setting
    global onoff_setting
    global fo_setting
    if scrnum == '1':
        inputchar('\033[2J')
        type(main_menu)
        inputchar('\033[11A')
        inputchar('\033[3C')
        inputchar('\033[2B')
        inputchar('\033[2;26H')
        type(name)
        tuploc = '10;19H'
        tmup(tuploc)
        curmen = 'main'
    if scrnum.lower() == 'exit':
        os._exit(0)
    elif scrnum == '2' and curmen == 'main':
        inputchar('\033[2J')
        type(prog_menu)
        inputchar('\033[11A')
        inputchar('\033[3C')
        inputchar('\033[2B')
        inputchar('\033[2;26H')
        type('PROGRAM LAUNCHER')
        tuploc = '10;19H'
        tmup(tuploc)
        curmen = 'prog'
    elif scrnum == '2' and curmen == 'prog':
        inputchar('\033[2J')
        type(external_prog)
        inputchar('\033[11A')
        inputchar('\033[3C')
        inputchar('\033[2B')
        inputchar('\033[2;26H')
        type('CHATPY')
        tuploc = '*'
        inputchar('\033[4;2H')
        curmen = 'ex_prog'
        inputchar('\033[4;2H')
        prognm = 'CHATPY  '
        # progtmu = threading.Thread(target=progtimup, args=())
        # progtmu.start()
        tmup('10;19H')
        inputchar('\033[4;1H')
        stprog("chatpy/chatpy2.py")
        time.sleep(0.5)
    elif scrnum == '3' and curmen == 'prog':
        inputchar('\033[1;1H')
        inputchar('\033[2J')
        type(external_prog)
        inputchar('\033[11A')
        inputchar('\033[3C')
        inputchar('\033[2B')
        inputchar('\033[2;26H')
        type('LIGHTMAN')
        tuploc = '*'
        inputchar('\033[4;2H')
        curmen = 'ex_prog'
        inputchar('\033[4;2H')
        prognm = 'CHATPY  '
        # progtmu = threading.Thread(target=progtimup, args=())
        # progtmu.start()
        tmup('10;19H')
        inputchar('\033[4;1H')
        stprog("LightMan.py")
        time.sleep(0.5)
    elif scrnum == '4' and curmen == 'prog':
        inputchar('\033[2J')
        type(external_prog)
        inputchar('\033[11A')
        inputchar('\033[3C')
        inputchar('\033[2B')
        inputchar('\033[2;26H')
        type('LIGHTCRYPTER')
        tuploc = '*'
        inputchar('\033[4;2H')
        curmen = 'ex_prog'
        inputchar('\033[4;2H')
        prognm = 'CHATPY  '
        # progtmu = threading.Thread(target=progtimup, args=())
        # progtmu.start()
        tmup('10;19H')
        inputchar('\033[4;1H')
        stprog("LightEncrypter.py")
        time.sleep(0.5)
    elif scrnum == '5' and curmen == 'prog':
        inputchar('\033[2J')
        type(external_prog)
        inputchar('\033[11A')
        inputchar('\033[3C')
        inputchar('\033[2B')
        inputchar('\033[2;26H')
        type('LIGHTTYPE')
        tuploc = '*'
        inputchar('\033[4;2H')
        curmen = 'ex_prog'
        inputchar('\033[4;2H')
        prognm = 'CHATPY  '
        # progtmu = threading.Thread(target=progtimup, args=())
        # progtmu.start()
        tmup('10;19H')
        inputchar('\033[4;1H')
        stprog("LightType.py")
        time.sleep(0.5)
    elif scrnum == '6' and curmen == 'prog':
        inputchar('\033[2J')
        type(external_prog)
        inputchar('\033[11A')
        inputchar('\033[3C')
        inputchar('\033[2B')
        inputchar('\033[2;26H')
        type('LIGHTCALC')
        tuploc = '*'
        inputchar('\033[4;2H')
        curmen = 'ex_prog'
        inputchar('\033[4;2H')
        prognm = 'CHATPY  '
        # progtmu = threading.Thread(target=progtimup, args=())
        # progtmu.start()
        tmup('10;19H')
        inputchar('\033[4;1H')
        stprog("LightCalc.py")
        time.sleep(0.5)
    elif scrnum == '8' and curmen == 'prog':
        inputchar('\033[2J')
        type(external_prog)
        inputchar('\033[11A')
        inputchar('\033[3C')
        inputchar('\033[2B')
        inputchar('\033[2;26H')
        type('PYBASIC')
        tuploc = '*'
        inputchar('\033[4;2H')
        curmen = 'ex_prog'
        inputchar('\033[4;2H')
        prognm = 'CHATPY  '
        # progtmu = threading.Thread(target=progtimup, args=())
        # progtmu.start()
        tmup('10;19H')
        inputchar('\033[4;1H')
        stprog("basic/interpreter.py")
        time.sleep(0.5)
    elif scrnum == '7' and curmen == 'prog':
        inputchar('\033[2J')
        type(external_prog)
        inputchar('\033[11A')
        inputchar('\033[3C')
        inputchar('\033[2B')
        inputchar('\033[2;26H')
        type('LIGHTSTOCKS')
        tuploc = '*'
        inputchar('\033[4;2H')
        curmen = 'ex_prog'
        inputchar('\033[4;2H')
        prognm = 'CHATPY  '
        # progtmu = threading.Thread(target=progtimup, args=())
        # progtmu.start()
        tmup('10;19H')
        inputchar('\033[4;1H')
        stprog("LightStonks.py")
        time.sleep(0.5)

    elif scrnum == '3' and curmen == 'main':
        inputchar('\033[2J')
        type(games_menu)
        inputchar('\033[11A')
        inputchar('\033[3C')
        inputchar('\033[2B')
        inputchar('\033[2;26H')
        type('GAMES')
        tuploc = '10;19H'
        tmup(tuploc)
        curmen = 'games'
    elif scrnum == '2' and curmen == 'games':
        inputchar('\033[2J')
        type(external_prog)
        inputchar('\033[11A')
        inputchar('\033[3C')
        inputchar('\033[2B')
        inputchar('\033[2;26H')
        type('LIGHTDRAW')
        tuploc = '*'
        inputchar('\033[4;2H')
        curmen = 'ex_prog'
        inputchar('\033[4;2H')
        prognm = 'CHATPY  '
        # progtmu = threading.Thread(target=progtimup, args=())
        # progtmu.start()
        tmup('10;19H')
        inputchar('\033[4;1H')
        stprog("lightbreakout.py")
        time.sleep(0.5)
    elif scrnum == '4' and curmen == 'main':
        inputchar('\033[2J')
        type(doc_menu)
        inputchar('\033[11A')
        inputchar('\033[3C')
        inputchar('\033[2B')
        inputchar('\033[2;30H')
        type('NOTES')
        tuploc = '10;19H'
        tmup(tuploc)
        curmen = 'note'
    elif scrnum == '2' and curmen == 'note':
        inputchar('\033[2J')
        type(loadingscr)
        inputchar('\033[11A')
        inputchar('\033[10;39H')
        encrypt_emb2(f'{name}_notes.txt', '', enckey, f'gtadYYDA6adAD87AD6dayHFG9B7gf{str(zlib.crc32(str(usenmls[name + "_pw"]).encode("utf-8")))}')

        inputchar('\033[2J')
        type(doc_menu)
        inputchar('\033[11A')
        inputchar('\033[3C')
        inputchar('\033[2B')
        inputchar('\033[2;30H')
        type('NOTES')
        tmup(tuploc)

    elif scrnum == '3' and curmen == 'note':
        inputchar('\033[2J')
        type(loadingscr)
        inputchar('\033[11A')
        inputchar('\033[10;39H')
        with open(f'{name}_notes.txt', "r") as file:
            encfdata = file.read()
        try:
            with open('notesdec.txt', "wb") as file:
                file.write(decrypt_emb2(encfdata, f'gtadYYDA6adAD87AD6dayHFG9B7gf{str(zlib.crc32(str(usenmls[name + "_pw"]).encode("utf-8")))}').encode("utf-8"))
        except:
            inputchar('\033[2J')
            print('Incorrect password or data.txt corrupt.')
            print('Fatal error occurred. Press enter to continue, then select 1.')
            input()
            exit()
        inputchar('\033[2J')
        type(loadingscr)
        inputchar('\033[11A')
        inputchar('\033[10;22H')
        type('DOCUMENT OPEN IN NOTEPAD')
        tuploc = '*'
        subprocess.call(['notepad.exe', 'notesdec.txt'])

        inputchar('\033[2J')
        type(loadingscr)
        inputchar('\033[11A')
        inputchar('\033[10;39H')
        with open('notesdec.txt', "r") as file:
            decfdata = file.read()
        encrypt_emb2(f'{name}_notes.txt', decfdata, enckey, f'gtadYYDA6adAD87AD6dayHFG9B7gf{str(zlib.crc32(str(usenmls[name + "_pw"]).encode("utf-8")))}')
        with open('notesdec.txt', "wb") as file:
            file.write(''.encode("utf-8"))

        inputchar('\033[2J')
        type(doc_menu)
        inputchar('\033[11A')
        inputchar('\033[3C')
        inputchar('\033[2B')
        inputchar('\033[2;30H')
        type('NOTES')
        tuploc = '10;19H'
        tmup(tuploc)

    elif scrnum == '4' and curmen == 'note':
        inputchar('\033[2J')
        type(loadingscr)
        inputchar('\033[11A')
        inputchar('\033[10;39H')
        with open(f'{name}_notes.txt', "wb") as file:
            file.write(''.encode("utf-8"))
        inputchar('\033[2J')
        type(doc_menu)
        inputchar('\033[11A')
        inputchar('\033[3C')
        inputchar('\033[2B')
        inputchar('\033[2;30H')
        type('NOTES')
        tmup(tuploc)

    elif scrnum == '7' and curmen == 'main':
        inputchar('\033[2J')
        type(external_prog)
        inputchar('\033[11A')
        inputchar('\033[3C')

        inputchar('\033[2B')
        inputchar('\033[2;26H')
        type('PYTHON PROMPT')
        tuploc = '4;1H'
        tmup(tuploc)
        tuploc = '*'
        curmen = 'py_dbg'
        while True:
            try:
                exec(input('>>> '))
            except KeyboardInterrupt:
                break
            except:
                print('?SYNTAXERROR')

    elif scrnum == '5' and curmen == 'main':
        inputchar('\033[2J')
        type(settings_menu)
        inputchar('\033[11A')
        inputchar('\033[3C')
        inputchar('\033[2B')
        inputchar('\033[2;26H')
        type('LIGHTOS SETTINGS')
        inputchar('\033[6;48H')
        if onoff_setting:
            type('ON')
        elif not onoff_setting:
            type('OFF')
        else:
            type('')
        inputchar('\033[7;48H')
        if fo_setting == 1:
            type('OFF')
        elif fo_setting == 2:
            type('LOW')
        elif fo_setting == 3:
            type('MEDIUM')
        elif fo_setting == 4:
            type('HIGH')
        else:
            type('')
        inputchar('\033[8;48H')
        type(str(mes_setting))
        tuploc = '10;19H'
        tmup(tuploc)
        curmen = 'set'
    elif scrnum == '2' and curmen == 'set':
        inputchar('\033[2J')
        type(setting_submenu)
        inputchar('\033[11A')
        inputchar('\033[3C')
        inputchar('\033[2B')
        inputchar('\033[2;26H')
        type('GENERIC ON/OFF SETTING')
        inputchar('\033[5;2H')
        type('1. ON')
        inputchar('\033[7;2H')
        type('2. OFF')
        tuploc = '10;13H'
        tmup(tuploc)
        inputchar('\033[10;2H')
        settocg = input('SELECTION: ')
        if settocg == '1':
            onoff_setting = True
        elif settocg == '2':
            onoff_setting = False
        inputchar('\033[2J')
        type(loadingscr)
        inputchar('\033[11A')
        inputchar('\033[10;39H')

        with open(f'{name}_settings.txt', 'w+') as sett:
            sett.write(f'''mes_setting = '{mes_setting}' 
onoff_setting = {onoff_setting}
fo_setting =  {fo_setting}''')

        inputchar('\033[2J')
        type(settings_menu)
        inputchar('\033[11A')
        inputchar('\033[3C')
        inputchar('\033[2B')
        inputchar('\033[2;26H')
        type('LIGHTOS SETTINGS')
        inputchar('\033[6;48H')
        if onoff_setting:
            type('ON')
        elif not onoff_setting:
            type('OFF')
        else:
            type('')
        inputchar('\033[7;48H')
        if fo_setting == 1:
            type('OFF')
        elif fo_setting == 2:
            type('LOW')
        elif fo_setting == 3:
            type('MEDIUM')
        elif fo_setting == 4:
            type('HIGH')
        else:
            type('')
        inputchar('\033[8;48H')
        type(str(mes_setting))
        tuploc = '10;19H'
        tmup(tuploc)
        curmen = 'set'


    elif scrnum == '3' and curmen == 'set':
        inputchar('\033[2J')
        type(setting_submenu)
        inputchar('\033[11A')
        inputchar('\033[3C')
        inputchar('\033[2B')
        inputchar('\033[2;26H')
        type('FOUR OPTION SETTING')
        inputchar('\033[5;2H')
        type('1. OFF')
        inputchar('\033[6;2H')
        type('2. LOW')
        inputchar('\033[7;2H')
        type('3. MEDIUM')
        inputchar('\033[8;2H')
        type('4. HIGH')
        tuploc = '10;13H'
        tmup(tuploc)
        inputchar('\033[10;2H')
        settocg = input('SELECTION: ')
        if settocg == '1':
            fo_setting = 1
        elif settocg == '2':
            fo_setting = 2
        elif settocg == '3':
            fo_setting = 3
        elif settocg == '4':
            fo_setting = 4
        else:
            fo_setting = 0

        inputchar('\033[2J')
        type(loadingscr)
        inputchar('\033[11A')
        inputchar('\033[10;39H')
        with open(f'{name}_settings.txt', 'w+') as sett:
            sett.write(f'''mes_setting = '{mes_setting}'
onoff_setting = {onoff_setting}
fo_setting =  {fo_setting}''')

        inputchar('\033[2J')
        type(settings_menu)
        inputchar('\033[11A')
        inputchar('\033[3C')
        inputchar('\033[2B')
        inputchar('\033[2;26H')
        type('LIGHTOS SETTINGS')
        inputchar('\033[6;48H')
        if onoff_setting:
            type('ON')
        elif not onoff_setting:
            type('OFF')
        else:
            type('')
        inputchar('\033[7;48H')
        if fo_setting == 1:
            type('OFF')
        elif fo_setting == 2:
            type('LOW')
        elif fo_setting == 3:
            type('MEDIUM')
        elif fo_setting == 4:
            type('HIGH')
        else:
            type('')
        inputchar('\033[8;48H')
        type(str(mes_setting))
        tuploc = '10;19H'
        tmup(tuploc)
        curmen = 'set'

    elif scrnum == '4' and curmen == 'set':
        inputchar('\033[2J')
        type(setting_submenu)
        inputchar('\033[11A')
        inputchar('\033[3C')
        inputchar('\033[2B')
        inputchar('\033[2;26H')
        type('GENERIC MESSAGE SETTING')
        tuploc = '10;13H'
        tmup(tuploc)
        inputchar('\033[10;2H')
        settocg = input('CUSTOM MESSAGE: ')
        mes_setting = str(settocg).upper()
        inputchar('\033[2J')
        type(loadingscr)
        inputchar('\033[11A')
        inputchar('\033[10;39H')
        with open(f'{name}_settings.txt', 'w+') as sett:
            sett.write(f'''mes_setting = '{mes_setting}' 
onoff_setting = {onoff_setting}
fo_setting =  {fo_setting}''')

        inputchar('\033[2J')
        inputchar('\033[2J')
        type(settings_menu)
        inputchar('\033[11A')
        inputchar('\033[3C')
        inputchar('\033[2B')
        inputchar('\033[2;26H')
        type('LIGHTOS SETTINGS')
        inputchar('\033[6;48H')
        inputchar('\033[6;48H')
        if onoff_setting:
            type('ON')
        elif not onoff_setting:
            type('OFF')
        else:
            type('')
        inputchar('\033[7;48H')
        if fo_setting == 1:
            type('OFF')
        elif fo_setting == 2:
            type('LOW')
        elif fo_setting == 3:
            type('MEDIUM')
        elif fo_setting == 4:
            type('HIGH')
        else:
            type('')
        inputchar('\033[8;48H')
        type(str(mes_setting))
        tuploc = '10;19H'
        tmup(tuploc)
        curmen = 'set'

    elif scrnum == '6' and curmen == 'main':
        inputchar('\033[2J')
        type(plugin_menu)
        inputchar('\033[11A')
        inputchar('\033[3C')
        inputchar('\033[2B')
        inputchar('\033[2;26H')
        type('PLUGIN MENU')
        tuploc = '10;19H'
        tmup(tuploc)
        curmen = 'plug'
        os.chdir('plugins')
        cwd = os.getcwd()
        files = []
        for (dirpath, dirnames, filenames) in walk(cwd):
            files.extend(filenames)
            break
        filenumls = {}
        j = 2
        for file in files:
            filenumls[str(j)] = file
            j += 1
        j = 5
        i = 2
        for file in files:
            try:
                console_log('plugin menu '+str(j)+str(i))
                dummy, plugn = filenumls[str(i)].split('--')
                if j > 13:
                    inputchar(f'\033[{j-10};45H')
                elif j > 8:
                    inputchar(f'\033[{j-5};23H')
                else:
                    inputchar(f'\033[{j};2H')
                plugntr = plugn.replace(".py","")[:16]
                type(f'{j-3}. {plugntr}')
                j += 1
                i += 1
            except:
                i += 1


        while True:
            inputchar('\033[10;2H')
            ussl = input('ENTER SELECTION: ')
            inputchar('\033[10;1H')
            type('█                                                                 █')
            if ussl == '1':
                switchscr('1')
                cwd = os.getcwd()
                cmd = os.path.dirname(cwd)
                os.chdir(cmd)
                break
            elif ussl.upper() == 'EXIT':
                os._exit(0)
            elif ussl in filenumls:
                console_log('running plugin')
                inputchar('\033[2J')
                type(loadingscr)
                inputchar('\033[11A')
                inputchar('\033[10;22H')
                type('PLUGIN LOADING...')
                try:
                    tuploc = '*'
                    subprocess.call(['python', filenumls[ussl]])
                except:
                    continue
                curmen = 'main'
                cwd = os.getcwd()
                cmd = os.path.dirname(cwd)
                os.chdir(cmd)
                switchscr('6')
                break
            else:
                continue






def inputchar(key):
    sys.stdout.write(key)
    sys.stdout.flush()

def type(t):
    inputchar(t)
    # for l in t:
    #     sys.stdout.write(l)
    #     sys.stdout.flush()
    #     # j = 0
    #     # while j != 10000:
    #     #     j+=1
def strtlstn():
    with Listener(on_press=on_press) as listener:
        listener.join()
def strttmup():
    global tuploc
    while True:
        if tuploc != '*':
            t = time.localtime()
            current_time = time.strftime("%I:%M %p", t)
            inputchar('\033[2;2H')
            type(current_time)
            inputchar(f'\033[{tuploc}')
            console_log('clock.update('+current_time+') done')
            time.sleep(30)
def tmup(tul):
    t = time.localtime()
    current_time = time.strftime("%I:%M %p", t)
    inputchar('\033[2;2H')
    type(current_time)
    inputchar(f'\033[{tul}')
    console_log('clock.update() done temp')

def stprog(pnm):
    try:
        subprocess.call(['python', pnm])
    except:
        # switchscr('1')
        pass
    switchscr('1')

def progtimup():
    global curmen
    global prognm
    while curmen == 'chat':
        try:
            time.sleep(30)
            t = time.localtime()
            current_time = time.strftime("%I:%M %p", t)
            inputchar('\033[H')
            tts = f'''███████████████████████████████████████████████████████████████████
█{current_time}                                                 LIGHT OS█
███████████████████████████████████████████████████████████████████'''
            type(tts)
            inputchar('\033[2;26H')
            type(prognm)
            inputchar('\033[11;1H')
        except:
            continue



def encrypt_emb2(filename, data, key, password):
    """
    Given a filename (str) and key (bytes), it encrypts the file and write it
    """
    f = Fernet(key)
    try:
        file_data = data.encode("utf-8")
    except MemoryError:
        print('How have you done this? There are too many users!')
        exit()
    except:
        print('A error occurred.')
        exit()

    # encrypt data
    try:
        encrypted_data = f.encrypt(file_data)
        password_enc = f.encrypt(password.encode("utf-8"))
        # write the encrypted file
        with open(filename, "wb") as file:
            file.write(encrypted_data)
        with open(filename, "a") as file:
            file.write('`-`' + key.decode("utf-8"))
        with open(filename, "a") as file:
            file.write(',-,' + password_enc.decode("utf-8"))
    except:
        print('A error occurred.')
        exit()


def decrypt_emb2(data, password):
    """
    Given a filename (str) and key (bytes), it decrypts the file and write it
    """
    data = data.encode("utf-8")
    sep = '`-`'
    sep = sep.encode("utf-8")
    sep2 = ',-,'
    sep2 = sep2.encode("utf-8")
    encrypted_data, file_data = data.split(sep)
    key, rpassword = file_data.split(sep2)
    f = Fernet(key)
    # decrypt data
    try:
        decrypted_data = f.decrypt(encrypted_data)
        password_dec = f.decrypt(rpassword)
        # write the original file
        if password_dec.decode("utf-8") == password:
                rdat = decrypted_data.decode("utf-8")
        else:
            print('data.txt corrupt.')
            exit()
    except:
        print('A error occurred.')
        exit()
    return rdat



#boot
# print('Initializing Display Drivers')
# i = 16
# while i > 0:
#     sys.stdout.write('.')
#     sys.stdout.flush()
#     time.sleep(random.uniform(0.2, 0.9))
#     i -= 1
# print('\nDone! \n')
#
# print('Initializing Basic I/O')
# i = 16
# while i > 0:
#     sys.stdout.write('.')
#     sys.stdout.flush()
#     time.sleep(random.uniform(0.2, 0.9))
#     i -= 1
# print('\nDone! \n')
#
# print('Initializing Human Input Devices')
# i = 16
# while i > 0:
#     sys.stdout.write('.')
#     sys.stdout.flush()
#     time.sleep(random.uniform(0.2, 0.9))
#     i -= 1
# print('\nDone! \n')
#
# print('Starting LightOS')
# i = 16
# while i > 0:
#     sys.stdout.write('.')
#     sys.stdout.flush()
#     time.sleep(random.uniform(0.2, 0.9))
#     i -= 1
# print('\nDone! \n')

time.sleep(0.8)
usenmls = {}
try:
    with open('data.txt', 'r') as data:
        decdat = decrypt_emb2(data.read(), 'gtTfs7Adh6G3j835GkdsJFYU86389llke')
        exec(decdat)
except:
    decdat = ''
    with open('data.txt', 'w+') as data:
        data.write('')
    encrypt_emb2('data.txt', '', enckey, 'gtTfs7Adh6G3j835GkdsJFYU86389llke')


console_log('drawing password screen')
type(usenmpw_menu)
inputchar('\033[11A')
inputchar('\033[5;23H')
name = input('USERNAME: ').upper()
inputchar('\033[7;23H')
passwd = input('PASSWORD: ')
if name + '_pw' in usenmls:
    if usenmls[name + '_pw'] != passwd:
        inputchar('\033[9;23H')
        type(f'WRONG PASSWORD FOR {name}!')
        console_log('password for '+name+'was not correct')
        exit()
else:
    console_log('password for ' + name + 'was correct')
    inputchar('\033[2J')
    type(loadingscr)
    inputchar('\033[11A')
    inputchar('\033[10;39H')
    encrypt_emb2('data.txt', decdat + f'usenmls["{name}_pw"] = "{passwd}" \n', enckey, 'gtTfs7Adh6G3j835GkdsJFYU86389llke')
    with open('data.txt', 'r') as data:
        decdat = decrypt_emb2(data.read(), 'gtTfs7Adh6G3j835GkdsJFYU86389llke')
        exec(decdat)
    # not used:
    # with open('data.txt', 'a') as data:
    #     data.write(f'usenmls["{name}_pw"] = "{passwd}" \n')

console_log('name inputted is '+name)

try:
    with open(f'{name}_settings.txt', 'r') as sett:
        exec(sett.read())
except:
    with open(f'{name}_settings.txt', 'w+') as sett:
        sett.write('''mes_setting = '' 
onoff_setting = False
fo_setting = 1 ''')
    mes_setting = ''
    onoff_setting = False
    fo_setting = 1

inputchar('\033[2J')
type(main_menu)
inputchar('\033[11A')
inputchar('\033[3C')
inputchar('\033[2B')
inputchar('\033[2;26H')
type(name)
inputchar('\033[2;49H')
type('TYPE EXIT TO QUIT ')
tuploc = '10;19H'
timup = threading.Thread(target=strttmup, args=())
timup.start()
time.sleep(0.1)
# sys.stdout.write('\033[10;2H ENTER SELECTION: ')
# usrsel = str(sys.stdin.read(2))
curmen = 'main'

#main
lisn = threading.Thread(target=strtlstn, args=())
lisn.start()
console_log('now in main loop')
while True:
    try:
        while curmen != 'ex_prog':
            inputchar('\033[10;2H')
            usrsel = input('ENTER SELECTION: ')
            inputchar('\033[10;1H')
            type('█                                                                 █')
            if usrsel.lower() == 'antigravity':
                import antigravity
            console_log('running program')
            switchscr(str(usrsel))
            console_log('done running '+usrsel)
    except:
        continue
