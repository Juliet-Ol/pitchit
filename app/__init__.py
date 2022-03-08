# from ensurepip import bootstrap
from flask import Flask
from flask_bootstrap import Bootstrap
from config import Config
from flask_sqlalchemy import SQLAlchemy

#Initializing application 
app = Flask(__name__) 
app.config.from_object(Config)

bootstrap = Bootstrap(app)
db = SQLAlchemy #creatin a database instance

# initializing flask extentions
bootstrap.init_app(app)
db.init_app(app)


from app import models,errors, views