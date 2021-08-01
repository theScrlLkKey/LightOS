#imports here
import time
import random
from os import walk
import os
import shutil
import subprocess
from pythonping import ping
import zipfile
# import win32com.client as comclt
from pynput.keyboard import Listener, Key
import colorama
import threading





#defs here
cached_cmds = []
# wsh= comclt.Dispatch("WScript.Shell")

def GetCmd(prompt):
    usrinput = input(prompt)
    #TODO
    return usrinput
def CheckCmd(cmd):


    if cmd == 'dir' or cmd == 'ls':
        cwd = os.getcwd()
        for (dirpath, dirnames, filenames) in walk(cwd):
            f.extend(filenames)
            break
        out = dirnames + filenames
        out = '\n'.join(out)
        return out
    elif cmd == 'cache.start':
        index = 0
        out = 'Cache starting'
        print(out)
        ccmd = ''
        cached_cmds = []
        while ccmd != 'cache.close':
            out = ''
            cwd = os.getcwd()
            cdir = os.path.abspath(cwd)
            inputprompt = f'{cdir}> '
            ccmd = GetCmd(inputprompt)
            if ccmd == 'dir' or ccmd == 'ls':
                index += 1
                cached_cmds.append(ccmd)
                cwd = os.getcwd()
                for (dirpath, dirnames, filenames) in walk(cwd):
                    f.extend(filenames)
                    break
                out = dirnames + filenames
                out = '\n'.join(out)
            elif 'cd' in ccmd:
                index += 1
                cached_cmds.append(ccmd)
                out = ''
                ccmd = ccmd.replace('cd ', '')
                ccmd = ccmd.replace('', '')
                try:
                    os.chdir(ccmd)
                except:
                    out = 'Folder not found'
            elif ccmd == 'back':
                index += 1
                cached_cmds.append(ccmd)
                out = ''
                cwd = os.getcwd()
                try:
                    cmd = os.path.dirname(cwd)
                    os.chdir(cmd)
                except:
                    out = 'Folder not found'
            elif ccmd == 'cache.undo':
                try:
                    cached_cmds.pop(index-1)
                    index -= 1
                except:
                    out = 'Nothing to undo'
            elif ccmd == 'cache.back':
                try:
                    index -= 1
                except:
                    out = 'Too far back'
            elif ccmd == 'cache.forward':
                try:
                    index += 1
                except:
                    out = 'Too far forward'
            elif ccmd == 'cache.index':
                out = index
            elif ccmd == 'cache.cache':
                out = cached_cmds
            elif ccmd == 'cache.commit':
                cindex = index
                index = 0
                aindex = len(cached_cmds)
                while index < aindex:
                    cccmd = cached_cmds[index]
                    print(CheckCmd(cccmd))
                    index += 1
                index = cindex

            else:
                index += 1
                cached_cmds.append(ccmd)
                out = 'Done'
            print(out)
            out = ''
        out = 'Closing cache'

        return out


    elif 'rename ' in cmd:
        out = ''
        cmd = cmd.replace('rename ', '')
        src, dst = cmd.split(', ')
        print('Renaming...')
        try:
            os.rename(src, dst)
        except:
            out = 'File/folder not found'
    elif 'cmd ' in cmd or 'shell ' in cmd:
        out = ''
        cmd = cmd.replace('cmd ', '')
        cmd = cmd.replace('shell ', '')
        stream = os.popen(cmd)
        output = stream.read()
        out = output
    elif 'cd ' in cmd:
        out = ''
        cmd = cmd.replace('cd ', '')
        cmd = cmd.replace('', '')
        try:
            os.chdir(cmd)
        except:
            out = 'Folder not found'
    elif cmd == 'back':
        out = ''
        cwd = os.getcwd()
        try:
            cmd = os.path.dirname(cwd)
            os.chdir(cmd)
        except:
            out = 'Folder not found'
    elif 'run ' in cmd or 'open ' in cmd:
        out = ''
        cmd = cmd.replace('run ', '')
        cmd = cmd.replace('open ', '')
        cmd = cmd.replace('', '')
        try:
            os.startfile(cmd)
        except:
            out = 'File not found'
    elif 'edit ' in cmd:
        out = ''
        cmd = cmd.replace('edit ', '')
        cmd = cmd.replace('', '')
        try:
            subprocess.call(['notepad.exe', cmd])
        except:
            out = 'File not found'
    elif 'lookat ' in cmd:
        out = ''
        cmd = cmd.replace('lookat ', '')
        cmd = cmd.replace('', '')
        try:
            with open(cmd, 'r') as data:
                read_data = data.read()
                out = read_data
        except:
            try:
                with open(cmd, 'rb') as data:
                    read_data = data.read()
                    out = read_data
                    readdat = str(out).split('\\')
                    #out = '\n'.join(readdat)
                    out = readdat
            except:
                out = 'File not found or too big'
    elif 'copydir ' in cmd:
        out = ''
        cmd = cmd.replace('copydir ', '')
        src, dst = cmd.split(', ')
        dst = dst + '\\' + src
        print('Copying...')
        try:
            shutil.copytree(src, dst)
        except:
            out = 'Folder not found'
    elif 'copy ' in cmd:
        out = ''
        cmd = cmd.replace('copy ', '')
        src, dst = cmd.split(', ')
        print('Copying...')
        try:
            shutil.copy2(src, dst)
        except:
            out = 'File not found'
    elif 'mkdir ' in cmd:
        out = ''
        cmd = cmd.replace('mkdir ', '')
        try:
            os.mkdir(cmd)
        except:
            out = 'A error occurred'
    elif 'deldir -full ' in cmd:
        out = ''
        cmd = cmd.replace('deldir -full ', '')
        print('Deleting...')
        try:
            shutil.rmtree(cmd)
        except:
            out = 'Folder not found'
    elif 'deldir ' in cmd:
        out = ''
        cmd = cmd.replace('deldir ', '')
        print('Deleting...')
        try:
            os.rmdir(cmd)
        except:
            out = 'Folder not found/folder not empty, use deldir -full to remove non-empty folders.'
    elif 'del ' in cmd:
        out = ''
        cmd = cmd.replace('del ', '')
        print('Deleting...')
        try:
            os.remove(cmd)
        except:
            out = 'File not found'
    elif 'move ' in cmd:
        out = ''
        cmd = cmd.replace('move ', '')
        src, dst = cmd.split(', ')
        print('Moving...')
        try:
            shutil.move(src, dst)
        except:
            out = 'File/folder not found'
    elif 'unzip ' in cmd:
        out = ''
        cmd = cmd.replace('unzip ', '')
        print('Unzipping...')
        try:
            with zipfile.ZipFile(cmd, 'r') as zip_ref:
                zip_ref.extractall(cmd.strip('.zip'))
        except:
            out = 'Zip not found'
    elif 'unpack ' in cmd:
        out = ''
        cmd = cmd.replace('unpack ', '')
        print('Unpacking...')
        try:
            shutil.unpack_archive(cmd, cmd + '-unpacked')
        except:
            out = 'Archive not found/invalid format'

    elif 'archive ' in cmd:
        out = ''
        cmd = cmd.replace('archive ', '')
        dir, atyp = cmd.split(', ')
        if atyp == zip:
            print('Zipping...')
        else:
            print('Archiving...')
        try:
            shutil.make_archive(dir, atyp, dir)
        except:
            out = 'Invalid archive format'
    elif 'ping ' in cmd:
        out = ''
        cmd = cmd.replace('ping ', '')
        try:
            response_list = ping(cmd, size=40, count=8)
            out = response_list
        except:
            out = 'Ping failed'
    elif cmd == 'exit':
        out = ''
        exit()

    else:
        out = '?SYNTAXERROR'
    return out

# def strtlstn():
#     with Listener(on_press=on_press) as listener:
#         listener.join()
#
# def on_press(key):
#     if key == Key.menu:
#         exit()
#     else:  # If anything else was pressed, write [<key_name>]
#         pass
#
#
#
#
#
# #main
# lisn = threading.Thread(target=strtlstn, args=())
# lisn.start()


#set defaults
cwd = os.getcwd()
f = []
inputprompt = ' '
cdir = 'C:\\'

#main here
while True:
    cwd = os.getcwd()
    cdir = os.path.abspath(cwd)
    inputprompt = f'{cdir}> '
    usrcmd = GetCmd(inputprompt)
    output = CheckCmd(usrcmd)
    print(output)
    # wsh.SendKeys("{SCROLLLOCK}")
    # time.sleep(0.03)
    # wsh.SendKeys("{SCROLLLOCK}")