"""https://acmp.ru/index.asp?main=task&id_task=2
   Требуется посчитать сумму целых чисел,
   расположенных между числами 1 и N включительно.
"""

n = int(input('Введите целое число: '))
s = 0

for i in range(2, n):
    if n % 1 == 0:
        s += i
if n > 0:
    print(s)
