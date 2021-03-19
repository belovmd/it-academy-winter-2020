"""Оформите решение задач из прошлых домашних работ
   в функции. Напишите функцию runner. (все станет
   проще когда мы изучим модули, getattr и setattr)
   a. runner() – все фукнции вызываются по очереди
   b. runner(‘func_name’) – вызывается только функцию
   func_name.
   c. runner(‘func’, ‘func1’...) - вызывает все
   переданные функции
"""

import task1_funcs


def runner(*args):
    list_func = [elem for elem in dir(task1_funcs)
                 if callable(getattr(task1_funcs, elem))]
    if not args:
        for elem in list_func:
            print(getattr(task1_funcs, elem)())
    else:
        for el in args:
            try:
                print(getattr(task1_funcs, el))
            except AttributeError:
                print(f'Нет такой {el} функции.')


runner()
print('\n')
runner('fizzbuzz()')
print('\n')
runner('total_cost()', 'gcd_num()')
