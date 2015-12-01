import os
from os.path import (isfile, walk)

filename = ''


def id_chapters():
    print(os.chdir('../static/images'))
    for root, dirs, files in os.walk(os.getcwd()):
        if len(dirs) > 0:
            filename = str(dirs[0])


def write_file():
    f = open(filename, 'w')
    f.write('hello world')
    f.close()

if __name__ == '__main__':
    id_chapters()
