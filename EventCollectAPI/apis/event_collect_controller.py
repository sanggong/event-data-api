from flask import request
from flask_restx import Resource, Namespace
import json
import logging
from utils.apiutil import success
from utils.sqs import SQS
from config import AWS


api = Namespace('EventCollectController')

@api.route('/collect')
class EventCollectController(Resource):
    def post(self):
        sqs = SQS(AWS['SQS_URL'], AWS['REGION'])
        sqs.send_sqs_message(json.dumps(request.get_json()))
        return success()