# Пары элементов
# Дан список чисел. Посчитайте, сколько в нем пар элементов,
# равных друг другу. Считается, что любые два элемента, равные
# друг другу образуют одну пару, которую необходимо посчитать.
# Входные данные - строка из чисел, разделенная пробелами.
# Выходные данные - количество пар.
# Важно: 1 1 1 - это 3 пары, 1 1 1 1 - это 6 пар
str_num = '2 2 2 2 4 5 6 6 6 6'
dct_str_num = {}
result_num = []
num_pairs = 0

for element in str_num.split():
    dct_str_num[element] = dct_str_num.get(element, 0) + 1

for val_ in dct_str_num.values():
    if val_ > 1:
        # формула подсчета пар
        # Кол-во пар = (всего элементов X всего элементов — 1) / 2
        result_num.append(val_ * ((val_ - 1) / 2))

for num in result_num:
    num_pairs += num
print(num_pairs)
