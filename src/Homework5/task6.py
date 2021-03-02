'''
Вводится число найти его максимальный делитель,
являющийся степенью двойки. 10(2) 16(16), 12(4).
'''


def max_divisor(number):
    prev = 1
    for i in range(number):
        current = 1 << i
        if not number % current:
            prev = current
        if current >= number:
            print(prev)
            return prev


max_divisor(10)
max_divisor(16)
max_divisor(12)
