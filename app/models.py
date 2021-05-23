from app.exts import db
from flask_login import UserMixin


class Hostel(db.Model):

    tablename = 'hostel'

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    name = db.Column(
        db.String(40),
        unique=True
    )

    type = db.Column(
        db.String(40)
    )

    address = db.Column(
        db.String(255)
    )

    price = db.Column(
        db.Integer
    )

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    def repr(self):
        return f'<Hostel {self.name}'


class Room(db.Model):

    tablename = 'room'

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    name = db.Column(
        db.String(5),
        nullable=False
    )

    bathroom = db.Column(
        db.Boolean,
        default=False
    )

    bedspace = db.Column(
        db.Integer,
        default=3
    )

    hostel_id = db.Column(
        db.Integer,
        db.ForeignKey('hostel.id')
    )

    # The idea is that we'll be able to specify the hostel
    # when we are creating a room record. Instead of
    # db.Column, we use db.relationship. Then we put the *class name*(not table name)
    # of the reference record. backref(specify name of the field) will create a field
    # on the reference record,
    # which will be a list of all records that have a relationship with one specific
    # hostel record.

    hostel = db.relationship(
        "Hostel",
        backref="rooms"
    )

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    def repr(self):
        return f'<Room {self.name}>'


class User(db.Model, UserMixin):

    tablename = 'user'

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    name = db.Column(
        db.String(255)
    )

    username = db.Column(
        db.String(255),
        nullable=False,
        unique=True

    )
    address = db.Column(
        db.String(255)

    )
    number = db.Column(
        db.Integer

    )

    school = db.Column(
        db.String(255)

    )

    email = db.Column(
        db.String(255),
        nullable=False,
        unique=True
    )
    password = db.Column(
        db.String(255),
        nullable=False
    )

    room_id = db.Column(
        db.Integer,
        db.ForeignKey('room.id')
    )

    room = db.relationship(
        'Room', backref='users'
    )

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    def repr(self):
        return f'<Room {self.name}>'
