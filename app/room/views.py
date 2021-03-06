from flask import Blueprint, render_template, url_for, request, redirect, flash
from flask_login import current_user
from flask_login.utils import login_required
from app.exts import db
from app.common.service import get_one_query
from app.common.traits import traits_strings, db_traits
from app.common.algorithms import match_traits
from app.models import Room, RoomieTrait, UserTrait

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
    if len(room.occupants) > 0:
        for user in room.occupants:
            user.traits = []
            for trait in db_traits:
                if getattr(user_traits, trait):
                    user.traits.append(traits_strings[trait])
                if db_traits[4] == trait:
                    break

    # print(occupants_match)
    if request.method == 'POST':
        if len(room.occupants) >= room.bedspace:
            flash('This room is full.', 'fair')
            return redirect(url_for('room_bp.room', roomId=roomId))

        current_user.room = room
        db.session.commit()
        flash('Assigned successfully.', 'success')
        return redirect(url_for('room_bp.room', roomId=roomId))

    return render_template('room/one_room.html', user=current_user, room=room)


@room_bp.route('/<roomId>/cancelReservation', methods=['GET', 'POST'])
@login_required
def cancel_room(roomId):
    current_user.room = None
    db.session.commit()
    flash('Room reservation cancelled.', 'success')
    return redirect(url_for('room_bp.room', roomId=roomId))
