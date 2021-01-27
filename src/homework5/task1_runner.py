"""Оформите решение задач из прошлых домашних работ в функции. Напишите
    функцию runner. (все станет проще когда мы изучим модули,
    getattr и setattr).
    a. runner() – все фукнции вызываются по очереди
    b. runner(‘func_name’) – вызывается только функцию func_name.
    c. runner(‘func’, ‘func1’...) - вызывает все переданные функции
"""


import os
from src.homework5 import task1_functions as my_funcs


def runner(*args):
    """Run other functions.

    :param args: functions' names.
    :return: None
    """
    if args:
        for function_ in args:
            my_func = getattr(my_funcs, function_)
            my_func()
            print('The function was called.')
    else:
        os.system('task1_functions.py')
        print('All functions were called.')


if __name__ == '__main__':
    runner()
    runner('palindrome')
