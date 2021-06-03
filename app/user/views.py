from app.common.algorithms import match_traits, sort_rooms_by_match
from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from werkzeug.utils import redirect
from app.user.forms import ProfileForm
from app.exts import db
from app.common.service import get_all_query, get_one_query
from app.common.traits import db_traits
from app.models import User, UserTrait, RoomieTrait, Hostel

user_bp = Blueprint('user_bp', __name__, template_folder='templates')


@user_bp.route('/dashboard', methods=['GET'])
@login_required
def dashboard():
    return render_template('user/dashboard.html', user=current_user)


@user_bp.route('/profile', methods=['POST', 'GET'])
@login_required
def profile():
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

        return redirect(url_for('user.profile'))

    return render_template('user/profile.html', user=current_user, form=ProfileForm())


@user_bp.route('/traits', methods=['POST', 'GET'])
@login_required
def traits():
    if request.method == 'POST':
        # Initialize all user traits into vars
        ut_exists = False
        rt_exists = False

        new_user_trait = UserTrait.query.filter_by(
            user_id=current_user.id).first()

        if new_user_trait:
            ut_exists = True
        else:
            new_user_trait = UserTrait(user_id=current_user.id)

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
            if user_neat == 'yes':
                new_user_trait.neat = True
            else:
                new_user_trait.neat = False
        else:
            if new_user_trait.neat == True or new_user_trait.neat == False:
                pass
            else:
                new_user_trait.neat = False

        if user_quiet:
            if user_quiet == 'yes':
                new_user_trait.quiet = True
            else:
                new_user_trait.quiet = False
        else:
            if new_user_trait.neat == True or new_user_trait.neat == False:
                pass
            else:
                new_user_trait.quiet = False

        if user_visitors:
            if user_visitors == 'yes':
                new_user_trait.visitors = True
            else:
                new_user_trait.visitors = False
        else:
            if new_user_trait.neat == True or new_user_trait.neat == False:
                pass
            else:
                new_user_trait.visitors = False

        if user_smoker:
            if user_smoker == 'yes':
                new_user_trait.smoker = True
            else:
                new_user_trait.smoker = False
        else:
            if new_user_trait.neat == True or new_user_trait.neat == False:
                pass
            else:
                new_user_trait.smoker = False

        if user_drinker:
            if user_drinker == 'yes':
                new_user_trait.drinker = True
            else:
                new_user_trait.drinker = False
        else:
            if new_user_trait.neat == True or new_user_trait.neat == False:
                pass
            else:
                new_user_trait.drinker = False

        if user_earlybird:
            if user_earlybird == 'yes':
                new_user_trait.earlybird = True
            else:
                new_user_trait.earlybird = False
        else:
            if new_user_trait.neat == True or new_user_trait.neat == False:
                pass
            else:
                new_user_trait.earlybird = False

        if user_nightcrawler:
            if user_nightcrawler == 'yes':
                new_user_trait.nightcrawler = True
            else:
                new_user_trait.nightcrawler = False
        else:
            if new_user_trait.neat == True or new_user_trait.neat == False:
                pass
            else:
                new_user_trait.nightcrawler = False

        if user_snores:
            if user_snores == 'yes':
                new_user_trait.snores = True
            else:
                new_user_trait.snores = False
        else:
            if new_user_trait.neat == True or new_user_trait.neat == False:
                pass
            else:
                new_user_trait.snores = False

        if user_sharethings:
            if user_sharethings == 'yes':
                new_user_trait.sharethings = True
            else:
                new_user_trait.sharethings = False
        else:
            if new_user_trait.neat == True or new_user_trait.neat == False:
                pass
            else:
                new_user_trait.sharethings = False

        if user_studyinroom:
            if user_studyinroom == 'yes':
                new_user_trait.studyinroom = True
            else:
                new_user_trait.studyinroom = False
        else:
            if new_user_trait.neat == True or new_user_trait.neat == False:
                pass
            else:
                new_user_trait.studyinroom = False

        if user_music:
            if user_music == 'yes':
                new_user_trait.music = True
            else:
                new_user_trait.music = False
        else:
            if new_user_trait.neat == True or new_user_trait.neat == False:
                pass
            else:
                new_user_trait.music = False

        if ut_exists:
            db.session.commit()
        else:
            new_user_trait.create()

        # Initialize all roomie triats into vars
        new_roomie_trait = RoomieTrait.query.filter_by(
            user_id=current_user.id).first()
        if new_roomie_trait:
            print(new_roomie_trait)
            rt_exists = True
        else:
            new_roomie_trait = RoomieTrait(user_id=current_user.id)

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
            if roomie_neat == 'yes':
                new_roomie_trait.neat = True
            else:
                new_roomie_trait.neat = False
        else:
            new_roomie_trait.neat = False

        if roomie_quiet:
            if roomie_quiet == 'yes':
                new_roomie_trait.quiet = True
            else:
                new_roomie_trait.quiet = False
        else:
            new_roomie_trait.quiet = False

        if roomie_visitors:
            if roomie_visitors == 'yes':
                new_roomie_trait.visitors = True
            else:
                new_roomie_trait.visitors = False
        else:
            new_roomie_trait.visitors = False

        if roomie_smoker:
            if roomie_smoker == 'yes':
                new_roomie_trait.smoker = True
            else:
                new_roomie_trait.smoker = False
        else:
            new_roomie_trait.smoker = False

        if roomie_drinker:
            if roomie_drinker == 'yes':
                new_roomie_trait.drinker = True
            else:
                new_roomie_trait.drinker = False
        else:
            new_roomie_trait.drinker = False

        if roomie_earlybird:
            if roomie_earlybird == 'yes':
                new_roomie_trait.earlybird = True
            else:
                new_roomie_trait.earlybird = False
        else:
            new_roomie_trait.earlybird = False

        if roomie_nightcrawler:
            if roomie_nightcrawler == 'yes':
                new_roomie_trait.nightcrawler = True
            else:
                new_roomie_trait.nightcrawler = False
        else:
            new_roomie_trait.nightcrawler = False

        if roomie_snores:
            if roomie_snores == 'yes':
                new_roomie_trait.snores = True
            else:
                new_roomie_trait.snores = False
        else:
            new_roomie_trait.snores = False

        if roomie_sharethings:
            if roomie_sharethings == 'yes':
                new_roomie_trait.sharethings = True
            else:
                new_roomie_trait.sharethings = False
        else:
            new_roomie_trait.sharethings = False

        if roomie_studyinroom:
            if roomie_studyinroom == 'yes':
                new_roomie_trait.studyinroom = True
            else:
                new_roomie_trait.studyinroom = False
        else:
            new_roomie_trait.studyinroom = False

        if roomie_music:
            if roomie_music == 'yes':
                new_roomie_trait.music = True
            else:
                new_roomie_trait.music = False
        else:
            new_roomie_trait.music = False

        if rt_exists:
            db.session.commit()
        else:
            new_roomie_trait.create()

    return render_template('user/traits.html', traits=db_traits)
