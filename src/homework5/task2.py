# Создайте декоратор, который хранит результаты вызовов функции
# (за все время вызовов, не только текущий запуск программы)
import time


def my_dec(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        func_time = time.time() - start_time
        with open('save_file_for_task2', 'a') as file:
            file.writelines(f"функции sum_num: {str(func_result)}, "
                            f"время выполнения {func_time} \n")
        return result

    return wrapper


@my_dec
def sum_num(a, b):
    global func_result
    func_result = a + b
    return func_result


print(sum_num(4, 5))
print(sum_num(5, 7))
print(sum_num(2, 9))
print(sum_num(33, 11))
print(sum_num(100, 500))


req_num = 5
with open('save_file_for_task2') as f:
    for i, line in enumerate(f, 1):
        if i == req_num:
            break
print(f'{str(req_num)} результат вызова {str(line)}')
