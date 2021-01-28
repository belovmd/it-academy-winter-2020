import os
from src.Homework5 import task1 as my_funcs


def runner(*args):

    if args:
        for function_ in args:
            my_func = getattr(my_funcs, function_)
            my_func()
            print('The function was called.')
    else:
        os.system('task1_import_file.py')
        print('All functions were called.')


if __name__ == '__main__':
    runner()
