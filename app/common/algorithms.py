def match_traits(u_traits, r_traits):

    u_traits = vars(u_traits)
    r_traits = vars(r_traits)

    u_traits.pop('_sa_instance_state', None)
    u_traits.pop('id', None)
    u_traits.pop('user_id', None)

    r_traits.pop('_sa_instance_state', None)
    r_traits.pop('id', None)
    roomie = r_traits.pop('user_id', None)

    shared_traits = {
        k: u_traits[k] for k in u_traits if k in r_traits and u_traits[k] == r_traits[k]}

    return (int(len(shared_traits)/11 * 100))


def sort_rooms_by_match(rooms):
    return sorted(rooms, key=lambda i: i['match'], reverse=True)
