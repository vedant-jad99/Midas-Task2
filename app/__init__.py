from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SECRET_KEY"] = 'ff127ef745c8859dd6509413570a5bd3'
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt()

from app import routes