from app import db
from app.models import User, Status


def update_user_status(username: str, status_id: int):
    user_to_update = User.query.filter_by(username=username).first()

    if user_to_update:
        user_to_update.status_id = status_id
        db.session.commit()
        return True
    return False


def get_user_details(username: str):
    user_data = User.query.with_entities(User.username, User.fullname,User.status_id ,Status.name).join(Status, User.status_id == Status.id).filter(User.username == username).first()
    if not user_data:
        return None
    user_data = {'fullname': user_data.fullname, 'username': user_data.username, 'status_name': user_data.name, 'status_id': user_data.status_id}
    return user_data


def get_all_users(username:str):
    users = User.query.with_entities(User.username, User.fullname,User.status_id ,Status.name).join(Status, User.status_id == Status.id).filter(User.username != username)
    if not users:
        return []
    return [
        {'fullname': user.fullname, 'username': user.username, 'status_name': user.name, 'status_id': user.status_id} for user in users
    ]