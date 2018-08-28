from revos.thread.cluster import Cluster
from revos.util.logging import Logging

"""
default settings
"""
MAX_DEFAULT_CLIENTS = 15         # Create as many containers as in MAX_DEFAULT_CLIENTS

AWAIT_THREAD_COMPLETE = False    # Thread container block others from start working while working

PATH_DOCKER_BIN = "/usr/local/bin/docker"   # Path to docker binary

THREAD_CONTAINER_COMMANDS = (   # Container commands sequence (after create)
                                # Lineal arguments like %name needs to be replaced
    "run --name %name -d -it e2e bash launch.sh %name",

    "exec %name bash linkuser.sh",

    "exec %name bash runner.load.test.sh"
)

THREAD_COMMAND_SLEEP = True       # Do a pause between container commands

THREAD_COMMAND_PAUSE_SECONDS = 5  # If pause number of seconds between container commands

"""
end default settings
"""

threads = {}

Logging.log("Provided setting for blocking threads: $setting"

          .replace("$setting", str(THREAD_COMMAND_SLEEP)))

Logging.log("Provided setting for blocking threads (sleep): $setting"

          .replace("$setting", str(THREAD_COMMAND_PAUSE_SECONDS)))

#
# """
# Create default containers
# """
for i in range(0, MAX_DEFAULT_CLIENTS):

    Logging.log("Creating container $id".replace("$id", str(i + 1)))

    threads[i] = Cluster(container_id=i, thread_container_commands=THREAD_CONTAINER_COMMANDS)
    threads[i].start()

    if AWAIT_THREAD_COMPLETE:
        threads[i].join()


