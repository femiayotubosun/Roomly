from flask import Flask
from flask.helpers import url_for
from app.exts import db, login_manager
from app.user.views import user
from app.main.views import main
from app.auth.routes import auth
from app.models import User


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


def register_blueprints(app):
    app.register_blueprint(main, url_prefix='/')
    app.register_blueprint(user, url_prefix='/user')
    app.register_blueprint(auth, url_prefix='/auth')
