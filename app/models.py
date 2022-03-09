from tabnanny import check
from app import db,login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),unique=True, nullable=False, index = True)
    email = db.Column(db.String(255),unique = True,index = True, nullable=False)
    
    password_hash = db.Column(db.String(255), nullable=False)


   

    def __repr__(self):
        return f'User {self.id} {self.username}' 

    def set_password(self, password):
        self.password_hash = generate_password_hash(password) 

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)        
