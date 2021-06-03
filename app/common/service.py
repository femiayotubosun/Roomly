from app.exts import db
from app.models import UserTrait, RoomieTrait


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
