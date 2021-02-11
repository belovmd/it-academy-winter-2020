'''
Создайте декоратор, который хранит результаты вызовов функции
(за все время вызовов, не только текущий запуск программы)
'''

import time


def count(func):
    def wrapper(*args, **kwargs):
        wrapper.num += 1
        print(f'вызов: {wrapper.num}')
        return func(*args, **kwargs)
    wrapper.num = 0
    return wrapper


def time_(func):
    def func_time():
        start_time = time.perf_counter()
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f'Время выполнена: {run_time:.8f} сек')
    return func_time


@count
@time_
def call():
    return


call(), call(), call()
