
from flask import Blueprint, render_template, request, redirect, url_for, flash, current_app
from flask_login import login_required, current_user
from werkzeug.utils import redirect
from app.user.forms import ProfileForm
from app.exts import db
from app.common.service import get_one_query
import os
from app.models import User, UserTrait, RoomieTrait, Room
from app.common.traits import db_traits, traits_strings

user_bp = Blueprint('user_bp', __name__, template_folder='templates')


@user_bp.route('/dashboard', methods=['GET'])
@login_required
def dashboard():
    if not get_one_query(UserTrait, current_user.id):
        flash('Please Pick your traits', 'error')
    return render_template('user/dashboard.html', user=current_user)


@user_bp.route('/<id>', methods=['GET'])
@login_required
def user(id):
    user = get_one_query(User, id)
    user_traits = get_one_query(UserTrait, user.id)
    roomie_traits = get_one_query(RoomieTrait, user.id)

    user.traits = []
    user.roomie_traits = []
    if user_traits and roomie_traits:
        for trait in db_traits:
            if getattr(user_traits, trait):
                user.traits.append(traits_strings[trait])
            if getattr(roomie_traits, trait) == 'True':
                user.roomie_traits.append(traits_strings[trait])

    user.traits = sorted(user.traits, key=len)
    user.roomie_traits = sorted(user.roomie_traits, key=len)
    return render_template('user/one_user.html', user=current_user, thisuser=user)


@user_bp.route('/editProfile', methods=['POST', 'GET'])
@login_required
def settings():
    if request.method == 'POST':

        uploaded_file = request.files['photo']
        if uploaded_file.filename != '':
            uploaded_file.save(os.path.join(
                current_app.root_path, current_app.config['STATIC_FOLDER'], 'img', 'user_photos', f'{current_user.get_id()}.{uploaded_file.filename.split(".")[1]}'))
            current_user.photo_name = f'{current_user.get_id()}.{uploaded_file.filename.split(".")[1]}'

        name = request.form['name']
        address = request.form['address']
        school = request.form['school']
        email = request.form['email']
        number = request.form['number']
        gender = request.form['gender']
        about = request.form['about']

        if name:
            current_user.name = name
        if address:
            current_user.address = address
        if school:
            current_user.school = school
        if email:
            current_user.email = email
        if number:
            current_user.number = number
        if about:
            current_user.about = about
        if gender and gender != 'Gender':
            current_user.gender = gender

        db.session.commit()

        return redirect(url_for('user_bp.profile'))

    return render_template('user/edit_profile.html', user=current_user, form=ProfileForm())


@ user_bp.route('/profile', methods=['POST', 'GET'])
@ login_required
def profile():
    user_traits = get_one_query(UserTrait, current_user.id)
    roomie_traits = get_one_query(RoomieTrait, current_user.id)
    current_user.traits = []
    current_user.roomie_traits = []
    if user_traits and roomie_traits:
        for trait in db_traits:
            if getattr(user_traits, trait):
                current_user.traits.append(traits_strings[trait])
            if getattr(roomie_traits, trait) == 'True':
                current_user.roomie_traits.append(traits_strings[trait])

    current_user.traits = sorted(current_user.traits, key=len)
    current_user.roomie_traits = sorted(current_user.roomie_traits, key=len)
    return render_template('user/profile.html', user=current_user)


@ user_bp.route('/traits', methods=['POST', 'GET'])
@ login_required
def traits():
    traits = get_one_query(UserTrait, current_user.id)
    return render_template('user/traits.html', user=current_user, traits=traits)
