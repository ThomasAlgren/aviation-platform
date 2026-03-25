from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

login_manager = LoginManager()
login_manager.login_view = "login"
login_manager.login_message = "Please log in to access this page."
