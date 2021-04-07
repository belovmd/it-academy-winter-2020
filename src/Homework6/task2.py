"""
Task 2. Создайте декоратор, который вызывает задекорированную функцию
пока она не выполнится без исключений (но не более n раз - параметр
декоратора).
Если превышено количество попыток, должно быть возбуждено исключение типа
TooManyErrors
"""


class TooManyErrors(RuntimeError):

    pass


def dec(func):
    total_count = 0
    def wrapper(namb):

        nonlocal total_count
        for _ in range(namb + 1):
            total_count += 1
            try:
                if total_count > namb:
                    raise TooManyErrors(f'TooManyErrors. {namb}')
                else:
                    print(f'выполнино: {total_count}')
            except TooManyErrors as err:
                print(err)

    return wrapper


@dec
def func(x):

    pass


func(6)
