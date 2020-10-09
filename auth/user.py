from flask_login import LoginManager
from . import login_manager
from models import User

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
