"""Создайте декоратор, который вызывает задекорированную функцию пока она не
    выполнится без исключений (но не более n раз - параметр декоратора). Если
    превышено количество попыток, должно быть возбуждено исключение типа
    TooManyErrors.
"""


class TooManyErrors(BaseException):
    pass


def decorator(shot):
    def my_dec(func):
        def wrapper(*args, **kwargs):
            nonlocal shot
            try:
                if not shot:
                    raise TooManyErrors
                else:
                    shot -= 1
                return func(*args, **kwargs)

            except TooManyErrors:
                print('Too many shots.')

        return wrapper

    return my_dec


@decorator(1)
def summation(a, b):
    return a + b


print(summation(2, 2))
print(summation(2, 3))
