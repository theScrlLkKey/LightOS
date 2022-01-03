def mainloop():
    timup.start()
    time.sleep(0.1)
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
                console_log('done running ' + usrsel)
        except:
            pass