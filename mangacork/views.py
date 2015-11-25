from flask import render_template

from mangacork import app


@app.route('/')
def index():
    return render_template('manga.html')
