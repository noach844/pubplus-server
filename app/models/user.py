from app import db


class User(db.Model):
    __tablename__ = 'users'  # Specify the desired table name
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    fullname = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(50), nullable=False)

