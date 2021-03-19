"""Реализовать функцию get_ranges которая получает на
   вход непустой список неповторяющихся целых чисел,
   отсортированных по возрастанию, которая этот список
   “сворачивает”
   get_ranges([0, 1, 2, 3, 4, 7, 8, 10]) // "0-4,7-8,10"
   get_ranges([4, 7, 10]) // "4, 7, 10"
   get_ranges([2, 3, 8, 9]) // "2-3, 8-9"
"""


def get_ranges(a):
    b = []
    for i in range(1, len(a)):
        if a[i] > a[i - 1] + 1:
            if a[0] != a[i - 1]:
                b.append(f'{a[0]}-{a[i - 1]}')
                a[0] = a[i]
            else:
                b.append(f'{a[0]}')
                a[0] = a[i]
    if a[0] != a[-1]:
        b.append(f'{a[0]}-{a[-1]}')
    else:
        b.append(f'{a[-1]}')
    return ','.join(b)


print(get_ranges([0, 1, 2, 3, 4, 7, 8, 10]))
print(get_ranges([4, 7, 10]))
print(get_ranges([2, 3, 8, 9]))
