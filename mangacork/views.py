import logging

from flask import render_template, request, redirect, url_for

from . import app, db
from .utils import (increment_page_number, build_img_path, is_last_page)
from .models import LastPage, Comments

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

INDEX_CHAPTER = 'dragonball_ch1'
INDEX_PAGE = 'ndragon_ball_v001-000'
LAST_PAGE_LIST = [i.lastpage for i in LastPage.query.all()]
logger.debug('Last Page List {}'.format(LAST_PAGE_LIST))


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
    comments = Comments.query.order_by(Comments.id.desc()).filter_by(
                image_path=image_path).all()

    if (is_last_page(page, LAST_PAGE_LIST)):
        next_page = '/last_page'
    else:
        next_page = build_img_path(chapter, next_page_number)

    return render_template('manga.html', next_page=next_page,
                           image_path=image_path, comments=comments)


@app.route('/add', methods= ['POST'])
def add_entry():
    image_path = request.form['image_path']
    comment = request.form['post_text']
    _, chapter, page  = image_path.split('/')

    new_comment = Comments(comment, image_path)
    db.session.add(new_comment)
    db.session.commit()

    return redirect(url_for('display', chapter=chapter, page=page ))

@app.route('/last_page')
def display_lastpage():
    return render_template('lastpage.html')
