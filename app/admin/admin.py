from flask_admin import AdminIndexView
from flask_login import current_user
from flask import redirect, url_for


class AdminView(AdminIndexView):
    '''
    Admin view with custom security
    '''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.static_folder = 'static'

    def is_accessible(self):
        if hasattr(current_user, 'username'):
            return current_user.username == 'admin'
        else:
            return False

    def inaccessible_callback(self, name, **kwargs):
        if not self.is_accessible():
            return redirect(url_for('main.homepage'))
