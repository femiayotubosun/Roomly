from app.exts import db


def get_all(Model):
    return Model.query.all()


def get_one(Model, identifier):
    return Model.query.get_or_404(identifier)


def delete_one(Model, identifier):
    data = get_one(Model, identifier)

    if not data:
        return None

    db.session.delete(data)
    db.session.commit()
    return None
