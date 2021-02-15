"""
    Task1. Оформите решение задач из прошлых домашних работ в функции.

    Напишите функцию runner. (все станет проще когда мы изучим модули,
    getattr и setattr)
    runner() – все фукнции вызываются по очереди
    runner(‘func_name’) – вызывается только функцию func_name.
    runner(‘func’, ‘func1’...) - вызывает все переданные функции

    Функции расположены в файле tasks.py
"""


def render(func_name, module):
    """Возвращение результата работы функции, найденной в заданном модуле

    :param func_name: str. Имя функции
    :param module: module.
    :return: Any. Результат работы функции
    """

    result = getattr(module, func_name)()
    print(result)
    return result


def runner(func=None):
    """Поиск имени функции в модуле, при его отсутствии - рендер всех функций,

    найденных в модуле

    :param func: str|None. Запрашиваемое имя функции если оно заданно,
    иначе None
    :return: None.
    """
    try:
        import tasks
    except ImportError as err:
        print(err)
        return

    if not func:
        functions = [task for task in dir(tasks)
                     if not task.startswith('__') and not task.endswith('__')]

        for func_name in functions:
            if callable(getattr(tasks, func_name)):
                render(func_name, tasks)
    elif func in dir(tasks):
        render(func, tasks)
    else:
        print("Function hasn't been found")


runner()
