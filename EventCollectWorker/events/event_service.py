from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime

import config
from events.event import Event
from events.purchase import Purchase
from events.stage import Stage
from events.event_type import EventType
from events.currency_type import CurrencyType

engine = create_engine('mysql+pymysql://{}:{}@{}:3306/{}'
                       .format(config.RDS['USER'],
                               config.RDS['PASSWORD'],
                               config.RDS['URL'],
                               config.RDS['NAME']))


def save_event(data):
    Session = sessionmaker(bind=engine)
    with Session() as session:
        event = session.query(Event).filter_by(id=data['event_id']).first()
        if not event:
            new_event = Event(
                id=data['event_id'],
                user_id=data['user_id'],
                event=EventType[data['event']],
                event_datetime=datetime.now()
            )
            session.add(new_event)

            if (new_event.event == EventType.stagein or
                    new_event.event == EventType.clear or
                    new_event.event == EventType.fail
            ):
                new_stage = Stage(
                    stage=data['parameters']['stage'],
                    event_id=new_event.id
                )
                session.add(new_stage)

            elif new_event.event == EventType.purchase:
                new_purchase = Purchase(
                    id=data['parameters']['order_id'],
                    currency=CurrencyType[data['parameters']['currency']],
                    price=data['parameters']['price'],
                    event_id=new_event.id
                )
                session.add(new_purchase)

            session.commit()
