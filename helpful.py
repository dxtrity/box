def help_start():
    print('''
#########################
#       Box Help        #
#########################

Box is a package manager created in Python.
This is a static help page that has all of the needed information about Box.
''')

def help_pack(): 
    print('''
#########################
#       Box Pack        #
#########################

Use "box pack <file>" to create and add your file to your box package.
''')

def help_ship(): 
    print('''
#########################
#       Box Ship        #
#########################

Use "box ship <file> <target>" to ship your box package to a directory.
''')

def help_install(): 
    print('''
#################################
#          Box Install          #
#################################

Use "box install <file>" to install a package from a directory.
''')

def help_query():
    print('''
##########################
#       Box Query        #
##########################

Use "box query <file>" to get information on a file.
''')


def help_cmd():
    help_start()
    help_pack()
    help_ship()
    help_install()
    help_query()