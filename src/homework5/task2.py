"""Task 2: Декоратор
Создайте декоратор, который хранит результаты вызовов функции
(за все время вызовов, не только текущий запуск программы)
"""

from datetime import datetime
from time import sleep


def logger(func):

    def wrapped(*args, **kwargs):
        with open('py_log.txt', mode='a') as f:
            result = func(*args, **kwargs)
            f.write(f'Result: {result}\n')
        return result

    return wrapped


@logger
def get_current_time():
    """Получение текущего системного времени

    :return: datetime.time. Текущее время в формате HH:MM:SS.
    """
    sleep(1)  # do something
    return datetime.now().time()


if __name__ == "__main__":
    for _ in range(3):
        print(get_current_time())
