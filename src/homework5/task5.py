"""Бинарные операции:
   Написать программу которая находит ближайшую степень двойки
   к введенному числу. 10(8), 20(16), 1(1), 13(16)
   Задачу поместите в файл task5.py в папке src/homework5.
"""


def near_power(number):
    number = int(number)
    result = 1
    power_counter = 0
    while True:
        current_power_number = 2 << power_counter
        current_difference = abs(current_power_number - number)
        previous_difference = abs(result - number)
        if current_difference < previous_difference:
            result = current_power_number
            power_counter += 1
        else:
            return result


if __name__ == "__main__":
    n = int(input())
    print(near_power(n))
