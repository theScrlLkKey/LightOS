#imports
import time
import random
from os import walk
import os
import shutil
import subprocess
import sys
from pynput.keyboard import Listener, Key, KeyCode
import colorama
import threading

#defs
colorama.init()
br = False
dl = False

def strtlstn():
    with Listener(on_press=on_press) as listener:
        listener.join()

def on_press(key):
    global br
    global dl
    if key == Key.left:
        inputchar('\033[1D')
    elif key == Key.right:
        inputchar('\033[1C')
    elif key == Key.up:
        inputchar('\033[1A')
    elif key == Key.down:
        inputchar('\033[1B')
    elif key == Key.end:
        if br == True:
            br = False
        elif br == False:
            br = True
            dl = False
    elif key == Key.home:
        if dl == True:
            dl = False
        elif dl == False:
            dl = True
            br = False
    elif key == Key.menu:
        exit()
    elif key == Key.shift:
        exit()
    else:
        pass

    if br == True:
        inputchar('█')
        inputchar('\033[1D')
    if dl == True:
        inputchar(' ')
        inputchar('\033[1D')


def inputchar(key):
    sys.stdout.write(key)
    sys.stdout.flush()


#main
lisn = threading.Thread(target=strtlstn, args=())
lisn.start()
# while True:
#     time.sleep(0)
#     # b_dir = random.randint(1,4)
#     # if b_dir == 1:
#     #     inputchar('\033[1D')
#     # elif b_dir == 2:
#     #     inputchar('\033[1C')
#     # elif b_dir == 3:
#     #     inputchar('\033[1A')
#     # elif b_dir == 4:
#     #     inputchar('\033[1B')
#     if br == True:
#         inputchar('█')
#         inputchar('\033[1D')