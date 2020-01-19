from litter import gd
import os


def print_files(path=os.getcwd()):
    target = 'trash.txt'
    dirlist = gd(path)
    for f in dirlist:
        fullname = os.path.join(path, f) # Turn name into full pathname
        if os.path.isdir(fullname):        # If a directory, recurse.
            print_files(fullname)
        else:
            if f == target:
                os.remove(fullname)
                print("file removed")


print_files('/Users/sadeliyi/Documents/Media')