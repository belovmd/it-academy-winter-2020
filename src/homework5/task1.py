""" Оформите решение задач из прошлых домашних работ в функции.
    Напишите функцию runner.
    a.	runner() – все фукнции вызываются по очереди
    b.	runner(‘func_name’) – вызывается только функцию func_name.
    c.	runner(‘func’, ‘func1’...) - вызывает все переданные функции
"""


import func_task1


def runner(*args):
    if args:
        for func_name in args:
            getattr(func_task1, func_name)()

    else:
        func_task1.func_1()
        func_task1.func_2()
        func_task1.func_3()


if __name__ == "__main__":

    runner()
    runner('func_1')
    runner('func_1', 'func_2', 'func_3')
