"""https://acmp.ru/index.asp?main=task&id_task=146
  По заданному натуральному числу А требуется найти
  наибольшее число В такое, что B**2 ≤ A. 
"""


A = int(input())
B = 1

while B * B <= A:
   B += 1
print(B-1)
