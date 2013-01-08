import SimpleOptparse

if __name__ == '__main__':
    # define the options we want to catch on the commandline
    # Format:
    #     ((long_option,short_option), a short helpline for this option): default value
    #
    optDef = {  
                (('--help',     '-h')       ,"This help"):                                False,
                (('--verbose',  '-v')       ,"Enable verbose output"):                    False,
                (('--timeout',  '-t')       ,"Timeout for the console to stay open"):         5,
                (('--branch',   '-b')       ,"use specific branch   "):                   '1.1',
                (('--magic' ,   '-m')       ,"insert random magic values here"):           None,
                (('--deluxe',   '-d')       ,"Deluxe Option cost more than a million"):   False,
                (('--cant-afford','-c')     ,"sure you cant! ha ha ha"):                  False,    
                (('--manD',     '1')        ,"This is a mandatory option!"):              SimpleOptparse.MANDATORY,     
              }
    # do the magic
    options,arguments= SimpleOptparse.parseOpts(optDef)
    # if no option was hit it will print the usage/help & exit
    # if options were hit, it returns a tuple in the following format:
    #
    # ( {dictionary of all parsed options}, [a list of optional arguments])
    print options
    print arguments