"""Создайте декоратор, который хранит результаты вызовов функции
(за все время вызовов, не только текущий запуск программы)
"""

import logging

log_file = "./logfile.log"
log_level = logging.DEBUG
logging.basicConfig(level=log_level, filename=log_file, filemode="w+",
                    format="%(asctime)-15s %(levelname)-8s %(message)s")
logger = logging.getLogger("Function_logging")


def wrap(begin, end):
    def decorate(func):
        def call(*args, **kwargs):
            begin(func)
            result = func(*args, **kwargs)
            end(func)
            return result
        return call
    return decorate


def entering(func):
    logger.debug("Entered %s", func.__name__)


def exiting(func):
    logger.debug("Exited  %s", func.__name__)


@wrap(entering, exiting)
def logging_function(amount):
    print("entered the function" % amount)
