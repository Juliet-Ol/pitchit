from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from flask_login import LoginManager
from flask_moment import Moment


login_manager = LoginManager()
bootstrap = Bootstrap()
db = SQLAlchemy()
migrate = Migrate()
moment = Moment()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)


    bootstrap.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    moment.init_app(app)

    from app.errors import bp as errors_bp
    app.register_blueprint(errors_bp)
    
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    from app.auth import bp as auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')

    return app

from app import models