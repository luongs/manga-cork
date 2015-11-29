from flask import render_template

from . import app

INDEX_CHAPTER = 'dragonball_ch1'
INDEX_PAGE = 'ndragon_ball_v001-000'


def increment_page_number(page):
    page, page_number = page.split('-')
    # Add leading zeroes to keep expected page format
    page_number = str(int(page_number) + 1).zfill(3)
    next_page = '{page}-{page_number}'.format(
        page=page, page_number=page_number)

    return next_page


def build_img_path(chapter, page):
    return '{}/{}'.format(chapter, page)


@app.route('/')
def index():
    image_path = build_img_path(INDEX_CHAPTER, INDEX_PAGE)
    next_page_number = increment_page_number(INDEX_PAGE)
    next_page = build_img_path(INDEX_CHAPTER, next_page_number)

    return render_template('manga.html', next_page=next_page,
                           image_path=image_path)


@app.route('/<chapter>/<page>')
def display(chapter, page):
    image_path = build_img_path(chapter, page)
    next_page_number = increment_page_number(page)
    next_page = build_img_path(chapter, next_page_number)

    return render_template('manga.html', next_page=next_page,
                           image_path=image_path)
