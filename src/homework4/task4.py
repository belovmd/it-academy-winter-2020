"""
    Task 4. Даны два списка чисел. Посчитайте, сколько различных чисел входит
    только в один из этих списков.
"""


list1 = [3, 6, 22, 95, 16]
list2 = [87, 22, 5, 6, 0]

result = set(list1) - set(list2)

print(result)
print(f"Количество различных чисел входящих только в один список - "
      f"{len(result)}")
