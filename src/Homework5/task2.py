"""Создайте декоратор, который хранит результаты
   вызовов функции (за все время вызовов, не только
   текущий запуск программы).
"""


from datetime import datetime


# Функция для записи результата в файл
def write_result_to_file(result):
    titles_txt = open('task2_time.txt', 'a+', encoding='UTF-8')
    titles_txt.writelines(result)
    titles_txt.close()


# Декоратор для основной функции
def decorator_function(func):
    def wrapper(*args, **kwargs):
        write_result_to_file(f'Функция: {func.__name__}\n')
        write_result_to_file(f'Запущена:'
                             f'{datetime.now().strftime("%d.%m.%Y,%H:%M:%S")}')
        result = func(*args, **kwargs)
        write_result_to_file(f'\nРезультат: {result}\n\n')
    return wrapper


# Основная функция, которую декорируем
@decorator_function
def hello():
    return 'H_e_l_l_o___w_o_r_l_d_!'


hello()
