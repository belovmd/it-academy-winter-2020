'''
Написать программу которая находит ближайшую степень
двойки к введенному числу. 10(8), 20(16), 1(1), 13(16)
'''


def nearest_pow2(numb):
    current, prev = 0, 0
    for i in range(numb):
        current = numb - (1 << i)
        if current > 0:
            prev = current
        else:
            nearest = numb + -current if -current < prev else numb - prev
            print(nearest)
            return nearest


nearest_pow2(10)
nearest_pow2(16)
nearest_pow2(1)
nearest_pow2(13)
