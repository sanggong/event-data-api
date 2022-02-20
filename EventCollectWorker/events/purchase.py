from sqlalchemy import Column, ForeignKey, BigInteger, Enum
from sqlalchemy.orm import relationship
from events.currency_type import CurrencyType
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Purchase(Base):
    __tablename__ = 'purchases'

    id = Column(BigInteger, primary_key=True)
    currency = Column(Enum(CurrencyType), nullable=False)
    price = Column(BigInteger, nullable=False)
    event_id = Column(BigInteger, unique=True, nullable=False)
