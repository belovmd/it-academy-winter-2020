"""Оформите решение задач из прошлых домашних работ в функции.
   Напишите функцию runner.
   (все станет проще когда мы изучим модули, getattr и setattr)
   runner() – все фукнции вызываются по очереди
   runner(‘func_name’) – вызывается только функцию func_name.
   runner(‘func’, ‘func1’...) - вызывает все переданные функции
   Задачу поместите в файл task1.py в папке src/homework5.
"""


import src.homework5.taskFunctions


def runner(*args):
    publicProps = []
    for prop in dir(src.homework5.taskFunctions):
        if not prop.startswith('_'):
            publicProps.append(prop)
    for arg in (publicProps, args)[len(args) > 0]:
        print(arg + ' function result:')
        getattr(src.homework5.taskFunctions, arg)()


runner()
