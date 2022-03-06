from flask import Flask

#Initializing application 
app = Flask(__name__) #create app instancee and allow connect to instance folder

from app import views