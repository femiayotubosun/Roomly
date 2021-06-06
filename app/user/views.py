from app.common.algorithms import match_traits, sort_rooms_by_match
from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from werkzeug.utils import redirect
from app.user.forms import ProfileForm
from app.exts import db
from app.common.service import get_one_query
from app.common.traits import db_traits, traits_questions
from app.common.algorithms import trait_obj_to_list
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

    user_trait = UserTrait.query.filter_by(
        user_id=current_user.id).first()
    if user_trait:
        ut_exists = True
    else:
        ut_exists = False

    roomie_trait = RoomieTrait.query.filter_by(
        user_id=current_user.id).first()
    if roomie_trait:
        rt_exists = True
    else:
        rt_exists = False

    if request.method == 'POST':

        if not ut_exists:
            user_trait = UserTrait(user_id=current_user.id)

        user_neat = request.form['user-neat']
        user_quiet = request.form['user-quiet']
        user_visitors = request.form['user-visitors']
        user_smoker = request.form['user-smoker']
        user_drinker = request.form['user-drinker']
        user_earlybird = request.form['user-earlybird']
        user_nightcrawler = request.form['user-nightcrawler']
        user_snores = request.form['user-snores']
        user_sharethings = request.form['user-sharethings']
        user_studyinroom = request.form['user-studyinroom']
        user_music = request.form['user-music']

        if user_neat:
            if user_neat == 'True':
                user_trait.neat = True
            else:
                user_trait.neat = False
        else:
            if user_trait.neat == True or user_trait.neat == False:
                pass
            else:
                user_trait.neat = False

        if user_quiet:
            if user_quiet == 'True':
                user_trait.quiet = True
            else:
                user_trait.quiet = False
        else:
            if user_trait.neat == True or user_trait.neat == False:
                pass
            else:
                user_trait.quiet = False

        if user_visitors:
            if user_visitors == 'True':
                user_trait.visitors = True
            else:
                user_trait.visitors = False
        else:
            if user_trait.neat == True or user_trait.neat == False:
                pass
            else:
                user_trait.visitors = False

        if user_smoker:
            if user_smoker == 'True':
                user_trait.smoker = True
            else:
                user_trait.smoker = False
        else:
            if user_trait.neat == True or user_trait.neat == False:
                pass
            else:
                user_trait.smoker = False

        if user_drinker:
            if user_drinker == 'True':
                user_trait.drinker = True
            else:
                user_trait.drinker = False
        else:
            if user_trait.neat == True or user_trait.neat == False:
                pass
            else:
                user_trait.drinker = False

        if user_earlybird:
            if user_earlybird == 'True':
                user_trait.earlybird = True
            else:
                user_trait.earlybird = False
        else:
            if user_trait.neat == True or user_trait.neat == False:
                pass
            else:
                user_trait.earlybird = False

        if user_nightcrawler:
            if user_nightcrawler == 'True':
                user_trait.nightcrawler = True
            else:
                user_trait.nightcrawler = False
        else:
            if user_trait.neat == True or user_trait.neat == False:
                pass
            else:
                user_trait.nightcrawler = False

        if user_snores:
            if user_snores == 'True':
                user_trait.snores = True
            else:
                user_trait.snores = False
        else:
            if user_trait.neat == True or user_trait.neat == False:
                pass
            else:
                user_trait.snores = False

        if user_sharethings:
            if user_sharethings == 'True':
                user_trait.sharethings = True
            else:
                user_trait.sharethings = False
        else:
            if user_trait.neat == True or user_trait.neat == False:
                pass
            else:
                user_trait.sharethings = False

        if user_studyinroom:
            if user_studyinroom == 'True':
                user_trait.studyinroom = True
            else:
                user_trait.studyinroom = False
        else:
            if user_trait.neat == True or user_trait.neat == False:
                pass
            else:
                user_trait.studyinroom = False

        if user_music:
            if user_music == 'True':
                user_trait.music = True
            else:
                user_trait.music = False
        else:
            if user_trait.neat == True or user_trait.neat == False:
                pass
            else:
                user_trait.music = False

        if ut_exists:
            db.session.commit()
        else:
            user_trait.create()

        # Initialize all roomie triats into vars
        if not rt_exists:
            roomie_trait = RoomieTrait(user_id=current_user.id)

        roomie_neat = request.form['roomie-neat']
        roomie_quiet = request.form['roomie-quiet']
        roomie_visitors = request.form['roomie-visitors']
        roomie_smoker = request.form['roomie-smoker']
        roomie_drinker = request.form['roomie-drinker']
        roomie_earlybird = request.form['roomie-earlybird']
        roomie_nightcrawler = request.form['roomie-nightcrawler']
        roomie_snores = request.form['roomie-snores']
        roomie_sharethings = request.form['roomie-sharethings']
        roomie_studyinroom = request.form['roomie-studyinroom']
        roomie_music = request.form['roomie-music']

        if roomie_neat:
            if roomie_neat == 'True':
                roomie_trait.neat = True
            else:
                roomie_trait.neat = False
        else:
            roomie_trait.neat = False

        if roomie_quiet:
            if roomie_quiet == 'True':
                roomie_trait.quiet = True
            else:
                roomie_trait.quiet = False
        else:
            roomie_trait.quiet = False

        if roomie_visitors:
            if roomie_visitors == 'True':
                roomie_trait.visitors = True
            else:
                roomie_trait.visitors = False
        else:
            roomie_trait.visitors = False

        if roomie_smoker:
            if roomie_smoker == 'True':
                roomie_trait.smoker = True
            else:
                roomie_trait.smoker = False
        else:
            roomie_trait.smoker = False

        if roomie_drinker:
            if roomie_drinker == 'True':
                roomie_trait.drinker = True
            else:
                roomie_trait.drinker = False
        else:
            roomie_trait.drinker = False

        if roomie_earlybird:
            if roomie_earlybird == 'True':
                roomie_trait.earlybird = True
            else:
                roomie_trait.earlybird = False
        else:
            roomie_trait.earlybird = False

        if roomie_nightcrawler:
            if roomie_nightcrawler == 'True':
                roomie_trait.nightcrawler = True
            else:
                roomie_trait.nightcrawler = False
        else:
            roomie_trait.nightcrawler = False

        if roomie_snores:
            if roomie_snores == 'True':
                roomie_trait.snores = True
            else:
                roomie_trait.snores = False
        else:
            roomie_trait.snores = False

        if roomie_sharethings:
            if roomie_sharethings == 'True':
                roomie_trait.sharethings = True
            else:
                roomie_trait.sharethings = False
        else:
            roomie_trait.sharethings = False

        if roomie_studyinroom:
            if roomie_studyinroom == 'True':
                roomie_trait.studyinroom = True
            else:
                roomie_trait.studyinroom = False
        else:
            roomie_trait.studyinroom = False

        if roomie_music:
            if roomie_music == 'True':
                roomie_trait.music = True
            else:
                roomie_trait.music = False
        else:
            roomie_trait.music = False

        if rt_exists:
            db.session.commit()
        else:
            roomie_trait.create()
        return redirect(url_for('user.profile'))

    return render_template('user/traits.html', traits=db_traits, traits_questions=traits_questions,
                           user=current_user, user_trait=trait_obj_to_list(user_trait), roomie_trait=trait_obj_to_list(roomie_trait))
