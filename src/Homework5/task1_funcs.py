"""1)Напишите программу, которая считает общую цену.
   Вводится M рублей и N копеек цена, а также количество
   S товара Посчитайте общую цену в рублях и копейках за
   L товаров. 
   Пример: 
   Input: Цена одной вещи 3 рубля 20 копеек, посчитать
   3 предмета. 
   Output: Общая цена 9 рублей 60 копеек
"""


def total_cost():
    rubles, penny, quantity = 3, 20, 3
    cost = (rubles * 100 + penny) * quantity
    return f'Общая стоимость: {cost // 100} рублей {cost % 100} копеек'


"""2) FizzBuzz 
   Напишите программу, которая печатает цифры от 1 до
   100, но вместо чисел, кратных 3 пишет Fizz, вместо
   чисел кратный 5 пишет Buzz, а вместо чисел одновременно
   кратных и 3 и 5 - FizzBuzz
"""


def fizzbuzz():
    number = 0
    limitation = 15

    while number < limitation:
        number += 1
        if number % 15 == 0:
            return print('FizzBuzz')
        elif number % 5 == 0:
            return 'Buzz'
        elif number % 3 == 0:
            return 'Fizz'
        else:
            return number


"""3)Оглянемся назад. Числа
   Даны два натуральных числа. Вычислите их НОД при помощи
   алгоритма Евклида (мы не знаем функции и рекурсию).
"""


def gcd_num():
    number1, number2 = abs(64), abs(- 32)
    while number1 != number2:
        if number1 > number2:
            number1 = number1 - number2
        else:
            number2 = number2 - number1
    return number1
