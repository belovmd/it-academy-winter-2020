# 7. Зарегистрируйтесь на одном (или нескольких) из сайтов:
# https://checkio.org/, https://www.codewars.com, https://www.hackerrank.com/,
# https://acmp.ru И решите 1-5 задач уровня Elementary и advanced.
# Поместите 3 простых и 2 сложных задачи на Ваш выбор в пул реквест.


# https://acmp.ru/index.asp?main=task&id_task=148
# Даны два натуральных числа A и B. Требуется найти их НОД.
a = 12
b = 42

while a != 0 and b != 0:
    if a > b:
        a = a % b
    else:
        b = b % a

if a == 0:
    print('НОД: ' + str(b))
else:
    print('НОД: ' + str(a))

# https://acmp.ru/index.asp?main=task&id_task=46
# Выведите в выходной файл округленное до n знаков после десятичной
# точки число E. Е в точности равно 2.7182818284590452353602875.
e = str(2.7182818284590452353602875)
print(e)
n = int(input('До какого N округлить? '))
m = n + 2  # переменная, для учитывания целой части числа "2."

if n == 0:
    e = 3
else:
    e = e[0:m]

print(e)

# https://acmp.ru/index.asp?main=task&id_task=574
# Cтрока S1 называется анаграммой строки S2, если она получается из S2
# перестановкой символов. Даны строки S1 и S2. Напишите программу,
# которая проверяет, является ли S1 анаграммой S2.
str1 = 'GGIF'
str2 = 'IGGF'
str1 = sorted(str1)
str2 = sorted(str2)

if str1 == str2:
    print('yes')
else:
    print('no')

# https://acmp.ru/index.asp?main=task&id_task=77
# Для заданных натуральных чисел N и K требуется вычислить количество
# чисел от 1 до N, имеющих в двоичной записи ровно K нулей.
str_ = "8 1"

_nums = str_.split(' ')
N = int(_nums[0])
K = int(_nums[1])
all_bins = []
output_bins = []

for i in range(1, N):
    all_bins.append(str(bin(i))[2:])

    if str(bin(i))[2:].count('0') == K:
        output_bins.append(str(bin(i))[2:])

print('Все числа: ')
print(all_bins)

print('Числа с нулями: ')
print(output_bins)

print('Чисел с нулями всего: ' + str(len(output_bins)))

# https://acmp.ru/index.asp?main=task&id_task=146
# По заданному натуральному числу А требуется найти наибольшее число В
# такое, что B2 ≤ A.
a = 17
b = 0
for num in range(a):
    if num ** 2 < a:
        b += 1

"Цикл заканчивает свою работу на значении +1 от искомого результата квадрата"

b -= 1
print(b)
