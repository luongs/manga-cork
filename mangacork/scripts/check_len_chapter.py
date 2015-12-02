import os


def id_chapters():
    os.chdir('../static/images')

    for _, dirs, files in os.walk(os.getcwd()):

        dirs = [d for d in dirs if not d[0] == '.']
        files = [f for f in files if not f[0] == '.']

        for directory in dirs:
            file_path = get_filepath(directory)
            write_file(file_path)


def get_filepath(directory):
    filepath = '{}.txt'.format(directory)
    return filepath


def write_file(filepath):
    os.chdir('../chapters')
    f = open(filepath, 'a')
    f.close()
    os.chdir('../images')

if __name__ == '__main__':
    id_chapters()
