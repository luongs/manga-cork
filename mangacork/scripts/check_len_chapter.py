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
    root, chapters, files = next(os.walk(os.getcwd()))

    path_list = [os.path.join(root, chapter) for chapter in chapters]
    chapter_list = [name for name in files if not name[0] == '.']

    # match path to txt file
    zipped = zip(path_list, chapter_list)

    for path, filename in zipped:
        _, _, files = next(os.walk(path))

        if (len(files) > 0):
            write_last_page(files[-1], filename)


def get_filepath(directory):
    filepath = '{}.txt'.format(directory)
    return filepath


def make_file(filepath):
    f = open(filepath, 'a')
    f.close()


def write_last_page(page_w_ext, filename):
    f = open(filename, 'w')
    page, _ = page_w_ext.split('.')
    f.write(page)
    f.close()

if __name__ == '__main__':
    make_chapter_files()
    write_chapter_files()
