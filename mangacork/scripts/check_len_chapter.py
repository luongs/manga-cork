import os
from os.path import (isfile, walk)


def id_chapters():
    os.chdir('../static/images')

    for _, dirs, files in os.walk(os.getcwd()):

        dirs = [d for d in dirs if not d[0] == '.']
        files = [f for f in files if not f[0] == '.']

        res_file_path = ''
        for directory in dirs:
            res_file_path = get_filepath(directory)

        # print res_file_path
        for filename in files:
            print(res_file_path)
            write_file(res_file_path, filename)


def get_filepath(directory):
    filepath = '{}.txt'.format(directory)
    return filepath


def write_file(filepath, data):
    print(filepath)
    f = open(filepath, 'a')
    f.write(data)
    f.close()

if __name__ == '__main__':
    id_chapters()
