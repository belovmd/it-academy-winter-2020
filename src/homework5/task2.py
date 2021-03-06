"""Создайте декоратор, который хранит результаты вызовов функции
   (за все время вызовов, не только текущий запуск программы)
   Задачу поместите в файл task2.py в папке src/homework5.
"""


import datetime


def date_time(fun):
    def _wrapper(*args, **kwargs):
        print(f'Функция запущена: {datetime.datetime.now()}')
        result = fun(*args, **kwargs)
        with open('file_for_task2.txt', 'a') as file:
            file.writelines(f'result function call: {str(result)} \n')
            file.writelines(f'function started: {datetime.datetime.now()} \n '
                            f'\n')
        return result

    return _wrapper


@date_time
def add(a, b):
    return a + b


add(10, 20)
add(20, 30)
add(30, 40)
