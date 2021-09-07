import time
import random
import string

stayInmainLoop = 1

lvl = 2
xp = 0

item1 = 0
item2 = 0
item3 = 0
item4 = 0

gend = 0

ePic=''' 
????????????
????????????
????????????
????????????
????????????
????????????
'''


mapvartxt = r"""

story = '''
beginning story goes here lol
'''
endstory = '''
you won my test game lol such good wow
'''

#Maps

e1m1map = '''================




             ================'''
dun1map='''
              _________________________        
              |                       |
                                      |
                                      |
              |                       |
              |                       |
              |                       |
              |                       |
              |                       |
              |                       |     
              |               |=======|
              |               |=======|     
              -------------------------




              '''



dun2map = '''
              _________________________
              |                       |
              | .                     
              |                       
              |           o           |
              |                       |
              |                       |
              |    o0           8     |
              |                       |
              |                       |     
              |                       |
              |                       |     
              --           ------------




              '''








dun3map =  r'''

              |     | 
              |     |
              |     |
              |     |
              |     |
              |     |
              |     |
             /       \
      -------         -----------      
                        
                                        
      ---------------------------



'''




dun4map = r'''

           |-----------------------
           |
           |
           |-----------------------


'''

dun5map = r'''

           -----------------------|
                                  |
                                  | 
           -----------------------|


'''

dun6map = r'''





'''


dun7map = r'''





'''
dun8map = r'''





'''
dun9map = r'''





'''
dun10map = r'''





'''
dun11map = r'''





'''
dun12map = r'''





'''
dun13map = r'''





'''
dun14map = r'''





'''

dun15map = r'''





'''



#Stories


e1m1story='You are the DOOMGUY!'
dun1story='This is your house'
dun2story='This is your yard'
dun3story='This is broadway'
dun4story='Looks like a dead end'
dun5story='Looks like a dead end'
dun6story='Looks like a dead end'
dun7story='Looks like a dead end'
dun8story='Looks like a dead end'
dun9story='Looks like a dead end'
dun10story='Looks like a dead end'
dun11story='Looks like a dead end'
dun12story='Looks like a dead end'
dun13story='Looks like a dead end'
dun14story='Looks like a dead end'
dun15story='Looks like a dead end'

eName='?' #Change the enemy name. You can change it in the move handler too.
#Enemy picture thing. You can change it in the move handler too.
ePic=''' 
????????????
????????????
????????????
????????????
????????????
????????????
'''


#Move database, A is level(eg, a = 2 is dun1)B is the players move(eg,b == l is left) item1-4 are items (eg item2 = 5), do what you want.

def moveHandlr(b,a):
    #print(str(b)+str(a))
    global needKey

    if a == 1:
        if b == 'l':
            lvl = a
        elif b == 'r':
            lvl = a
        elif b == 'f':
            lvl = a
        elif b == 'b':
            lvl = a
        else:
            lvl = a
    
    elif a == 2:
        if b == 'l':
            lvl = 3
        elif b == 'r':
            lvl = a
        elif b == 'f':
            lvl = a
        elif b == 'b':
            lvl = a
        else:
            lvl = a

    elif a == 3:
        if b == 'l':
            lvl = a
        elif b == 'r':
            lvl = 2
        elif b == 'f':
            lvl = a
        elif b == 'b':
            lvl = 4
        else:
            lvl = a

    elif a == 4:
        if b == 'l':
            lvl = 5
        elif b == 'r':
            lvl = 6
            
        elif b == 'f':
            lvl = 3
        elif b == 'b':
            lvl = a
        else:
            lvl = a
    elif a == 5:
        if b == 'l':
            if needKey == 1 or needKey == 2:
                print ('You need a key.')
                lvl = a
                needKey=1
            else:
                print('You have a key!')
                lvl = 2
                needKey = 2
            
        elif b == 'r':
            lvl = 4
        elif b == 'f':
            lvl = a
        elif b == 'b':
            lvl = a
        else:
            lvl = a

    elif a == 6:
        
        if b == 'l':
            lvl = 4
        elif b == 'r':
            lvl = a
        elif b == 'f':
            lvl = a
        elif b == 'b':
            lvl = a
        else:
            lvl = a
    elif a == 7:
        if b == 'l':
            lvl = a
        elif b == 'r':
            lvl = a
        elif b == 'f':
            lvl = a
        elif b == 'b':
            lvl = a
        else:
            lvl = a
    elif a == 8:
        if b == 'l':
            lvl = a
        elif b == 'r':
            lvl = a
        elif b == 'f':
            lvl = a
        elif b == 'b':
            lvl = a
        else:
            lvl = a
    elif a == 9:
        if b == 'l':
            lvl = a
        elif b == 'r':
            lvl = a
        elif b == 'f':
            lvl = a
        elif b == 'b':
            lvl = a
        else:
            lvl = a
    elif a == 10:
        if b == 'l':
            lvl = a
        elif b == 'r':
            lvl = a
        elif b == 'f':
            lvl = a
        elif b == 'b':
            lvl = a
        else:
            lvl = a
    elif a == 11:
        if b == 'l':
            lvl = a
        elif b == 'r':
            lvl = a
        elif b == 'f':
            lvl = a
        elif b == 'b':
            lvl = a
        else:
            lvl = a
    elif a == 12:
        if b == 'l':
            lvl = a
        elif b == 'r':
            lvl = a
        elif b == 'f':
            lvl = a
        elif b == 'b':
            lvl = a
        else:
            lvl = a
    elif a == 13:
        if b == 'l':
            lvl = a
        elif b == 'r':
            lvl = a
        elif b == 'f':
            lvl = a
        elif b == 'b':
            lvl = a
        else:
            lvl = a
    elif a == 14:
        if b == 'l':
            lvl = a
        elif b == 'r':
            lvl = a
        elif b == 'f':
            lvl = a
        elif b == 'b':
            lvl = a
        else:
            lvl = a
    elif a == 15:
        if b == 'l':
            lvl = a
        elif b == 'r':
            lvl = a
        elif b == 'f':
            lvl = a
        elif b == 'b':
            lvl = a
        else:
            lvl = a
    elif a == 16:
        if b == 'l':
            lvl = a
        elif b == 'r':
            lvl = a
        elif b == 'f':
            lvl = a
        elif b == 'b':
            lvl = a
        else:
            lvl = a
            
            
    else:
        lvl = a

    


    return lvl
#Item sutffs

item1Name = 'Health potion'
item2Name = 'sPotion'
item3Name = 'Not a real key'
item4Name = 'Coin'
 
def useItem():
    global item1
    global item2
    global item3
    global item4
    #This is for variable to modify, check docs.
    global pHealth
    global x
    global x
    global x
    global x
    global x
    Use = input('What item do you want to use?')
    itmToUse = Use.lower()
    if item1Name.lower() in itmToUse and item1 > 0:
        pHealth += 5
        item1 -= 1
        print('slurp slurp')
    elif item2Name.lower() in itmToUse and item2 > 0:
        item2 -= 1
    elif item3Name.lower() in itmToUse and item3 > 0:
        item3 -= 1
    elif item4Name.lower() in itmToUse and item4 > 0:
        item4 -= 1
    else:
        print('You don\'t have any ' + str(itmToUse))


def EoG():
    global lvl
    global gend
    if lvl == 6: #End of game level number 
        gend = 1

"""




