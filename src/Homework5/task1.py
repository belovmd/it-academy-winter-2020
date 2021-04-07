'''
    Оформите решение задач из прошлых домашних работ в функции.
    Напишите функцию runner. (все станет проще когда мы
    изучим модули, getattr и setattr)
    a. runner() – все фукнции вызываются по очереди
    b. runner(‘func_name’) – вызывается только функцию func_name.
    c. runner(‘func’, ‘func1’...) - вызывает все переданные функции
'''


import function


def runner(*args):

    if not args:
        function.task_1()
        function.task_2()
        function.task_3()
    else:
        for func_name in args:
            getattr(function, func_name)()


runner()
runner('task_1', 'task_2')
runner('task_2')
