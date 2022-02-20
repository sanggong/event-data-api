import json
from events.event_service import save_event


def lambda_handler(event, context):
    for record in event['Records']:
        payload = record["body"]
        if type(payload) == str:
            payload = json.loads(payload)
        save_event(payload)

    return {'is_success': True}