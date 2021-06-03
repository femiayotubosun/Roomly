from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_admin import Admin
from app.admin.admin import AdminView

db = SQLAlchemy()
login_manager = LoginManager()

admin = Admin(index_view=AdminView(name="Room.ly-Admin", url='/admin',
                                   endpoint='admin'))
