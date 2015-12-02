import os


def make_chapter_files():
    os.chdir('../static/images')

    for _, dirs, files in os.walk(os.getcwd()):

        dirs = [d for d in dirs if not d[0] == '.']
        files = [f for f in files if not f[0] == '.']

        for directory in dirs:
            file_path = get_filepath(directory)
            make_file(file_path)


def write_chapter_files():
    os.chdir('../static/images')

    root, chapters, files = next(os.walk(os.getcwd()))
    for chapter in chapters:
        path_list.append(os.path.join(root, chapter))
    path_list = [p for p in chapters]
    chapter_list = [name for name in files if not name[0] == '.']
    print path_list
    # print chapter_list


def get_filepath(directory):
    filepath = '{}.txt'.format(directory)
    return filepath


def make_file(filepath):
    f = open(filepath, 'a')
    f.close()

if __name__ == '__main__':
    # make_chapter_files()
    write_chapter_files()
