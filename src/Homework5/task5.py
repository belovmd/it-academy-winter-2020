'''
Написать программу которая находит ближайшую степень
двойки к введенному числу. 10(8), 20(16), 1(1), 13(16)
'''


num = int(input())
num_2 = 2
while num_2 <= num:
    num_2 *= 2
n = num_2 // 2

if num_2 - num > num - n:
    print(n)
else:
    print(num_2)
