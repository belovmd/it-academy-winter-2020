'''
Проект Эйлера. https://euler.jakumo.org/problems/pg/1.html.
Обобщите указанную задачу на свое усмотрение,
решите ее, покройте тестами.
Задача 17
Если записать числа от 1 до 5 английскими словами
(one, two, three, four, five), то используется
всего 3 + 3 + 5 + 4 + 4 = 19 букв.
Сколько букв понадобится для записи всех чисел
от 1 до 1000 (one thousand) включительно?
'''

nums = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    21: 'twenty-one',
    22: 'twenty-two',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety',
}


def gen(n, dic):
    s = str(n)
    if dic.get(n, False):
        return dic[n]
    elif n < 100:
        tr = n - int(s[1])
        return dic[tr] + dic[int(s[1])]
    elif n < 1000:
        if s[1:3] == '00':
            return dic[int(s[0])] + 'hundret'
        else:
            return dic[int(s[0])] + 'hundretand' + gen(int(s[1:3]), nums)
    elif n == 1000:
        return 'onethousand'


num = 0
for i in range(1, 1000):
    num += len(gen(i, nums))
print(num)
