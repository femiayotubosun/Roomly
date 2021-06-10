from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import current_user, login_required
from app.common.service import set_user_trait

trait_bp = Blueprint('trait_bp', __name__, template_folder='templates')


@trait_bp.route('/', methods=['GET', 'POST'])
@login_required
def quiz_home():
    # Send questions actually.
    return render_template('traits/start.html', user=current_user)


@trait_bp.route('/quiz', methods=['GET', 'POST'])
@login_required
def quiz():
    if request.method == 'POST':
        data = request.json
        trait_to_set = data['answerArray']
        set_user_trait(current_user.id, trait_to_set)

        return {'message': 'success'}
    return render_template('traits/quiz.html', user=current_user)


@trait_bp.route('/endquiz', methods=['GET', 'POST'])
@login_required
def end_quiz():

    return render_template('traits/end.html', user=current_user)