def getCmd (b):

    #print(str(b))
    a=input('Enter a command: ')
    print("Your command is " + str(a)) 
    return a

def plyrAction (j,a,lvl,c,d,plyrMove,v):
    b = j.lower()
    
    #print('You choose to ' + str(b))

    if 'west' in b:
        plyrMove = 'l'

    elif 'east' in b:
        plyrMove = 'r'

    elif 'north' in b:
        plyrMove = 'f'

    elif 'south' in b:
        plyrMove = 'b'

    elif 'map' in b:
        showMap(currentLoc,a,lvl,v)
        plyrMove = 'map'
    elif 'save' in b:
        saveGame(b,lvl,c,d,plyrMove,v)
        plyrMove = 'sav'
    elif 'load "$",8' in b:
        commBasic()
        plyrMove = 'c64'
    elif 'load' in b:
        loadGame()
        plyrMove = 'ld'
    elif 'debug' in b:
        plyrMove = 'dbg'
    elif 'commands' in b:
        plyrMove = 'cmd'
        print('''
To move, type north, south, east, or west
In an enemy attack, type bow, sword, or run
To view your items, type inventory
To use an item, type use and the name of the item
To save your game, type save
To view these commands at a later date, type commands.''')

    elif 'inventory' in b:
        try:
            openInventory()
        except:
            frmt = input('Error when reading map file, do you want to format the file?(y/n)')
            if frmt == 'y':
                time.sleep(2.4)
                with open(path,'w+') as maps:
                    maps.write(mapvartxt)
                with open(path,'r') as maps:
                    maptbl = maps.read()
                    exec(maptbl)
                    print('Format complete!')
                    openInventory()
        
            else:
                print('Ok, please fix the map file.')
        
        plyrMove = 'inv'
    elif 'use' in b:
        try:
            useItem()   
        except:
            frmt = input('Error when reading map file, do you want to format the file?(y/n)')
            if frmt == 'y':
                time.sleep(2.4)
                with open(path,'w+') as maps:
                    maps.write(mapvartxt)
                with open(path,'r') as maps:
                    maptbl = maps.read()
                    exec(maptbl)
                    print('Format complete!')
                    useItem()
        
            else:
                print('Ok, please fix the map file.')
        
        plyrMove = 'use'
    elif 'antigravity' in b:
        import antigravity
    else:
        plyrMove = 'error'
        print('That is not a valid command')

    #print(str(plyrMove))
    return plyrMove


