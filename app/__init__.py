from ensurepip import bootstrap
from flask import Flask
from flask_bootstrap import Bootstrap
from config import Config

#Initializing application 
app = Flask(__name__) 
app.config.from_object(Config)

bootstrap = Bootstrap(app)

from app import views