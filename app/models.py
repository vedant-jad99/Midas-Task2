from app import db, login_manager
from flask_login import UserMixin
from datetime import datetime

@login_manager.user_loader
def load_user(userid):
    return User.query.get(int(userid))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(40), unique=False, nullable=True)
    last_name = db.Column(db.String(40), unique=False, nullable=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(40), unique=False, nullable=False)
    account_created = db.Column(db.DateTime, nullable=False, default=datetime.now())

    def __repr__(self):
        return "User details - Name: {}, Username: {}, Email: {}".format(self.first_name + " " + self.last_name, self.username, self.email)