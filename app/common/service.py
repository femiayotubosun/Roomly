from typing import List
from app.exts import db
from app.models import UserTrait, RoomieTrait
from app.common.traits import db_traits


def get_all_query(Model):
    return Model.query.all()


def get_one_query(Model, identifier):
    if Model == UserTrait:
        return UserTrait.query.filter_by(user_id=identifier).first()
    elif Model == RoomieTrait:
        return RoomieTrait.query.filter_by(user_id=identifier).first()
    else:
        return Model.query.get(identifier)


def delete_one_query(Model, identifier):
    data = get_one_query(Model, identifier)
    if not data:
        return None

    db.session.delete(data)
    db.session.commit()
    return None


def set_user_trait(user_id: int, trait_list: List):

    # Check if they have traits already
    user_trait = get_one_query(UserTrait, user_id)

    if not user_trait:
        data_exists = False
        user_trait = UserTrait(user_id=user_id)
        roomie_trait = RoomieTrait(user_id=user_id)
    else:
        data_exists = True
        roomie_trait = get_one_query(RoomieTrait, user_id)

    for i in range(0, 13):
        if trait_list[i][0] == 'True':
            setattr(user_trait, db_traits[i], True)

        elif trait_list[i][0] == 'False':
            setattr(user_trait, db_traits[i], False)

        else:
            setattr(user_trait, db_traits[i], None)

        setattr(roomie_trait, db_traits[i], trait_list[i][1])

    if data_exists:
        db.session.commit()
    else:
        user_trait.create()
        roomie_trait.create()
