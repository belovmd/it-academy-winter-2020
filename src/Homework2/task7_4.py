"""https://acmp.ru/index.asp?main=task&id_task=171
   Пусть X — натуральное число. Назовем Y его
   делителем, если 1 ≤ Y ≤ X и остаток от деления X
   на Y равен нулю. Задано число X.
   Найдите количество его делителей.
"""

x = int(input())
m = 0

for i in range(1, x + 1):
    if x % i == 0:
        m += 1
if m > 0:
    print(m)
