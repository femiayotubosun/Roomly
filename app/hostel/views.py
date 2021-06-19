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
        # To get the total room match average.
        # We need to get the total sum of matches and divide it by the room_mem
        # If the current logged in user in that room, we don't want to add him
        # To this calculation, it wouldn't really makes sense.
        sum_of_matches = 0
        room_mem = len(room.occupants)
        # room members are in room.occupants, loop through them
        for user in room.occupants:
            # If the user in the current looop is the logged in user, skip
            if(user.id == current_user.id):
                room_mem -= 1
            else:
                sum_of_matches += match_traits(current_user.id, user.id)

        # This means that its only the current_user that is in that room.
        # Because room_mem doesn't increase. His match percentage is perfect then.
        if room_mem == 0:
            match_percentage = 100
        else:
            match_percentage = round(sum_of_matches / room_mem)

        # Add a new attribute to the room, save the it in match, so we can use it in the frontend
        room.match = match_percentage

    return render_template('user/one_hostel.html', user=current_user, hostel=hostel, empty_rooms=empty_rooms, other_rooms=occupied_rooms)
