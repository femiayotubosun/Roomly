from app.exts import db
from flask_login import UserMixin


class Hostel(db.Model):

    __tablename__ = 'hostel'

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    name = db.Column(
        db.String(40),
    )

    hosteltype = db.Column(
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

    def __repr__(self):
        return f'<Hostel {self.name}>'


class Room(db.Model):

    __tablename__ = 'room'

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

    def __repr__(self):
        return f'<Room {self.name}>'


class User(db.Model, UserMixin):

    __tablename__ = 'user'

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
        db.String(255)

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

    gender = db.Column(
        db.String(255)
    )

    photo_name = db.Column(
        db.String(255)
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

    def __repr__(self):
        return f'<User {self.username}>'


class UserTrait(db.Model):

    __tablename__ = 'usertrait'

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    user_id = db.Column(
        db.Integer,
        nullable=False
    )

    neat = db.Column(
        db.Boolean
    )

    quiet = db.Column(
        db.Boolean
    )
    visitors = db.Column(
        db.Boolean
    )
    smoker = db.Column(
        db.Boolean
    )
    drinker = db.Column(
        db.Boolean
    )

    earlybird = db.Column(
        db.Boolean
    )

    nightcrawler = db.Column(
        db.Boolean
    )

    snores = db.Column(
        db.Boolean
    )

    sharethings = db.Column(
        db.Boolean
    )

    studyinroom = db.Column(
        db.Boolean
    )

    music = db.Column(
        db.Boolean
    )

    lightsleeper = db.Column(
        db.Boolean
    )
    darkroom = db.Column(
        db.Boolean
    )

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    def __repr__(self):
        return f'<UserTrait {self.user_id}>'


class RoomieTrait(db.Model):

    __tablename__ = 'roomietrait'

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    user_id = db.Column(
        db.Integer,
        nullable=False
    )

    neat = db.Column(
        db.String(255)
    )

    quiet = db.Column(
        db.String(255)
    )
    visitors = db.Column(
        db.String(255)
    )
    smoker = db.Column(
        db.String(255)
    )
    drinker = db.Column(
        db.String(255)
    )

    earlybird = db.Column(
        db.String(255)
    )

    nightcrawler = db.Column(
        db.String(255)
    )

    snores = db.Column(
        db.String(255)
    )

    sharethings = db.Column(
        db.String(255)
    )

    studyinroom = db.Column(
        db.String(255)
    )

    music = db.Column(
        db.String(255)
    )

    lightsleeper = db.Column(
        db.String(255)
    )
    darkroom = db.Column(
        db.String(255)
    )

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    def __repr__(self):
        return f'<RoomieTrait {self.user_id}>'
