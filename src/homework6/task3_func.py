"""Оформите решение задач из прошлых домашних работ в функции. Напишите
    функцию runner. (все станет проще когда мы изучим модули,
    getattr и setattr).
    a. runner() – все фукнции вызываются по очереди
    b. runner(‘func_name’) – вызывается только функцию func_name.
    c. runner(‘func’, ‘func1’...) - вызывает все переданные функции
"""


from src.homework6 import task3_additional as my_funcs


def runner(*args):
    """Run other functions.

    :param args: functions' names.
    :return: None
    """
    funcs = []
    if args:
        for function_ in args:
            my_func = getattr(my_funcs, function_)
            my_func()
            print('The function was called.')
    else:
        for func in dir(my_funcs):
            if not func.startswith('__'):
                funcs.append(func)
        for f in funcs:
            my_func = getattr(my_funcs, f)
            my_func()
        print('All functions were called.')


if __name__ == '__main__':
    runner('__name__')
    runner('palindrome')
