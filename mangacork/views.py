from flask import render_template, request, url_for

from mangacork import app


@app.route('/')
def hello_world():
    return 'Hello world'
