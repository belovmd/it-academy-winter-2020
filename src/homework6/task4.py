""" Task 3: Максимум функции Эйлера, Задача 69
Функция Эйлера, φ(n) [иногда ее называют фи-функцией] используется для
определения количества чисел, меньших n, которые взаимно просты с n.
К примеру, т.к. 1, 2, 4, 5, 7 и 8 меньше девяти и взаимно просты с
девятью, φ(9)=6.
"""

def gcd(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a

    return a


def totient_maximum(n):
    result = 1
    for i in range(2, n):
        if (gcd(i, n) == 1):
            result += 1
    return result


# Driver Code
for n in range(2, 11):
    print('n=', n, totient_maximum(n), n / totient_maximum(n))

# This code is contributed
# by Smitha
