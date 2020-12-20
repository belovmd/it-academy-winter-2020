'''
Пары элементов
Дан список чисел. Посчитайте, сколько в нем пар элементов,
равных друг другу. Считается, что любые два элемента,
равные друг другу образуют одну пару, которую необходимо посчитать.
Входные данные - строка из чисел, разделенная пробелами. 
Выходные данные - количество пар. 
Важно: 1 1 1 - это 3 пары, 1 1 1 1 - это 6 пар
'''
import math

dict_ = {}

for element in input('введите числа, разделенные пробелам: ').split():
    dict_[element] = dict_.get(element, 0) + 1
for values_ in dict_.values():
    if values_ > 1:
        result = (math.factorial(values_) // (math.factorial(values_ - 2) * 2))
#        print((math.factorial(value - 2) * 2))
#        print(math.factorial(value))
        # по формуле C == n! // (n - k)! * k!, где n - кол-во объектов,
        # k - пара объектов, C - кол-во комбинаций.
        print(result)
