from app import app
from models import db, Message

with app.app_context():
    db.drop_all()
    db.create_all()

    msg1 = Message(body="Hello, world!", username="Ian")
    msg2 = Message(body="Flask + React is fun!", username="Pascal")

    db.session.add_all([msg1, msg2])
    db.session.commit()
