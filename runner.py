import datetime
import math
import random
import uuid

from revos import catalog, thread

CONFIG = {

    "host": "http://localhost:9000",

    "uri": "/v1/iotrequest",

    "max_queue_size": 60,

    "sleep": 3

    # "host": "http://localhost:8080",

    # "filename": "revos.dev.full.log"
}

headers = {

    "x-amz-sns-topic-arn": "arn:aws:sns:us-east-1:157715479645:edt-device-connect-event-service-sns-topic-REVOS",

    "x-amz-sns-message-id": str(uuid.uuid4()),

    "x-amz-sns-message-type": "Notification",

    "Content-Type": "application/json"
}

request = {}

def submit_deep_laser(parameters):

    submit_request = thread.ThreadRequest(params=parameters, headers=headers, config=CONFIG)
    submit_request.start()
    submit_request.join()

def throttle(string):

    """
    Throttle
    Load test
    :param string:
    :return:
    """
    value = int(string)

    handler = open("payload.log", "w")

    total_char_count = len(catalog.chars) - 1

    iterations = math.ceil(value / 4)

    total_activity_count = len(catalog.activity) - 1

    entries = []

    entry = 0

    i = 0

    parameters = {}

    while i < value:

        now = datetime.datetime.now()

        telemetry_key_index = "TelemetryDataLog_" + str(entry + 1)

        log = "\t".join([

            str(i + 1),

            catalog.chars[random.randint(0, total_char_count)],

            now.strftime("%d/%m/%Y %H:%M:%S.%f")[:-3],

            catalog.activity[random.randint(0, total_activity_count)]])

        parameters[telemetry_key_index] = log

        entries.append(log)

        entry += 1

        if entry == 4:

            submit_deep_laser(parameters)

            entry = 0

        i += 1

    if len(parameters):

        submit_deep_laser(parameters)

    handler.write("\n".join(entries))


throttle("150")
exit()

