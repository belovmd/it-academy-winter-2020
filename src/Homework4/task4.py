"""Даны два списка чисел. Посчитайте, сколько различных чисел входит только
   в один из этих списков
"""


s1 = [1, 2, 1, 1, 3, 4, 5, 8, 9]
s2 = [10, 10, 11, 1, 2, 6, 7]
a1 = []
a2 = []
s = []

for i in s1:
    if i not in a1:
        a1.append(i)
for j in s2:
    if j not in a2:
        a2.append(j)
for k in a1:
    if k in a2:
        s.append(k)
        a2.remove(k)
    else:
        s.append(k)
print(len(s))
