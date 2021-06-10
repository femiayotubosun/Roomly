from flask import Flask
from flask_admin.contrib.sqla import ModelView
from flask_sqlalchemy.model import Model
from app.exts import db, login_manager, admin
from app.user.views import user_bp
from app.main.views import main
from app.auth.routes import auth
from app.room.views import room_bp
from app.hostel.views import hostel_bp
from app.traits.views import trait_bp
from app.models import User, Hostel, Room, UserTrait, RoomieTrait


def create_app(config_object='config.Config'):
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    register_blueprints(app)
    return app


def register_extensions(app):
    # Set up database
    db.init_app(app)
    from app import models
    db.create_all(app=app)

    # Set up flask_login
    login_manager.login_view = 'main.homepage'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Set up flask-admin
    admin.init_app(app)
    admin.add_view(ModelView(Hostel, db.session))
    admin.add_view(ModelView(Room, db.session))
    admin.add_view(ModelView(User, db.session))
    admin.add_view(ModelView(UserTrait, db.session))
    admin.add_view(ModelView(RoomieTrait, db.session))


def register_blueprints(app):
    app.register_blueprint(main, url_prefix='/')
    app.register_blueprint(user_bp, url_prefix='/user')
    app.register_blueprint(auth, url_prefix='/auth')
    app.register_blueprint(room_bp, url_prefix='/rooms')
    app.register_blueprint(hostel_bp, url_prefix='/hostels')
    app.register_blueprint(trait_bp, url_prefix='/traitQuiz')
