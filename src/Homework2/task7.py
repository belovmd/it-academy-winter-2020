"""Все задачи взяты с сайта www.hackerrank.com"""


"""https://www.hackerrank.com/contests/it-academy-03/challenges/fizzbuzz-16-2
Напишите программу, которая считывает два натуральных числа a и b
(гарантируется, что a < b),
после чего для всех чисел от a до b выводит:
“Fizz”, если это число делится на 3;
“Buzz”, если это число делится на 5;
“FizzBuzz”, если выполнены оба предыдущих условия;
само это число в остальных случаях."""


number1 = int(input())
number2 = int(input())
for i in range(number1, number2 + 1):
    if number1 < number2 and i % 5 == 0 and i % 3 == 0:
        print("FizzBuzz")
        continue
    elif number1 < number2 and i % 5 == 0:
        print("Buzz")
        continue
    elif number1 < number2 and i % 3 == 0:
        print("Fizz")
        continue
    else:
        print(i)


""" https://www.hackerrank.com/contests/it-academy-03/challenges/1-n
Дано число n. Вывести квадрат каждого числа, предшествующего числу n,
не включая квадрат n"""


print('Вывести квадрыты чисел в интервале от 0 до 5, не включая 5')
n = 5
for number in range(n):
    print(number ** 2)


"""
https://www.hackerrank.com/contests/it-academy-01/challenges/
challenge-1961/problem
Напишите программу, вычисляющую по двум заданным
катетам гипотенузу прямоугольного треугольника"""


print('Вычислить по сторонам треугольника его гипотенузу')

side_one = 5
side_two = 12
hypotenuse = (side_one ** 2) + (side_two ** 2)

hypotenuse = (hypotenuse ** 1/2)

hypotenuse = round(hypotenuse, 11)
print(hypotenuse)


"""
https://www.hackerrank.com/contests/it-academy-03/challenges/nxn
Напишите программу, которая считывает строку, состояющую из целых чисел
(разделены пробелом)
и выводит только те числа, которые стоят на чётных индексах"""


counter = '1 3 5 8 12 4 5 812 '
string = counter.split()
for i in range(0, len(string), 2):
    print(string[i], end=' ')


"""https://www.hackerrank.com/contests/it-academy-03/challenges"""
"""Напишите программу, которая считывает
одно целое число N и выводит N строк,
содержащих N звёздочек в каждой строке
(без пробелов)"""


Number_ = 10
for i in range(Number_):
    print(Number_ * "*", end='\n')


"""https://www.hackerrank.com/contests/it-academy-03/challenges/
challenge-1988"""
"""Напишите программу, которая находит кота. В первой строке
пользователь вводит натуральное число - количество строк,
в последующих строках - сами строки.
Если хотя бы в одной введённой строке нашлось сочетание
букв «Cat» или «cat», программа выводит «MIAOW»,
иначе программа выводит «NO CAT»."""


num_ = int(input())

for i in range(num_):
    sentence = input()
    if 'Cat' in sentence or 'cat' in sentence:

        print('MIAOW')
    else:
        print('NO CAT')
