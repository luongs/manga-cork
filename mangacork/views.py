from flask import render_template

from mangacork import app

INDEX_IMAGE_PATH = 'dragonball_ch1/ndragon_ball_v001-000.jpg'
FILE_TYPE = 'jpg'


@app.route('/')
def index():
    return render_template('manga.html', image_path=INDEX_IMAGE_PATH)


@app.route('/<chapter>/<page>')
def display(chapter, page):
    image_path = '{}/{}.{}'.format(
        chapter, page, FILE_TYPE)
    return render_template('manga.html', image_path=image_path)
