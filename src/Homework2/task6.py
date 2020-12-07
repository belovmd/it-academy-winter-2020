"""Определите, является ли число палиндромом
(читается слева направо и справа налево одинаково).
  Число положительное целое, произвольной длины"""


# Этот вариант делал для себя через строки-)))

number = int(input("введите число: "))
int_number = int(number)
reverse_num = (str(number)[::-1])
int_reversed = int(reverse_num)
print(reverse_num)
for number in range(1):
    if int_number == int_reversed:
        print("Полиндром")
    else:
        print("Не Полиндром")
