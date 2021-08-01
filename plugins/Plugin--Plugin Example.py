# Plugin code
import colorama
import sys
colorama.init()
sys.stdout.write('\033[2J')
sys.stdout.flush()
# End of plugin code, your code goes below
import time

print('Hello World!')
time.sleep(1)
name = input('What is your name? ')
print('Hello '+name+'!')
time.sleep(2)
