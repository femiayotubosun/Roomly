from app.models import RoomieTrait, UserTrait
from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import current_user, login_required
from app.common.service import get_one_query, set_user_trait
from app.common.traits import traits_questions, db_traits

trait_bp = Blueprint('trait_bp', __name__, template_folder='templates')


@trait_bp.route('/', methods=['GET', 'POST'])
@login_required
def quiz_home():
    # Send questions actually.
    return render_template('traits/start.html', user=current_user)


@trait_bp.route('/quiz', methods=['GET', 'POST'])
@login_required
def quiz():
    user_traits = get_one_query(UserTrait, current_user.id)
    roomie_traits = get_one_query(RoomieTrait, current_user.id)
    traits_bank = []

    # user_traits = vars(user_traits)
    # roomie_traits = vars(roomie_traits)
    if (user_traits):

        for trait in db_traits:
            temp = []
            temp.append(getattr(user_traits, trait))
            temp.append(getattr(roomie_traits, trait))
            traits_bank.append(temp)

    data = {
        'questionBank': traits_questions,
        'traits': db_traits,
        'answerBank': traits_bank
    }

    if request.method == 'POST':
        print("Posting")
        data = request.json
        trait_to_set = data['answerBank']
        set_user_trait(current_user.id, trait_to_set)
        return {'message': 'success'}

    if len(traits_bank) == 0:
        newTraits = 'true'
    else:
        newTraits = 'false'
    return render_template('traits/quiz.html', user=current_user, data=data, newTraits=newTraits)


@trait_bp.route('/endquiz', methods=['GET', 'POST'])
@login_required
def end_quiz():

    return render_template('traits/end.html', user=current_user)
