from app.models import Status

def init_status_db(db):
    default_names = ['Working', 'Working Remotely', 'On Vacation', 'Business Trip']
    for name in default_names:
        if not Status.query.filter_by(name=name).first():
            status = Status(name=name)
            db.session.add(status)

    db.session.commit()