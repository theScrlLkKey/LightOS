import time
import random
from os import walk
import os
import shutil
import subprocess
import sys
from pynput.keyboard import Listener, Key
import colorama
import threading
from cryptography.fernet import Fernet


#menus

main_menu = '''███████████████████████████████████████████████████████████████████
█00:00 AM                                            DOCUMENT MENU█  
███████████████████████████████████████████████████████████████████
█OPTIONS:                                                         █
█(N)EW                                                            █
█(E)DIT                                                           █
█(D)ELETE                                                         █
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

def switchscr(scrnum):

    if scrnum == 'N':
        encrypt_emb2('notes.txt', '', enckey, 'gtadYYDA6adAD87AD6dayHFG9B7gf')
    elif scrnum == 'E':
        with open('notes.txt', "r") as file:
            encfdata = file.read()

        with open('notesdec.txt', "wb") as file:
            file.write(decrypt_emb2(encfdata, 'gtadYYDA6adAD87AD6dayHFG9B7gf').encode("utf-8"))


        subprocess.call(['notepad.exe', 'notesdec.txt'])


        with open('notesdec.txt', "r") as file:
            decfdata = file.read()

        encrypt_emb2('notes.txt', decfdata, enckey, 'gtadYYDA6adAD87AD6dayHFG9B7gf')

        with open('notesdec.txt', "wb") as file:
            file.write('')
    elif scrnum == 'D':
        with open('notes.txt', "wb") as file:
            file.write('')






def inputchar(key):
    sys.stdout.write(key)
    sys.stdout.flush()

def type(t):
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        # j = 0
        # while j != 10000:
        #     j+=1
def strttmup():
    global tuploc
    while True:
        if tuploc != '*':
            t = time.localtime()
            current_time = time.strftime("%I:%M %p", t)
            inputchar('\033[2;2H')
            type(current_time)
            inputchar(f'\033[{tuploc}')
            time.sleep(30)
def tmup(tul):
    t = time.localtime()
    current_time = time.strftime("%I:%M %p", t)
    inputchar('\033[2;2H')
    type(current_time)
    inputchar(f'\033[{tul}')

def stprog(pnm):
    try:
        subprocess.call(['python', pnm])
    except:
        switchscr('1')
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






try:
    with open('data.txt', 'r') as data:
        decdat = decrypt_emb2(data.read(), 'gtTfs7Adh6G3j835GkdsJFYU86389llke')
except:
    print('An error occurred.')
    exit()


inputchar('\033[2J')
type(main_menu)
inputchar('\033[11A')
inputchar('\033[3C')
inputchar('\033[2B')
inputchar('\033[2;26H')
tuploc = '10;19H'
timup = threading.Thread(target=strttmup, args=())
timup.start()
time.sleep(0.1)
# sys.stdout.write('\033[10;2H ENTER SELECTION: ')
# usrsel = str(sys.stdin.read(2))
curmen = 'main'

while True:
    try:
        while curmen != 'ex_prog':
            inputchar('\033[10;2H')
            usrsel = input('ENTER SELECTION: ')
            inputchar('\033[10;1H')
            type('█                                                                 █')
            if usrsel.lower() == 'antigravity':
                import antigravity
            switchscr(str(usrsel))
    except:
        continue
