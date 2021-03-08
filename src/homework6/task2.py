""" Task 2:
Создайте декоратор, который вызывает задекорированную функцию пока она не
выполнится без исключений (но не более n раз - параметр декоратора). Если
превышено количество попыток, должно быть возбуждено исключение типа
TooManyErrors.
"""


class TooManyErrors(Exception):
    ...


def retry(max_retry_number=2):
    def decorator(func):

        def wrapped(*args, **kwargs):
            nonlocal max_retry_number

            while max_retry_number != 0:
                try:
                    result = func(*args, **kwargs)
                    return result
                except Exception:
                    max_retry_number -= 1

            raise TooManyErrors('Превышено количество попыток')

        return wrapped

    return decorator


@retry(10)
def division():
    print('Try to 1/0')
    return 1 / 0  # set 1/0 and run program


print(division())
