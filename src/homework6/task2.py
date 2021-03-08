"""Создайте декоратор, который вызывает задекорированную функцию пока она
   не выполнится без исключений (но не более n раз - параметр декоратора).
   Если превышено количество попыток, должно быть возбуждено
   исключение типа TooManyErrors
"""


class TooManyErrors(Exception):
    pass


def decorators(tries, success_on_try=-1):
    def inner(func):
        def wrapper(*fn_args):
            for iter_ in range(tries):
                if iter_ == success_on_try - 1:
                    print(f"Try {iter_ + 1}: "
                          f"function successfully completed!")
                    return func(*fn_args)
                try:
                    func(*fn_args)
                except Exception:
                    print(f'Try {iter_ + 1}: exception catched!')
                else:
                    print(f"Try {iter_ + 1}: "
                          f"function successfully completed!")
                    return func(*fn_args)
            raise TooManyErrors(f"{tries} attempts consumed")

        return wrapper

    return inner


@decorators(5)
def divider(num):
    return 100 / num


counter = 0


@decorators(10, 7)
def errors_factory(num):
    return num / 0


dialog = input('Enter 1 to test divider(5),\nEnter 2 to test divider(0),\n'
               'Enter 3 to test errors_factory(100500):\n')

if dialog == '1':
    divider(5)
if dialog == '2':
    divider(0)
if dialog == '3':
    errors_factory(100500)
