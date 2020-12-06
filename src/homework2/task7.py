"""Зарегистрируйтесь на одном (или нескольких) из сайтов:
   https://py.checkio.org/, https://www.codewars.com
   https://www.hackerrank.com/,https://acmp.ru
   И решите 1-5 задач уровня Elementary и advanced
   Поместите 3 простых и 2 сложных задачи на Ваш выбор в пул реквест
"""


""" Task 1
    Требуется посчитать сумму целых чисел, 
    расположенных между числами 1 и N включительно.
    Входные данные
    В единственной строке входного файла INPUT.TXT
    записано единственное целое число N,
    не превышающее по абсолютной величине 104.
    Выходные данные
    В единственную строку выходного файла нужно вывести одно целое число —
    сумму чисел, расположенных между 1 и N включительно.
    
"""
a = int(input())
c = 0
if (a > 0) and (a <= 10 ** 4):
    s = (a + 1) * a // 2
elif (a <= 0) and (a > ((-1) * 10 ** 4)):
    s = (a + 1) * (abs(a) + 2 * (a <= 0)) // 2
sign = -1 if a <= 0 else 1
s = sum(range(1, a + sign, sign))
print(s)


""" Task 2
    Главный вождь племени Абба не умеет считать.
    В обмен на одну из его земель вождь другого племени
    предложил ему выбрать одну из трех куч с золотыми монетами.
    Но вождю племени Абба хочется получить наибольшее количество
    золотых монет. Помогите вождю сделать правильный выбор!
    Входные данные
    В первой строке входного файла INPUT.TXT записаны
    три натуральных числа через пробел. Каждое из чисел
    не превышает 10100. Числа записаны без ведущих нулей.
    Выходные данные
    В выходной файл OUTPUT.TXT нужно вывести одно целое число —
    максимальное количество монет, которые может взять вождь.
    
"""
a = int(input())
b = int(input())
c = int(input())
var = a, b, c <= 10 ** 100
gold = [a, b, c]
count = 0
for num in gold:
    if num > count:
        count = num
    if num > count:
        count = num
print(count)


""" Task 3
    По данному натуральному числу n ≤ 9 выведите лесенку из n ступенек,
    i-я ступенька состоит из чисел от 1 до i без пробелов.
    
"""
n = int(input())
s = 1
for element in range(1, n + 1):
    s += element
    for element_ in range(1, s):
        print(element_, end='')
    s = 1
    print()


""" Task 4
    Известны результаты каждой из 4х четвертей баскетбольной встречи.
    Нужно определить победителя матча.
    Входные данные
    Входной файл INPUT.TXT содержит 4 строки,
    в каждой строке находится два целых числа a и b – 
    итоговый счет в соответствующей четверти. 
    а – количество набранных очков за четверть первой командой,
    b – количество очков, набранных за четверть второй командой. 
    Выходные данные
    В выходной файл OUTPUT.TXT выведите номер выигравшей команды,
    в случае ничьей следует вывести «DRAW».
    
"""
result = sum(int(a) - int(b) for a, b in (input().split() for _ in range(4)))
print("DRAW" if not result else 1 if result > 0 else 2)


""" Task 5
    Группа программистов собралась в понедельник
    и на все свои деньги купила «Sprite» в бутылках емкостью по 0.25 л.,
    не забыв взять сдачу. Во вторник они сдали пустую посуду,
    добавили оставшуюся сдачу, вновь купили столько таких же бутылок «Sprite»,
    сколько могли. Так они действовали до пятницы. В пятницу, сдав посуду
    и добавив сдачу с четверга, они смогли купить только одну бутылку напитка.
    При этом денег у них уже не осталось. Требуется написать программу,
    определяющую минимальную сумму,
    которой располагали программисты в понедельник.
    Входные данные
    Входной файл INPUT.TXT состоит из единственной строки,
    содержащей два целых числа F (стоимость одной бутылки «Sprite»)
    и P (стоимость одной пустой бутылки из под «Sprite»),разделенных пробелом.
    Ограничения: 1 ≤ P < F ≤ 109, начальная сумма не превосходит 2×109.
    Выходные данные
    В единственную строку выходного файла нужно вывести одно целое число –
    минимальную сумму, которой располагали программисты в понедельник.
    
"""
F, P = map(int, input().split())


def f(Q, deep):
    if deep == 5:
        return Q
    for x in range(Q, Q * Q, F - P):
        if x == Q + (F - P) * (x // F):
            break
    return f(x, deep + 1)


print(f(F, 1))
