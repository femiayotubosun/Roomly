from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from app.models import Hostel, UserTrait, RoomieTrait
from app.common.service import get_all_query, get_one_query
from app.common.algorithms import sort_rooms_by_match, match_traits

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
    room_matches = []

    for room in hostel.rooms:
        if len(room.users) == 0:
            empty_rooms.append(room)
            continue
        occupied_rooms.append(room)
    # Get Match for Rooms
    for room in occupied_rooms:
        counter = 0
        accum = 0
        for user in room.users:
            accum += (match_traits(get_one_query(
                RoomieTrait, current_user.id), get_one_query(UserTrait, user.id)))
            counter += 1
        match_percentage = accum / counter
        room_matches.append({'room': room, 'match': match_percentage})
    room_matches = sort_rooms_by_match(room_matches)
    print(room_matches)

    return render_template('user/one_hostel.html', user=current_user, hostel=hostel, empty_rooms=empty_rooms, other_rooms=room_matches)
