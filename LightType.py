import msvcrt
import sys
import random
import time
import os
import msvcrt as m

def wait():

   m.getch()

typing_speed = 50 #wpm
def slow_type(t):
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        #time.sleep(random.random()*10.0/typing_speed)
        #time.sleep(random.uniform(0.2, 0.3))
        wait()

    print ('')

filetoprint = input('File to type: ')
typing_speed = float(input('Wpm: '))

with open(filetoprint, 'r') as file:
    fileData = file.read()
    print(file)

slow_type(fileData)