import datetime
from threading import Thread


class Cluster(Thread):

    """
    Thread create docker container (client)
    With prefixed name
    """

    def __init__(self,

                 container_id=None,

                 thread_container_commands=None,

                 prefix="default-container-",

                 docker_bin="/usr/local/bin/docker"):

        """
        :param container_id:
        :param prefix:
        :return:
        """

        Thread.__init__(self)

        self.id = container_id
        self.prefix = prefix
        self.name = prefix + str(id)
        self.docker_bin = docker_bin
        self.cmd = thread_container_commands

    def run(self):

        """
        :return:
        """

        for _ in self.cmd:

            print("[DEBUG] {now} - {debug}".format(

                " ".join([self.docker_bin, _])

                , datetime.datetime.now()))

