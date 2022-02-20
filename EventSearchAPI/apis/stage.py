from apis import db


class Stage(db.Model):
    __tablename__ = 'stages'

    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    stage = db.Column(db.Integer, nullable=False)
    event_id = db.Column(db.BigInteger, db.ForeignKey('events.id'),
                      unique=True, nullable=False)
    event = db.relationship('apis.event.Event')

    def as_dict(self):
        return {col.name: getattr(self, col.name) for col in self.__table__.columns}