def showMap (b,story,lvl,v):
    if b == 'E1M1':
        print(str(e1m1map))
        print (str(story) + ' -- xp:'+ str(xp)+' health:' + str(pHealth))

    elif b == 'dun1':
        print (str(dun1map))
        print (str(story) + ' -- xp:'+ str(xp)+' health:' + str(pHealth))
        

    elif b == 'dun2':
        print (str(dun2map))
        print (str(story) + ' -- xp:'+ str(xp)+' health:' + str(pHealth))

    elif b == 'dun3':
        print (dun3map)
        print (str(story) + ' -- xp:'+ str(xp)+' health:' + str(pHealth))

    elif b == 'dun4':
        print (dun4map)
        print (str(story) + ' -- xp:'+ str(xp)+' health:' + str(pHealth))
    elif b == 'dun5':
        print (dun5map)
        print (str(story) + ' -- xp:'+ str(xp)+' health:' + str(pHealth))
    elif b == 'dun6':
        print (dun6map)
        print (str(story) + ' -- xp:'+ str(xp)+' health:' + str(pHealth))
    elif b == 'dun7':
        print (dun7map)
        print (str(story) + ' -- xp:'+ str(xp)+' health:' + str(pHealth))
    elif b == 'dun8':
        print (str(dun8map))
        print (str(story) + ' -- xp:'+ str(xp)+' health:' + str(pHealth))
        

    elif b == 'dun9':
        print (str(dun9map))
        print (str(story) + ' -- xp:'+ str(xp)+' health:' + str(pHealth))

    elif b == 'dun10':
        print (dun10map)
        print (str(story) + ' -- xp:'+ str(xp)+' health:' + str(pHealth))

    elif b == 'dun11':
        print (dun11map)
        print (str(story) + ' -- xp:'+ str(xp)+' health:' + str(pHealth))
    elif b == 'dun12':
        print (dun12map)
        print (str(story) + ' -- xp:'+ str(xp)+' health:' + str(pHealth))
    elif b == 'dun13':
        print (dun13map)
        print (str(story) + ' -- xp:'+ str(xp)+' health:' + str(pHealth))
    elif b == 'dun14':
        print (dun14map)
        print (str(story) + ' -- xp:'+ str(xp)+' health:' + str(pHealth))
    elif b == 'dun15':
        print (dun15map)
        print (str(story) + ' -- xp:'+ str(xp)+' health:' + str(pHealth))
        
        

    else:
        print('Map error, please load the last save. But I never made a save function (i did lol), so u gonna have to fix dat maps.txt file!(or use debug, but that should have been removed by now .) ')



