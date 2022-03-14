from flask import Blueprint, Flask
# from flask_mail import Mail
# from app import app

bp = Blueprint('auth',__name__)
# mail = Mail()

def create_app(config_name):
    app = Flask(__name__)

from app.auth import views, forms

# mail.init_app(app)