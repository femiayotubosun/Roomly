from flask import Blueprint, render_template, url_for, request, redirect, flash
from flask_login import current_user
from flask_login.utils import login_required
from app.exts import db
from app.common.service import get_one_query
from app.common.algorithms import match_traits
from app.models import Room, User, UserTrait

room_bp = Blueprint('room_bp', __name__, template_folder='templates')


@room_bp.route('/<roomId>', methods=['GET', 'POST'])
@login_required
def room(roomId):
    # Check if user has done traits
    user_traits = get_one_query(UserTrait, current_user.id)
    if not user_traits:
        flash('Please fill traits before picking your room', 'error')
        return redirect(url_for('user_bp.traits'))

    room = get_one_query(Room, roomId)
    occupants_match = []
    user_traits = get_one_query(UserTrait, current_user.id)

    print(user_traits)
    if user_traits and len(room.users) >= 1:
        for user in room.users:
            if(user.id == current_user.id):
                r_traits = user_traits
            else:
                r_traits = get_one_query(UserTrait, user.id)

            occupants_match.append(match_traits(user_traits, r_traits))

    print(occupants_match)
    if request.method == 'POST':
        if len(room.users) >= room.bedspace:
            flash('This room is full', 'fair')
            return redirect(url_for('room_bp.room', roomId=roomId))
        current_user.room = room
        db.session.commit()
        flash('Assigned successfully', 'success')

    return render_template('room/one_room.html', user=current_user, room=room)
