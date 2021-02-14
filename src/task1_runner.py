"""
1. Оформите решение задач из прошлых домашних работ в функции.
Напишите функцию runner.
(все станет проще когда мы изучим модули, getattr и setattr)
runner() – все фукнции вызываются по очереди
runner(‘func_name’) – вызывается только функцию func_name.
runner(‘func’, ‘func1’...) - вызывает все переданные функции
"""

import task1_functions


def runner(*args):
    input = {
        'pairs': '1 1 2 2 67 67 1 1 2',
        'unique': [2, 2, 'abc', 79, 'k', 1, 67, 'k'],
        'order': [1, 45, 67, 43, 43, 43, 0, 7, 0, 4]
    }

    function = []
    [function.append(elem) for elem in dir(task1_functions) if callable(getattr(task1_functions, elem))]
    if args:
        for elem in args:
            callable(getattr(task1_functions, elem)(input.get(elem)))
    else:
        for elem in function:
            callable(getattr(task1_functions, elem)(input.get(elem)))


if __name__ == '__main__':
    runner()
    runner('pairs')
    runner('pairs', 'unique', 'order')
