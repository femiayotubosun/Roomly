from app.models import RoomieTrait, UserTrait
from app.common.service import get_one_query
from app.common.traits import db_traits


def match_traits(myId, theirId):

    # We need to match four things
    # What I want against what he has
    # RoomieTrait(myId) UserTrait(theirId)
    # What he wants against what I have
    # RoomieTria(theirId)) UserTriat(myId)
    # I need only their ids
    my_ideal_roomie = get_one_query(RoomieTrait, myId)
    candidate_user = get_one_query(UserTrait, theirId)
    my_traits = get_one_query(UserTrait, myId)
    candidate_user_ideal_roomie = get_one_query(RoomieTrait, theirId)

    my_matching_traits = []
    their_matching_trait = []

    # Loop through the traits and get matching traits
    for trait in db_traits:

        perfect_roomie = getattr(my_ideal_roomie, trait)
        candidate_traits = str(getattr(candidate_user, trait))
        my_own_traits = str(getattr(my_traits, trait))
        candidate_perfect_roomie = getattr(
            candidate_user_ideal_roomie, trait)

        if perfect_roomie == 'Neutral' or perfect_roomie == candidate_traits:
            my_matching_traits.append(trait)

        if candidate_perfect_roomie == 'Maybe' or candidate_perfect_roomie == 'Neutral' or my_own_traits == candidate_perfect_roomie:
            their_matching_trait.append(trait)

    match = (len(my_matching_traits) + len(their_matching_trait)) * (100/26)
    return round(match)
