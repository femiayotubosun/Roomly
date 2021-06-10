from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from app.models import Hostel, UserTrait, RoomieTrait
from app.common.service import get_all_query, get_one_query
from app.common.algorithms import match_traits

hostel_bp = Blueprint('hostel_bp', __name__, template_folder='templates')


@hostel_bp.route('/', methods=['GET'])
@login_required
def hostels():
    # Check if user has done traits
    user_traits = get_one_query(UserTrait, current_user.id)
    if not user_traits:
        flash('Please fill traits before picking your room', 'error')
        return redirect(url_for('user_bp.traits'))

    hostels = get_all_query(Hostel)
    return render_template('user/all_hostels.html', user=current_user, hostels=hostels)


@hostel_bp.route('/<id>', methods=['GET'])
@login_required
def hostel(id):
    # Check if user has done traits
    user_traits = get_one_query(UserTrait, current_user.id)
    if not user_traits:
        flash('Please fill traits before picking your room', 'error')
        return redirect(url_for('user_bp.traits'))
    hostel = get_one_query(Hostel, id)

    # Check for empty rooms and occupied rooms
    empty_rooms = []
    occupied_rooms = []

    for room in hostel.rooms:
        if len(room.users) == 0:
            empty_rooms.append(room)
            continue
        occupied_rooms.append(room)
    # Get Match for Rooms
    for room in occupied_rooms:
        accum = 0
        room_mem = 0
        for user in room.users:
            if(user.id == current_user.id):
                continue
            else:
                room_mem += 1
                accum += match_traits(current_user.id, user.id)

        if room_mem == 0:
            match_percentage = 100
        else:
            match_percentage = round(accum / room_mem)

        room.match = match_percentage

    return render_template('user/one_hostel.html', user=current_user, hostel=hostel, empty_rooms=empty_rooms, other_rooms=occupied_rooms)
