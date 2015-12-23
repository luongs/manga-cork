import logging
import os

from mangacork import db
from mangacork.models import LastPage

logger = logging.getLogger(__name__)

def make_chapter_files():
    os.chdir('../mangacork/static/images')

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
            write_last_page_to_file(files[-1], filename)
            write_last_page_to_db(files[-1])


def get_filepath(directory):
    filepath = '{}.txt'.format(directory)
    return filepath


def make_file(filepath):
    f = open(filepath, 'a')
    f.close()


def write_last_page_to_file(page_w_ext, filename):
    f = open(filename, 'w')
    page, _ = page_w_ext.split('.')
    f.write(page)
    f.close()


def write_last_page_to_db(page_w_ext):
    page, _ = page_w_ext.split('.')
    table_value = LastPage(page)
    # Do not add if value already exists in db
    if not LastPage.query.filter_by(lastpage=table_value.lastpage).count():
        db.session.add(table_value)
        db.session.commit()


if __name__ == '__main__':
    make_chapter_files()
    write_chapter_files()