def saveGame(a,b,c,d,e,f):
    global needKey
    global lvl
    global xp
    global pHealth
    global eStr
    global item1
    global item2
    global item3
    global item4
    with open(dpath,'w+') as data:
        data.write('lvl = '+str(lvl) + '''
''')
        data.write('xp = '+str(xp) + '''
''')
        data.write('pHealth = '+str(pHealth) + '''
''')
        data.write('item1 = '+str(item1) + '''
''')
        data.write('item2 = '+str(item2) + '''
''')
        data.write('item3 = '+str(item3) + '''
''')
        data.write('item4 = '+str(item4) + '''
''')
        data.write('needKey = '+str(needKey) + '''
''')
        data.write('eStr = '+str(eStr) + '''
''')
    print('Game saved!')
        #lvl = data.read()
    
    
    #print('Your savegm String is: '+ str(a)+str(b)+str(c)+str(d)+str(e),str(f),str(pHealth))
    #while True:
        #print('Oh look, you found the abandoned save/load function!')


def loadGame():
    a = input('Enter savegm String')
    global lvl
    global xp
    global pHealth
    while True:
        print('Oh look, you found the abandoned load function! If only there was a way to use it...                                                                                                                                                                                                                                          mocmordeo -- anagram')
    return a
    


def getLoc(loc):
    if lvl == 1:
        
        l = 'E1M1'

    elif lvl == 2:
        l = 'dun1'

    elif lvl == 3:
        l = 'dun2'
    elif lvl == 4:
        l= 'dun3'
    elif lvl == 5:
        l= 'dun4'
    elif lvl == 6:
        l= 'dun5'
    elif lvl == 7:
        l= 'dun6'
    elif lvl == 8:
        l= 'dun7'
    elif lvl == 9:
        l = 'dun8'

    elif lvl == 10:
        l = 'dun9'
    elif lvl == 11:
        l= 'dun10'
    elif lvl == 12:
        l= 'dun11'
    elif lvl == 13:
        l= 'dun12'
    elif lvl == 14:
        l= 'dun13'
    elif lvl == 15:
        l= 'dun14'
    elif lvl == 16:
        l= 'dun15'


    else:
        l = 'invalid_lvl'

    return l




def getStory(m):
    if m == 'E1M1':
        a = e1m1story
    elif m == 'dun1':
        a = dun1story
    elif m == 'dun2':
        a = dun2story
    elif m == 'dun3':
        a = dun3story
    elif m == 'dun4':
        a = dun4story
    elif m == 'dun5':
        a = dun5story
    elif m == 'dun6':
        a = dun6story
    elif m == 'dun7':
        a = dun7story
    elif m == 'dun8':
        a = dun8story
    elif m == 'dun9':
        a = dun9story
    elif m == 'dun10':
        a = dun10story
    elif m == 'dun11':
        a = dun11story
    elif m == 'dun12':
        a = dun12story
    elif m == 'dun13':
        a = dun13story
    elif m == 'dun14':
        a = dun14story
    elif m == 'dun15':
        a = dun15story
    else:
        a = 'story_msg_error'
    return a



    

def enmyEnc(n):
    k = random.randint(0,1)
    x = random.randint(1,5)
    global pHealth
    global needKey
    global eStr
    if x == 1:
        
        print('ENEMY('+n+') ENCOUNTERED!')
        print (ePic)
        win=random.randint(3,6) + eStr
        #timer=random.randint(3,7)
        while True:
            print('Enemy health: '+str(round(win,1)))
            print('You can use your sword or your bow (or run)')
            ct = input('What do you do? ')
            act = ct.lower()
            
            

            if 'sword' in act:
                print('You attack!')
                time.sleep(random.uniform(0.3,1.6))
                print('Enemy('+n+') attacks!')
                win=win-3
                atcc = random.randint(2,4)+ eStr-1.2
                pHealth=pHealth-round(atcc, 0) #timer=timer-1
                print('Health: '+str(pHealth))
                #print(win)

                
                if pHealth <= 0:#timer == 0:
                    print('The Enemy lands a mortal blow, knocking you to the ground.  Try as you might, you cannot recover and you take your last breath.  Better luck next time!')
                    return 0
                if round(win,0) <= 0:#eHealth:
                    print('You won!')
                    x = random.randint(4,6)+ round(eStr, 1)
                    h = random.randint(4,6)

                    print('You gained '+str(h)+' health!')
                    print('You gained '+str(x)+' xp!')
                    eStr = eStr + random.uniform(0.4,0.6)
                    pHealth = pHealth + h
                    if k == 1 and needKey == 1:
                        print('You got a key!')
                        needKey = 0
                              
                    return x
            elif 'bow' in act:
                    print('You attack!')
                    time.sleep(random.uniform(0.3,1.6))
                    print('Enemy('+n+') attacks!')
                    win=win-2.4
                    atcc = random.randint(1,3)+ eStr-1.2
                    pHealth=pHealth-round(atcc, 0)#timer=timer-1
                    print('Health: '+str(pHealth))
                    
                    #print(win)

            
                    if pHealth <= 0:#timer == 0:
                        print('The Enemy lands a mortal blow, knocking you to the ground.  Try as you might, you cannot recover and you take your last breath.  Better luck next time!')
                        return 0
                    if round(win,0) <= 0:#eHealth:
                        print('You won!')
                        x = random.randint(4,6)+ round(eStr, 1)
                        h = random.randint(4,6)

                        print('You gained '+str(h)+' health!')
                        print('You gained '+str(x)+' xp!')

                        pHealth = pHealth + h
                        eStr = eStr + random.uniform(0.4,0.6)
                        if k == 1 and needKey == 1:
                            print('You got a key!')
                            needKey = 0
                        return x
                

            elif 'run' in act:
                
                return 0
    else:
        return 0

