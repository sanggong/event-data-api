from flask import request
from flask_restx import Resource, Namespace
from apis.event_search_service import get_all_event_by_user
from utils.apiutil import success
from apis import db
import json

api = Namespace('EventSearchController')

@api.route('/search')
class EventSearchController(Resource):
    def post(self):
        user_id = json.loads(request.get_data())['user_id']
        data = get_all_event_by_user(user_id)
        return success(data)
