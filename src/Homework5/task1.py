'''
Оформите решение задач из прошлых домашних работ в функции.
Напишите функцию runner.
(все станет проще когда мы изучим модули, getattr и setattr)
runner() – все фукнции вызываются по очереди
runner(‘func_name’) – вызывается только функцию func_name.
runner(‘func’, ‘func1’...) - вызывает все переданные функции
'''

import funck


def runner(*args):
    if not args:
        funck.funck_1()
        funck.funck_2()
        funck.funck_3()
    else:
        for func_name in args:
            getattr(funck, func_name)()


runner()
runner('funck_1')
runner('funck_1', 'funck_2')
