""" Оформите решение задач из прошлых домашних работ в функции.
    Напишите функцию runner.
    a.	runner() – все фукнции вызываются по очереди
    b.	runner(‘func_name’) – вызывается только функцию func_name.
    c.	runner(‘func’, ‘func1’...) - вызывает все переданные функции
"""


import func_task1


def runner(*args):
    functions = [func_name for func_name in dir(func_task1)
                 if callable(getattr(func_task1, func_name))]
    if args:
        for func_name in args:
            print(f'Result {func_name} :')
            getattr(func_task1, func_name)()

    else:
        for func_name in functions:
            print(f'Result {func_name} :')
            getattr(func_task1, func_name)()


if __name__ == "__main__":

    runner()
    runner('func_1')
    runner('func_1', 'func_2', 'func_3')
