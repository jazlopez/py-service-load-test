import datetime
import json
import logging
import random
import sys
import time
import uuid
from threading import Thread

import requests

CONSTANT_DEVICE_ID = sys.argv[1]

CONSTANT_ENDPOINT_URL = sys.argv[2]

CONSTANT_MESSAGE_ID = str(uuid.uuid4())

CONFIG = {

    "host": CONSTANT_ENDPOINT_URL,

    "uri": "/api/revos/public/v1/log/message"
}

logging.basicConfig(level=logging.DEBUG)

headers = {

    "x-amz-sns-topic-arn": "arn:aws:sns:us-east-1:157715479645:edt-device-connect-event-service-sns-topic-REVOS",

    "x-amz-sns-message-id": CONSTANT_MESSAGE_ID,

    "x-amz-sns-message-type": "Notification",

    "Content-Type": "application/json"
}


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

            "Type": "Notification",

            "MessageId": str(uuid.uuid4()),

            "TopicArn": self.headers["x-amz-sns-topic-arn"],

            "Message": json.dumps({

                "deviceType": "REVOS",

                "deviceId": CONSTANT_DEVICE_ID,

                "timestamp": str(datetime.datetime.now()),

                "eventKey": "DATA_LOG_SPLUNK",

                "eventParameters": event_parameters
            })
        }

        self.request = activity_template_request

    def do_post(self, data=None):

        if not self.url:
            self.url = self.config["host"] + self.config["uri"]

        logging.info("URL POST %s", self.url)

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


def submit_deep_laser(parameters):

    submit_request = ThreadRequest(params=parameters, headers=headers, config=CONFIG)
    submit_request.start()
    submit_request.join()

diagnostic = open("diagnostic.log", "w+")

started_at = time.time()

with open('template.log') as f:

    while True:

        ___ = []

        for j in range(0,4):

            _ = f.readline()

            if not _:
                break

            ___.append(_)

        __payload = ___.copy()

        random.shuffle(___)

        i = 1

        parameters = dict()

        for __ in ___:

            parameters["TelemetryDataLog_" + str(i) + ""] = __

            i += 1

        submit_deep_laser(parameters)

        for v in __payload:
            diagnostic.write(v)

        current_now = time.time()

        wait_time = random.randint(3,9) / 10

        logging.info("Wait Time %0.2f", wait_time)

        time.sleep(wait_time)

        logging.info("started at %d", started_at)

        logging.info("now %d", current_now)
        logging.info("diff %d", current_now - started_at)

        if current_now - started_at > 300:
            break

        # break

diagnostic.close()
