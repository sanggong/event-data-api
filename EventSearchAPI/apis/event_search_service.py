from apis.event import Event
from apis.purchase import Purchase
from apis.stage import Stage
from apis import db
from apis.event_type import EventType


def get_all_event_by_user(user_id):
    responses = []
    events = Event.query.filter_by(user_id=user_id).order_by(Event.id.desc())
    for event in events:
        response = dict()
        response['event_id'] = event.id
        response['event'] = event.event.name
        param = None
        if (event.event == EventType.stagein or
            event.event == EventType.clear or
            event.event == EventType.fail
        ):
            stage = Stage.query.filter_by(event_id=event.id).first()
            param = dict()
            param['stage'] = stage.stage
        elif (event.event == EventType.purchase):
            purchase = Purchase.query.filter_by(event_id=event.id).first()
            param = dict()
            param['order_id'] = purchase.id
            param['currency'] = purchase.currency.name
            param['price'] = purchase.price
        response['parameters'] = param
        response['event_datetime'] = event.event_datetime.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + 'Z'
        responses.append(response)

    return responses




