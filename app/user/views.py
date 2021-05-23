from flask import Blueprint, render_template
from flask_login import login_required, current_user

user = Blueprint('user', __name__, template_folder='templates')


@user.route('/dashboard', methods=['GET'])
@login_required
def dashboard():
    user = current_user
    return render_template('user/dashboard.html', user=user)
