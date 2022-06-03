# Logging Basics

"""
DEBUG
INFO
WARNING
ERROR
CRITICAL
"""

import logging


def test():
    print(30*'-')
    level = logging.getLevelName(logging.getLogger().getEffectiveLevel())
    print(f"Log Level: {level}")
    logging.debug("Debug Message Here")
    logging.info("Info Message Here")
    logging.warning("Warning Message Here")
    logging.error("Error  Message Here")
    logging.critical("Critical  Message Here")
    print(30*'-')


test()

#  Set to Debug
print('-------------- Changing the log level ------------------')
root_log = logging.getLogger()
root_log.setLevel(logging.DEBUG)

print("---------- After changing the log level ------------")

test()


print("---------- Log into a file ------------")
handler = logging.FileHandler("logs.txt")
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')

handler.setFormatter(formatter)
root_log.addHandler(handler)

test()
