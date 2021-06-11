from flask import Blueprint, render_template, redirect, flash, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required
from app.main.forms import SignUpForm, SignInForm
from app.models import User

main = Blueprint('main', __name__, template_folder='templates')


signinmode = 'false'


@main.route('/', methods=['GET'])
def homepage():
    sign = signinmode
    signin_form = SignInForm()
    signup_form = SignUpForm()
    return render_template('main/index.html', signin_form=signin_form, signup_form=signup_form,  signinmode=signinmode)


@main.route('/signup', methods=['POST'])
def signup():

    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()

        if user:
            flash(u'Username already exists', 'error')
            return redirect(url_for('main.homepage'))

        new_user = User(email=email, username=username,
                        password=generate_password_hash(password, method='sha256'))

        new_user.create()
        flash('Sign-up successful. Please Sign-in.', 'success')
        global signinmode
        signinmode = 'true'
        return redirect(url_for('main.homepage'))

    return redirect(url_for('main.homepage'),)


@main.route('/', methods=['POST'])
def signin():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()
        # Check if user exists and correct password
        if not user or not check_password_hash(user.password, password):
            flash(u'Invalid Username or password provided', 'error')
            return redirect(url_for('main.homepage'))

        # Login user
        login_user(user, remember=False)

        # Redirect admin to admin page
        if user.username == 'admin':
            return redirect('/admin')

        return redirect(url_for('user_bp.traits'))


@login_required
@main.route('/logout')
def logout():
    global signinmode
    signinmode = 'true'
    logout_user()
    return redirect(url_for('main.homepage'))
