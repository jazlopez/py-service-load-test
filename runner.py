import argparse
import datetime
import math
import random
import time
import uuid

from revos import catalog, thread

CONFIG = {

    "host": "https://test.apps.thermofisher.com",

    "uri": "/api/revos/public/v1/log/message",

    "max_queue_size": 40,

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

parameters = {}

request = {}


def throttle(string):

    """
    Throttle
    Load test
    :param string:
    :return:
    """
    value = int(string)

    total = 0

    segment_block = 0

    registered_threads = {}

    total_char_count = len(catalog.chars) - 1

    iterations = math.ceil(value / 4)

    total_activity_count = len(catalog.activity) - 1

    for i in range(0, iterations):

        throttle_params = {}

        if segment_block > 0 and segment_block == CONFIG["max_queue_size"]:

            print("[DEBUG] Take a sip of coffee and relax...pausing %d seconds due to max block of threads..." %

                  CONFIG["sleep"])

            time.sleep(CONFIG["sleep"])

            segment_block = 0

        for entry in range(0, 4):

            if total >= value:

                continue

            telemetry_key_index = "TelemetryDataLog_" + str(entry + 1)

            now = datetime.datetime.now()

            throttle_params[telemetry_key_index] = "\t".join(
                [
                    str(total + 1),

                    catalog.chars[random.randint(0, total_char_count)],

                    now.strftime("%d/%m/%Y %H:%M:%S.%f")[:-3],

                    catalog.activity[random.randint(0, total_activity_count)]
                ]
            )

            registered_threads[total] = thread.ThreadRequest(params=throttle_params, headers=headers, config=CONFIG)
            registered_threads[total].start()

            total += 1
            segment_block += 1

parser = argparse.ArgumentParser(description="Load test runner for service log micro service.")
parser.add_argument("--entries",  help="Total activity requests",
                    required=True, type=throttle)
args = parser.parse_args()

exit()

