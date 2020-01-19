from recursion import get_dirlist as gd
import os


def print_files(path=os.getcwd()):

    dirlist = gd(path)
    for f in dirlist:
        fullname = os.path.join(path, f)   # Turn name into full pathname
        if os.path.isdir(fullname):        # If a directory, recurse.
            newfile = open(fullname + '/' + 'trash.txt', 'w')
            newfile.write('This is trash')
            newfile.close()
            print('Created file in {0}'.format(fullname))
            print_files(fullname)


# print_files('/Users/sadeliyi/Documents/Media')
