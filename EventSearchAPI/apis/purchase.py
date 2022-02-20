from apis.currency_type import CurrencyType
from apis import db


class Purchase(db.Model):
    __tablename__ = 'purchases'

    id = db.Column(db.BigInteger, primary_key=True)
    currency = db.Column(db.Enum(CurrencyType), nullable=False)
    price = db.Column(db.BigInteger, nullable=False)
    event_id = db.Column(db.BigInteger, db.ForeignKey('events.id'),
                      unique=True, nullable=False)
    event = db.relationship('apis.event.Event')

    def as_dict(self):
        return {col.name: getattr(self, col.name) for col in self.__table__.columns}
