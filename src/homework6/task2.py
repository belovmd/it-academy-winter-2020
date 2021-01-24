""" Task 2:
Создайте декоратор, который вызывает задекорированную функцию пока она не
выполнится без исключений (но не более n раз - параметр декоратора). Если
превышено количество попыток, должно быть возбуждено исключение типа
TooManyErrors.
"""


def retry(n):
    def decorator(func):

        def wrapped(*args, **kwargs):
            for attempt_number in range(0, n):
                result = func(*args, **kwargs)
            print('-')

            return result

        return wrapped
    return decorator


@retry
def division(number):
    return 1 / number


print(division(0))

