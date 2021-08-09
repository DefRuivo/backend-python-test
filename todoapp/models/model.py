from operator import truediv
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from sqlalchemy.orm import backref

db = SQLAlchemy()

def configure(app):
    db.init_app(app)
    app.db = db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=True, nullable=False)
    todos = db.relationship("Todo", backref="user", lazy=True)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    description = db.Column(db.Text)
    
    def __repr__(self):
        return self.description