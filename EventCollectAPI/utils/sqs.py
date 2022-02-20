import boto3


class SQS:
    def __init__(self, sqs_url, region):
        self._sqs_url = sqs_url
        self._region = region
        self._sqs = boto3.client('sqs', region_name=self._region)

    def send_sqs_message(self, data):
        response = self._sqs.send_message(QueueUrl=self._sqs_url,
                                         MessageBody=data)
        return response

