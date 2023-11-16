from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app import db


from app.models import User, RegisterPayload
from flask_jwt_extended import create_access_token, create_refresh_token
from typing import Optional, Tuple


def auth_user(username: str, password: str) -> Tuple[Optional[str], Optional[str]]:
    user = User.query.filter_by(username=username).first()
    if user and user.username == username and user.password == password:
        return create_access_token(identity=user.username), create_refresh_token(identity=user.username)

    return None, None


def create_user(userDetails: RegisterPayload):
    existing_user = User.query.filter_by(username=userDetails.username).first()
    if existing_user:
        return False
    new_user = User(username=userDetails.username, fullname=userDetails.fullname, password=userDetails.password)
    db.session.add(new_user)
    db.session.commit()

    return True


def get_user_details(username: str):
    user_data = User.query.with_entities(User.username, User.fullname).filter_by(username=username).first()
    if not user_data:
        return None
    user_data = {'fullname': user_data.fullname, 'username': user_data.username}
    return user_data


def refresh_token(identity):
    return create_access_token(identity=identity)
