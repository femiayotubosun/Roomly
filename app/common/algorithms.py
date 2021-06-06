
def trait_obj_to_list(traits):
    try:
        traits = vars(traits)
        traits.pop('_sa_instance_state', None)
        traits.pop('id', None)
        traits.pop('user_id', None)
    except:
        return None

    return traits


def match_traits(u_traits, r_traits):
    u_traits = trait_obj_to_list(u_traits)
    r_traits = trait_obj_to_list(r_traits)
    shared_traits = {
        k: u_traits[k] for k in u_traits if k in r_traits and u_traits[k] == r_traits[k]}

    return (int(len(shared_traits)/11 * 100))


def sort_rooms_by_match(rooms):
    return sorted(rooms, key=lambda i: i['match'], reverse=True)
