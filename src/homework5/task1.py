""" Task 1: Модули и функции
Оформите решение задач из прошлых домашних работ в функции. Напишите функцию
runner. (все станет проще когда мы изучим модули, getattr и setattr)

a. runner() – все фукнции вызываются по очереди
b. runner(‘func_name’) – вызывается только функцию func_name.
c. runner(‘func’, ‘func1’...) - вызывает все переданные функции
"""

import src.homework5.func_for_task1.functions


def call_function(module, func):
    func = getattr(module, func)
    print(f'Call function with name: "{func.__name__}". Result: {func()}')


def runner(*args):
    _module = src.homework5.func_for_task1.functions
    # if args is empty - call all functions
    if not args:
        function_names = [name for name in dir(_module) if not name.startswith('__')]
        for func in function_names:
            call_function(_module, func)
        return

    for arg in args:
        if hasattr(_module, arg):
            call_function(_module, arg)
        else:
            print(f'No such function: "{arg}"')


if __name__ == "__main__":
    runner('count', 'abc', 'fibonacci')
    # runner()
