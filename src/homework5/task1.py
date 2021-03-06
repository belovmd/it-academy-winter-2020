"""Оформите решение задач из прошлых домашних работ в функции.
   Напишите функцию runner.
   (все станет проще когда мы изучим модули, getattr и setattr)
   runner() – все фукнции вызываются по очереди
   runner(‘func_name’) – вызывается только функцию func_name.
   runner(‘func’, ‘func1’...) - вызывает все переданные функции
   Задачу поместите в файл task1.py в папке src/homework5.
"""


import src.homework5.task_functions


def runner(*args):
    public_props = []
    for prop in dir(src.homework5.task_functions):
        if not prop.startswith('__') and callable(prop):
            public_props.append(prop)
    for arg in (public_props, args)[len(args) > 0]:
        print(arg + ' function result:')
        getattr(src.homework5.task_functions, arg)()


runner()