def openInventory():
    global item1
    global item2
    global item3
    global item4
    #x = 'You have:' + hPotion ' Health potions' + sPotion ' Strength potions ' + key ' Keys' + coins ' Coins '
    print('''You have:
''' + str(item1) +' '+ item1Name + '''s
''' + str(item2) +' '+ item2Name)
    #+ str(item3) +' '+ item3Name + '''s

    #+ str(item4)+ ' '+ item4Name +'s '


def commBasic():
    global stayInmainLoop
    stayInmainLoop = 0
    print('OMG WOW HOW DID YOU FIND THIS?!?!?!')
    print('''
               *******      COMMODORE 64 BASIC V2      *******
''')
    while True:
         x = input('READY.')
         print('?SYNTAX ERROR')
        
        

    


b = ''


plyrShortAct = 'Null'
xp = 0
eStr = 0.344
xpx = 0
pHealth = 25
eName='?'
needKey = 2 
path = r'maps.txt'
dpath = r'gamedata.gcfg'
print('This game is made with LightRPG-creator v4 (modded)')
print('Reading game data...')
time.sleep(random.randint(1,3))
#with open(dpath,'w+') as data:
 #   data.write('')



#gamedatainfo = ''.join(random.choices(string.ascii_letters + string.digits, k=56))
try:
    with open(dpath,'r') as data:
        #data.write(gamedatainfo)
        gdat = data.read()
except FileNotFoundError:
        with open(dpath,'w+') as data:
            data.write('lvl = '+str(lvl) + '''
''')
            data.write('xp = '+str(xp) + '''
''')
            data.write('pHealth = '+str(pHealth) + '''
''')
            data.write('item1 = '+str(item1) + '''
''')
            data.write('item2 = '+str(item2) + '''
''')
            data.write('item3 = '+str(item3) + '''
''')
            data.write('item4 = '+str(item4) + '''
''')
            data.write('needKey = '+str(needKey) + '''
''')
            data.write('eStr = '+str(eStr) + '''
''')

except:    
    print('Save corrupt :(')
    with open(dpath,'w+') as data:
        data.write('lvl = '+str(lvl) + '''
''')
        data.write('xp = '+str(xp) + '''
''')
        data.write('pHealth = '+str(pHealth) + '''
''')
        data.write('item1 = '+str(item1) + '''
''')
        data.write('item2 = '+str(item2) + '''
''')
        data.write('item3 = '+str(item3) + '''
''')
        data.write('item4 = '+str(item4) + '''
''')
        data.write('needKey = '+str(needKey) + '''
''')
        data.write('eStr = '+str(eStr) + '''
''')
with open(dpath,'r') as data:
    #data.write(gamedatainfo)
    gdat = data.read()
try:
    exec(gdat)
