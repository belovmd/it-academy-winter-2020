"""Task 2: Декоратор
Создайте декоратор, который хранит результаты вызовов функции
(за все время вызовов, не только текущий запуск программы)
"""

from datetime import datetime
from time import sleep


def logger(func):
    inmemory_db = []

    def wrapped(*args, **kwargs):
        nonlocal inmemory_db
        result = func(*args, **kwargs)
        inmemory_db.append(result)
        print(inmemory_db)
        return result

    return wrapped


@logger
def get_current_time():
    """Получение текущего системного времени

    :return:
    """
    return datetime.now().time()


if __name__ == "__main__":
    print(get_current_time())
    sleep(1)  # функция sleep эмулирует выполнение некоторой работы

    print(get_current_time())
    sleep(2)

    print(get_current_time())
