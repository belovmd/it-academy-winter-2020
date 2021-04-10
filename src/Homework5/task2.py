'''
Создайте декоратор, который хранит результаты вызовов функции
(за все время вызовов, не только текущий запуск программы)
'''

import datetime


def my_decor(func):
    counter = 0

    def wrapper(*args, **kwargs):
        nonlocal counter

        today = datetime.datetime.today()
        counter += 1
        print(f'{today}, {counter}')

        with open('Counter.txt', 'a') as file:
            file.write(f'{today}, name: my_func, {counter}\n')

        return today

    return wrapper


@my_decor
def my_fync():
    pass


my_fync()
my_fync()