except:
    print('Save corrupt :(')
    with open(dpath,'w+') as data:
        data.write('lvl = '+str(lvl) + '''
''')
        data.write('xp = '+str(xp) + '''
''')
        data.write('pHealth = '+str(pHealth) + '''
''')
        data.write('item1 = '+str(item1) + '''
''')
        data.write('item2 = '+str(item2) + '''
''')
        data.write('item3 = '+str(item3) + '''
''')
        data.write('item4 = '+str(item4) + '''
''')
        data.write('needKey = '+str(needKey) + '''
''')
        data.write('eStr = '+str(eStr) + '''
''')
with open(dpath,'r') as data:
    #data.write(gamedatainfo)
    gdat = data.read()
exec(gdat)


print('Reading mapfile data...')
time.sleep(random.randint(1,3))
time.sleep(random.randint(1,3))
try:    

    with open(path,'r') as maps:
        maptbl = maps.read()
except FileNotFoundError:
        with open(path,'a+') as maps:
            maps.write(mapvartxt)
with open(path,'r') as maps:
    maptbl = maps.read()      
#print(maptbl)
try:
    exec(maptbl)
except:
    frmt = input('Error when reading map file, do you want to format the file?(y/n)')
    if frmt == 'y':
        time.sleep(2.4)
        with open(path,'w+') as maps:
                maps.write(mapvartxt)
        print('Format complete!')
    else:
        print('Ok, please fix the map file.')
with open(path,'r') as maps:
    maptbl = maps.read()
    
print('Starting game...')
time.sleep(random.randint(3,6))













exec(maptbl)


try:
    print(story)   
except:
    frmt = input('Error when reading map file, do you want to format the file?(y/n)')
    if frmt == 'y':
        time.sleep(2.4)
        with open(path,'w+') as maps:
            maps.write(mapvartxt)
        with open(path,'r') as maps:
            maptbl = maps.read()
            exec(maptbl)
        print('Format complete!')
        time.sleep(2.4)
        print(story)   

            
input()







while stayInmainLoop == 1 :


    if pHealth <= 0:
        print('You died. Press enter to close.')
        input()
        exit()
        




    

    
    
    currentLoc = getLoc(lvl)
    try:
        EoG()
    except:
        frmt = input('Error when reading map file, do you want to format the file?(y/n)')
        if frmt == 'y':
            time.sleep(2.4)
            with open(path,'w+') as maps:
                    maps.write(mapvartxt)
            with open(path,'r') as maps:
                    maptbl = maps.read()
                    exec(maptbl)
            print('Format complete!')
            EoG()
    if gend == 1:
        print(endstory)
        with open(dpath,'w+') as data:
            data.write('')
        input()
        exit()
        

    

    try:
        story = getStory(currentLoc)
    except:
        frmt = input('Error when reading map file, do you want to format the file?(y/n)')
        if frmt == 'y':
            time.sleep(2.4)
            with open(path,'w+') as maps:
                    maps.write(mapvartxt)
            with open(path,'r') as maps:
                    maptbl = maps.read()
                    exec(maptbl)
            print('Format complete!')
            story = getStory(currentLoc)
        
        else:
            print('Ok, please fix the map file.')
    try:
        showMap(currentLoc,story,lvl,xp)

    except:
        frmt = input('Error when reading map file, do you want to format the file?(y/n)')
        if frmt == 'y':
            time.sleep(2.4)
            with open(path,'w+') as maps:
                    maps.write(mapvartxt)
            with open(path,'r') as maps:
                    maptbl = maps.read()
                    exec(maptbl)
            print('Format complete!')
            showMap(currentLoc,story,lvl,xp)
        
        else:
            print('Ok, please fix the map file.')
    
    
    #print('You can: go up, go down, move left, move right, save the game. ')
    #print('Note: all commands are in lowercase.')
    plyrInput = getCmd (b)
    plyrShortAct = plyrAction(plyrInput,story,lvl,currentLoc,b,plyrShortAct,xp)
    if plyrShortAct == 'dbg':
        try:
            dbugStr = input('>>>')
            exec(dbugStr)
        except NameError:
            print('Thats an oops!')
        except SyntaxError:
            print('Thats an oops!')
    else:
        lvl = moveHandlr(plyrShortAct,lvl)
    xpx = enmyEnc(eName)
    xp = xp + xpx

    if needKey == 0:
        item3 = 1
    else:
        item3 = 0
