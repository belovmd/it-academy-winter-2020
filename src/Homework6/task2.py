"""Создайте декоратор, который вызывает задекорированную функцию пока
   она не выполнится без исключений (но не более n раз - параметр декоратора).
   Если превышено количество попыток, должно быть возбуждено исключение
   типа TooManyErrors
"""

class TooManyErrors(Exception):
    print("TooManyErrors: the function is called more times.")


# Декоратор для основной функции
def decorator_function(func, try_count=5):
    func.__count_run__ = 0  # добавили переменную в функцию

    def wrapper(*args, **kwargs):
        result = None
        while result == 'Incorrect run' or func.__count_run__ == 0\
                and func.__count_run__ <= try_count:
            result = func(*args, **kwargs)
            if result != 'Incorrect run':
                return result
            func.__count_run__ += 1
        else:
            raise TooManyErrors

    return wrapper


# Основная функция, которую декорируем
@decorator_function
def division_func(number1, number2):
    try:
        result = number1 / number2
        return result
    except Exception:
        return 'Incorrect run'


print(division_func(6, 2))
print(division_func(5, 0))
