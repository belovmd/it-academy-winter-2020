"""Пары элементов
   Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
   Считается, что любые два элемента, равные друг другу образуют одну пару,
   которую необходимо посчитать.
   Входные данные - строка из чисел, разделенная пробелами. 
   Выходные данные - количество пар. 
   Важно: 1 1 1 - это 3 пары, 1 1 1 1 - это 6 пар
"""

str = '1 1 1 1'
old_list = str.split()

for i in old_list:
    n = old_list.count(i)
    if n > 0:
        all_pairs = (n * (n - 1)) / 2
print (int(all_pairs))

# Формула для получения возможного количества пар из общего числа:
# Количество пар = (Общее число элементов X (Общее число элементов — 1)) / 2
         

        

