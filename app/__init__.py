# from ensurepip import bootstrap

from distutils.command.config import config
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(config)

login_manager = LoginManager()
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
migrate = Migrate(app,db)

from app import routes, errors, models


