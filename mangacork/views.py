import logging

from flask import render_template

from . import app
from .utils import (increment_page_number, build_img_path, is_last_page)
from .models import LastPage

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

INDEX_CHAPTER = 'dragonball_ch1'
INDEX_PAGE = 'ndragon_ball_v001-000'
logger.info('Initialize LAST_PAGE_LIST from database')
LAST_PAGE_LIST = LastPage.query.all()
logger.debug('Last Page List {}'.format(LAST_PAGE_LIST))
for i in LAST_PAGE_LIST:
    logger.debug(i.lastpage)

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

    if (is_last_page(chapter, page)):
        next_page = '/last_page'
    else:
        next_page = build_img_path(chapter, next_page_number)

    return render_template('manga.html', next_page=next_page,
                           image_path=image_path)


@app.route('/last_page')
def display_lastpage():
    return render_template('lastpage.html')
