"""https://acmp.ru/index.asp?main=task&id_task=7
Золото племени АББА.
Главный вождь племени Абба не умеет считать.
В обмен на одну из его земель вождь другого племени
предложил ему выбрать одну из трех куч с золотыми монетами.
Но вождю племени Абба хочется получить наибольшее количество золотых монет.
Помогите вождю сделать правильный выбор!"""
a = int(input())
b = int(input())
c = int(input())
gold = [a, b, c]
count = 0
for num in gold:
    if num > count:
        count = num
print(count)

# https://acmp.ru/index.asp?main=task&id_task=18. Факториал.
# Требуется вычислить факториал целого числа N.
# Факториал обозначают как N! и вычисляют по формуле:
# N! = 1 * 2 * 3 * … * (N-1) * N, причем 0! = 1.
n = int(input())
fact = 1
for i in range(1, n + 1):
    fact *= i
print(fact)

# Программа, которая преобразует номер телефона,
# введённого пользователем в защищённый вид.
# Должно быть выведено только 4 последние цифры номера телефона,
# остальные цифры закрыты звездочками.
telnumber = input()
if telnumber.isdigit() and len(telnumber) >= 8:
    stars_count = len(telnumber) - 4
    stars = "*" * stars_count
    print(stars + telnumber[-4:])
else:
    print("Ошибка")

# https://acmp.ru/index.asp?main=task&id_task=859. Сумма от 1 до N.
n = 8
summa = 0
for digit in range(1, n + 1):
    summa += digit

print(summa)

# https://acmp.ru/index.asp?main=task&id_task=171. Количество делителей.
n = int(input())
num_div = 0
for digit in range(1, n + 1):
    if (1 <= digit <= n) and n % digit == 0:
        num_div += 1

print(num_div)
