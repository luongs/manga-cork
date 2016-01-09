import logging

from flask import render_template, request, redirect, session, url_for
from flask.ext.login import (login_user, logout_user)


from . import app, db, login_manager
from .utils import (increment_page_number, build_img_path, is_last_page)
from .models import LastPage, Comments, User
from .forms import SignupForm, LoginForm

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

INDEX_CHAPTER = 'dragonball_ch1'
INDEX_PAGE = 'ndragon_ball_v001-000'
LAST_PAGE_LIST = [i.lastpage for i in LastPage.query.all()]
logger.debug('Last Page List {}'.format(LAST_PAGE_LIST))


@app.route('/')
def index():
    return redirect(url_for('display',chapter=INDEX_CHAPTER, page=INDEX_PAGE))


@app.route('/<chapter>/<page>', methods=['GET','POST'])
def display(chapter, page):
    login_form = LoginForm()
    signup_form = SignupForm()
    login_error = request.args.get('login_error')
    signup_error = request.args.get('signup_error')
    login_error_buffer = request.args.get('login_error_buffer')
    signup_error_buffer = request.args.get('signup_error_buffer')

    image_path = build_img_path(chapter, page)
    next_page_number = increment_page_number(page)
    comments = Comments.query.order_by(Comments.id.desc()).filter_by(
                image_path=image_path).all()

    if (is_last_page(page, LAST_PAGE_LIST)):
        next_page = '/last_page'
    else:
        next_page = build_img_path(chapter, next_page_number)

    return render_template('manga.html',
                            login_form=login_form,login_error=login_error,
                            login_error_buffer=login_error_buffer,
                            signup_form=signup_form, signup_error=signup_error,
                            signup_error_buffer=signup_error_buffer,
                            next_page=next_page,page=page,chapter=chapter,
                            comments=comments, session=session)


@app.route('/login', methods=['GET','POST'])
def login():
    login_form = LoginForm()
    chapter = request.form['chapter']
    page = request.form['page']
    login_error = None
    login_error_buffer = None

    if login_form.validate_on_submit():
        user = User.query.filter_by(username=login_form.username.data).first()

        if user is None:
            login_error = True
            login_error_buffer = "Username does not exist"
        elif user.is_correct_password(plaintext=login_form.password.data):
            login_user(user)
            session['username'] = user.username
        else:
            login_error=True
            login_error_buffer = "Incorrect password"

    else:      # Missing values in login form
        login_error = True
        for _, error_messages in login_form.errors.iteritems():
            # print out first error message only
            login_error_buffer= error_messages[0]
            break

    return redirect(url_for('display', chapter=chapter, page=page,
                            login_error=login_error,
                            login_error_buffer=login_error_buffer))


@app.route('/signup', methods=['POST'])
def signup():
    signup_form = SignupForm()
    chapter = request.form['chapter']
    page = request.form['page']

    if signup_form.validate_on_submit():
        user = User(username=signup_form.username.data,
                    plaintext=signup_form.password.data,
                    email=signup_form.email.data)
        db.session.add(user)
        db.session.commit()
        login_user(user)
        session['username'] = user.username

        return redirect(url_for('display', chapter=chapter, page=page))
    else:
        signup_error = True
        for _, error_messages in signup_form.errors.iteritems():
            # print out first error message only
            signup_error_buffer= error_messages[0]
            break
        # Reloads page with signup modal opened
        return redirect(url_for('display', chapter=chapter, page=page,
                                signup_error=signup_error,
                                signup_error_buffer=signup_error_buffer))


@app.route('/signout')
def signout():
    session.clear()
    logout_user()
    return redirect(url_for('index'))


@app.route('/add', methods= ['POST'])
def add_entry():
    chapter = request.form['chapter']
    page = request.form['page']
    comment = request.form['post_text']
    image_path = build_img_path(chapter, page)
    if 'username' not in session:
        # Require login to post entry
        return redirect(url_for('display', chapter=chapter, page=page,
                            login_error=True))

    username = session.get('username')
    new_comment = Comments(comment, image_path, username)
    db.session.add(new_comment)
    db.session.commit()

    return redirect(url_for('display', chapter=chapter, page=page ))

@app.route('/last_page')
def display_lastpage():
    login_form = LoginForm()
    return render_template('lastpage.html',login_form=login_form)
