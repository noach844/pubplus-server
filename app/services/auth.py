from app import db, Status
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
    new_user = User(username=userDetails.username, fullname=userDetails.fullname, password=userDetails.password, status_id=1)
    db.session.add(new_user)
    db.session.commit()

    return True


def refresh_token(identity):
    return create_access_token(identity=identity)
