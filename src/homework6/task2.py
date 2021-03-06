# Создайте декоратор, который вызывает задекорированную
# функцию пока она не выполнится без исключений (но не
# более n раз - параметр декоратора). Если превышено
# количество попыток, должно быть возбуждено исключение
# типа TooManyErrors
import random


class TooManyErrors(BaseException):
    pass


def my_dec(func):
    total_attempts = 5

    def wrapper(*args, **kwargs):
        with open('trying_to_guess_task2', 'r') as fh:
            trying_to_guess = fh.readline()
        try:
            if int(trying_to_guess) > total_attempts:
                raise TooManyErrors('Превышено количество попыток!')
            else:
                print(f'Попытка №{trying_to_guess}. '
                      f'Всего попыток {total_attempts}')

            trying_to_guess = int(trying_to_guess) + 1
            with open('trying_to_guess_task2', 'w') as file:
                file.write(str(trying_to_guess))
        except TooManyErrors:
            with open('trying_to_guess_task2', 'w') as file:
                file.write('1')
            print("Превышено количество попыток!")
        result = func(*args, **kwargs)

        return result

    return wrapper


"""Пользователь загадывает число в диапазоне от 1 до 10.
Функция пытается его угадать"""


def random_():
    random_num = random.randrange(1, 10)
    return random_num


@my_dec
def guess(user_number):
    if user_number not in range(1, 10):
        raise TypeError('Неверный тип данных!')
    else:
        computer_number = random_()
        print(f'Число пользователя {user_number}')
        print(f'Число компьютера {computer_number}')
        if user_number == computer_number:
            return print('Угадал!')
        else:
            print('Не угадал!')
            raise ValueError
