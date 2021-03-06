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
            file.writelines(f'result function call: {str(func_result)} \n')
            file.writelines(f'function started: {datetime.datetime.now()} \n \n')
        return result

    return _wrapper


global func_result


@date_time
def add(a, b):
    global func_result
    func_result = a + b
    return func_result


add(10, 20)
add(20, 30)
add(30, 40)
