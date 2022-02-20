from apis.event_type import EventType
from apis import db


class Event(db.Model):
    __tablename__ = 'events'

    id = db.Column(db.BigInteger, primary_key=True)
    user_id = db.Column(db.BigInteger, nullable=False)
    event = db.Column(db.Enum(EventType), nullable=False)
    event_datetime = db.Column(db.DateTime, nullable=False)

    def as_dict(self):
        return {col.name: getattr(self, col.name) for col in self.__table__.columns}
