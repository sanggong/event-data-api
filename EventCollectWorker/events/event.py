from sqlalchemy import Column, BigInteger, Enum, DateTime
from sqlalchemy.orm import relationship
from events.event_type import EventType
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Event(Base):
    __tablename__ = 'events'

    id = Column(BigInteger, primary_key=True)
    user_id = Column(BigInteger, nullable=False)
    event = Column(Enum(EventType), nullable=False)
    event_datetime = Column(DateTime(3), nullable=False)
