from app.common.algorithms import match_traits
from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from werkzeug.utils import redirect
from app.user.forms import ProfileForm
from app.exts import db
from app.common.service import get_one_query
# from app.common.traits import db_traits, traits_questions
# from app.common.algorithms import trait_obj_to_list
from app.models import UserTrait, RoomieTrait, Hostel

user_bp = Blueprint('user_bp', __name__, template_folder='templates')


@user_bp.route('/dashboard', methods=['GET'])
@login_required
def dashboard():
    if not get_one_query(UserTrait, current_user.id):
        flash('Please Pick your traits', 'error')
    return render_template('user/dashboard.html', user=current_user)


@user_bp.route('/settings', methods=['POST', 'GET'])
@login_required
def settings():
    if request.method == 'POST':
        name = request.form['name']
        address = request.form['address']
        school = request.form['school']
        email = request.form['email']
        number = request.form['number']

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

        db.session.commit()

        return redirect(url_for('user_bp.profile'))

    return render_template('user/settings.html', user=current_user, form=ProfileForm())


@user_bp.route('/profile', methods=['POST', 'GET'])
@login_required
def profile():
    return render_template('user/profile.html', user=current_user)


@user_bp.route('/traits', methods=['POST', 'GET'])
@login_required
def traits():
    traits = get_one_query(UserTrait, current_user.id)
    return render_template('user/traits.html', user=current_user, traits=traits)
# traits=db_traits, traits_questions=traits_questions,
#                            user=current_user, user_trait=trait_obj_to_list(user_trait), roomie_trait=trait_obj_to_list(roomie_trait)
