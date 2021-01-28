"""Создайте декоратор, который хранит результаты вызовов функции
(за все время вызовов, не только текущий запуск программы)
"""

import logging


def setup_logging(name="logger",
                  filepath=None,
                  stream_log_level="DEBUG",
                  file_log_level="DEBUG"):
    _logger = logging.getLogger(name)
    _logger.setLevel("DEBUG")
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    ch = logging.StreamHandler()
    ch.setLevel(getattr(logging, stream_log_level))
    ch.setFormatter(formatter)
    _logger.addHandler(ch)
    if filepath is not None:
        fh = logging.FileHandler(filepath)
        fh.setLevel(getattr(logging, file_log_level))
        fh.setFormatter(formatter)
        _logger.addHandler(fh)
    return _logger


logger = setup_logging(name="default_log", filepath="logger.log")


def log_decorator(log_name):
    def log_this(function):
        _logger = logging.getLogger(log_name)

        def new_function(*args, **kwargs):

            _logger.debug(f"{function.__name__} - {args} - {kwargs}")
            output = function(*args, **kwargs)
            _logger.debug(f"{function.__name__} returned: {output}")
            return output
        return new_function
    return log_this
