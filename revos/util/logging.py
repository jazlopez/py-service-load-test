import datetime


class Logging(object):

    def __init__(self):

        """

        :return:
        """

    @staticmethod
    def log(entry):

        """
        Default log (custom)
        :param entry
        """

        print("[DEBUG] - {now} - {debug}".format(now=datetime.datetime.now(), debug=entry))

