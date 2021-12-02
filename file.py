import os

def just_the_file(file):
        with open(file, "r") as f:
            filename = str(os.path.basename(f.name))
            return filename

def get_filetype(file):
    with open(file, "r") as f:
        filename = os.path.basename(f.name).split(".")
        filetype = str(filename[1])
        return filetype

def get_dirname(file):
    with open(file, "r") as f:
        filename = os.path.basename(f.name).split(".")
        dirname = str(filename[0])
        return dirname

# Help Command

help_start = '''
#########################
#       Box Help        #
#########################

Box is a package manager created in Python.
This is a static help page that has all of the needed information about Box.
'''

help_pack = '''
#########################
#       Box Pack        #
#########################

Use "box pack <file>" to create and add your file to your box package.
'''

help_ship = '''
#########################
#       Box Ship        #
#########################

Use "box ship <file> <target>" to ship your box package to a directory.
'''

help_install = '''
#################################
#          Box Install          #
#################################

Use "box install <file>" to install a package from a directory.
'''

help_query = '''
##########################
#       Box Query        #
##########################

Use "box query <file>" to get information on a file.
'''

def help_cmd():
    print(help_start)
    print(help_pack)
    print(help_ship)
    print(help_install)
    print(help_query)