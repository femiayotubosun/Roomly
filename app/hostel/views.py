from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from app.models import Hostel, UserTrait
from app.common.service import get_all_query, get_one_query
from app.common.algorithms import match_traits

hostel_bp = Blueprint('hostel_bp', __name__, template_folder='templates')


@hostel_bp.route('/', methods=['GET'])
@login_required
def hostels():
    # Check if user has done traits
    user_traits = get_one_query(UserTrait, current_user.id)
    if not user_traits or not current_user.gender:
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

    # Get the hostel
    hostel = get_one_query(Hostel, id)

    # Check if the gender can be assigned to that hostel
    if not((hostel.hosteltype == "Co-Ed") or (hostel.hosteltype == current_user.gender)):
        flash('You cannot be assigned to this hostel', 'error')
        return redirect(url_for('hostel_bp.hostels'))

    # Create an empty list for empty rooms and occupied rooms
    empty_rooms = []
    occupied_rooms = []

    # hostel.rooms is a list of rooms in that hostel. Loop through the rooms.
    for room in hostel.rooms:
        # For each room, there are occupants, which is a list of users in that room

        # Check if the room is empty, add to empty rooms if it is.
        if len(room.occupants) == 0:
            empty_rooms.append(room)
            continue

        # Else add to occupied rooms.
        occupied_rooms.append(room)

    # Do match for occupied rooms.
    for room in occupied_rooms:
        accum = 0
        room_mem = 0
        for user in room.occupants:
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
