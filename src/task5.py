"""
Написать программу которая находит
ближайшую степень двойки к введенному
числу. 10(8), 20(16), 1(1), 13(16)
"""


def power_two(num):
    if num <= 0:
        return False
    n = 0
    while num >> n > 0:
        n += 1
    return (1 << n) if abs((1 << n) - num) < abs((1 << (n - 1)) - num) \
        else (1 << (n - 1))


print(power_two(10))
print(power_two(20))
print(power_two(1))
print(power_two(13))
