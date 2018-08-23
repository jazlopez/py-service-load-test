import datetime
import json
import time
from threading import Thread

import requests


class ThreadRequest(Thread):

    """
    Thread Request
    """

    def __init__(self, params=None, config=None, headers=None):

        Thread.__init__(self)
        self.request = {}
        self.response = {}
        self.parameters = params
        self.config = config
        self.headers = headers
        self.url = None

    def run(self):

        self.setup_request(event_parameters=self.parameters)

        self.do_post(data=self.request)

    def setup_request(self, event_parameters=None):

        activity_template_request = {

            "id": "30000",

            "request": "senddata",

            "datatype": "event",

            "eventKey": "DATA_LOG_SPLUNK",

            "eventParameters": event_parameters

        }

        ws_activity_template_request = {

            "Type": "Notification",

            "MessageId": self.headers["x-amz-sns-message-id"],

            "TopicArn": self.headers["x-amz-sns-topic-arn"],

            "Message": json.dumps({

                "deviceType": "REVOS",

                "deviceId": "sync-concurrent-9990",

                "timestamp": str(datetime.datetime.now()),

                "eventKey": "DATA_LOG_SPLUNK",

                "eventParameters": event_parameters
            })
        }

        self.request = activity_template_request

    def do_post(self, data=None):

        if not self.url:
            self.url = self.config["host"] + self.config["uri"]

        start_at = time.time()

        payload = json.dumps(data)

        self.response = requests.post(self.url, headers=self.headers, data=payload)

        request_time = time.time() - start_at

        print("[INFO]\tREQUEST SERVER TOOK {} seconds".format(str(request_time)))

        if not self.response.status_code == 200:
            print("[ERROR]\tUNEXPECTED ERROR: {}".format(self.response.text))
            print(self.response)
            print(data)
            print("\n\n")