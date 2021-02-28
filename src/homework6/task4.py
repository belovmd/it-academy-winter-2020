"""
    Task 463. Странные рекурсивные отношения

    Функция f определена для всех положительных целых аргументов следующим
    образом:

    f(1)=1
    f(3)=3
    f(2n)=f(n)
    f(4n+1)=2f(2n+1)−f(n)
    f(4n+3)=3f(2n+1)−2f(n)
    Функция S(n) определена как ∑ni=1f(i).

    S(8)=22 и S(100)=3604.

    Найдите S(337). В качестве ответа приведите последние 9 цифр полученного
    числа.
"""


class WeirdRecursion:
    def __init__(self):
        self.cached = {
            0: 0,
            1: 1,
            2: 2,
            3: 5,
        }

    def get(self, n):
        if n in self.cached:
            return self.cached[n]

        result = None
        div, mod = n // 4, n % 4

        if mod == 0:
            calc = 6 * self.get(2 * div) - 5 * self.get(div)
            result = calc - 3 * self.get(div - 1) - 1
        elif mod == 1:
            calc = 2 * self.get(2 * div + 1) + 4 * self.get(2 * div)
            result = calc - 6 * self.get(div) - 2 * self.get(div - 1) - 1
        elif mod == 2:
            calc = 3 * self.get(2 * div + 1) + 3 * self.get(2 * div)
            result = calc - 6 * self.get(div) - 2 * self.get(div - 1) - 1
        elif mod == 3:
            result = 6 * self.get(2 * div + 1) - 8 * self.get(div) - 1

        self.cached[n] = result
        return result


recursion_result = WeirdRecursion().get(3 ** 37)
print(recursion_result % 10 ** 10)
