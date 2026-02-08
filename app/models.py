from app import db
from datetime import datetime

class User(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(50), nullable=False,unique=True)
    password=db.Column(db.String(255), nullable=False)
    email=db.Column(db.String(50), nullable=False,unique=True)
    notes=db.relationship('Note', backref='user', lazy=True)

class Note(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(50), nullable=False)
    content=db.Column(db.Text, nullable=False)
    created_at=db.Column(db.DateTime,default=datetime.utcnow)
    category=db.Column(db.String(50), nullable=False)
    user_id=db.Column(db.Integer, db.ForeignKey('user.id'),nullable=True)
