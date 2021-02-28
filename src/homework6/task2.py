import random


"""
    Task 2. Создайте декоратор, который вызывает задекорированную функцию
    пока она не выполнится без исключений (но не более n раз - параметр
    декоратора).
    Если превышено количество попыток, должно быть возбуждено исключение типа
    TooManyErrors
"""


class TooManyErrors(RuntimeError):
    pass


def errors_attempts(max_attempts):
    def dec(fun):
        attempts_count = 0

        def wrapper(*args, **kwargs):
            nonlocal attempts_count

            for _ in range(max_attempts + 1):
                try:
                    attempts_count += 1

                    if attempts_count > max_attempts:
                        raise TooManyErrors(
                            "You've reached the maximum attempts. "
                            "Please try again."
                        )

                    result = fun(*args, **kwargs)
                except TooManyErrors as err:
                    print(err)
                except ValueError as err:
                    print(f"attempt {attempts_count}: {err}")
                else:
                    return result

        return wrapper

    return dec


@errors_attempts(10)
def find_number(values):
    """В списке values находит случайную строку и преобразует ее в число

    В случае невозможности преобразования - выбрасывает исключение

    :param values: список строк
    :return: число.
    :raises: ValueError: если элемент списка не является числом
    """
    random_value = random.choice(values)
    try:
        return int(random_value), print("Number was found")
    except ValueError:
        raise ValueError("ValueError exception thrown")


list_of_values = ["two", "6", "run", "eight", "rose", "gold", "Italy"]
find_number(list_of_values)
