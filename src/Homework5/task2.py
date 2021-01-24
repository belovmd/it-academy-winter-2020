'''
Создайте декоратор, который хранит результаты вызовов функции
(за все время вызовов, не только текущий запуск программы)
'''


def counter(funck):
    count = [0]

    def call_counter():
        count[0] += 1
        return funck(), count[0]
    return call_counter


@counter
def decorator():
    return


print(decorator(), decorator(), decorator())
