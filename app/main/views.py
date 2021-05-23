from flask import Blueprint, render_template, redirect, flash, url_for, request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required
from app.main.forms import SignUpForm, SignInForm
from app.models import User

main = Blueprint('main', __name__, template_folder='templates')


@main.route('/', methods=['GET'])
def homepage():
    signin_form = SignInForm()
    signup_form = SignUpForm()
    return render_template('main/index.html', signin_form=signin_form, signup_form=signup_form)


@main.route('/signup', methods=['POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()
        print(user)

        # Check if user already exists
        if user:
            print('User exits')
            flash('User already exists')
            return redirect(url_for('main.homepage'))

        new_user = User(email=email, username=username,
                        password=generate_password_hash(password, method='sha256'))

        new_user.create()
        return {
            'message': 'SUCCESS'
        }
    return redirect(url_for('main.homepage'))


@main.route('/', methods=['POST'])
def signin():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()
        # Check if user exists and correct password
        if not user or not check_password_hash(user.password, password):
            print('Please check your login details and try again.')
            return redirect(url_for('main.homepage'))

        # Login user
        login_user(user, remember=False)

        # Redirect admin to admin page
        if user.username == 'admin':
            return redirect('/admin')

        return redirect(url_for('user.dashboard'))


@login_required
@main.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.homepage'))
