from app import db, User
from app.models import Status, RegisterPayload


def all_statuses():
    statuses = Status.query.all()
    if not statuses:
        return None
    return [
        {"value": str(status.id), "label": status.name} for status in statuses
    ]
