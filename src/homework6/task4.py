"""Проект Эйлера. https://euler.jakumo.org/problems/pg/1.html.
   Обобщите указанную задачу на свое усмотрение, решите ее, покройте тестами.
   Вариант 2. Задача 452. Примечание - там кортежи длины n, не числа.

   Define F(m,n) as the number of n-tuples of positive integers for which
   the product of the elements doesn't exceed m.
   F(10, 10) = 571.
   F(106, 106) mod 1 234 567 891 = 252903833.
   Find F(109, 109) mod 1 234 567 891.
"""


import math


def get(n):
    primes = []
    visited = [False] * (n + 1)
    for i in range(2, n + 1):
        if not visited[i]:
            primes.append(i)
            for j in range(i * i, n + 1, i):
                visited[j] = True
    return primes


class Prime:
    pass


class BinomialCoefficient:
    def __init__(self, mod):
        self.mod = mod
        self.cache = {}

    def get(self, n, m):
        if n not in self.cache:
            self.cache[n] = {}
        if m not in self.cache[n]:
            result = 1
            for i in range(1, m + 1):
                result = result * (n - i + 1) // i
            self.cache[n][m] = result % self.mod
        return self.cache[n][m]


class SieveAlgorithm:
    def __init__(self, n, mod):
        self.n = n
        self.mod = mod
        self.binomial_coefficient = BinomialCoefficient(mod)
        self.basic_primes = get(math.floor(math.sqrt(n)))
        self.solution_count_cache = {}

    def get_range(self, begin, end):
        if begin > end:
            return []
        number_list = [i for i in range(begin, end + 1)]
        result_list = []
        for i in range(begin, end + 1):
            result_list.append(1)
        for p in self.basic_primes:
            p_begin_pos = 0
            if begin % p != 0:
                p_begin_pos = p - (begin % p)
            for i in range(p_begin_pos, end - begin + 1, p):
                e = 0
                while number_list[i] % p == 0:
                    number_list[i] //= p
                    e += 1
                    result_list[i] = (
                        result_list[i] * self.__get_solution_count(e)
                    ) % self.mod
        for i in range(end - begin + 1):
            if number_list[i] > 1:
                result_list[i] = (result_list[i] * self.n) % self.mod
        return result_list

    def __get_solution_count(self, e):
        if e not in self.solution_count_cache:
            self.solution_count_cache[e] = \
                self.binomial_coefficient.get(self.n + e - 1, e)
        return self.solution_count_cache[e]


class Problem:

    def __init__(self, power):
        self.mod = 1234567891
        self.power = power
        self.solve()

    def solve(self):
        print(self.get(10 ** self.power, 10 ** self.power))

    def get(self, n, segment_count=1):
        assert (n % segment_count == 0)

        segment_len = n // segment_count
        sieve_algorithm = SieveAlgorithm(n, self.mod)
        total_count = 0
        for i in range(segment_count):
            solution_count_list = sieve_algorithm.get_range(
                i * segment_len + 1, (i + 1) * segment_len
            )
            count = sum(solution_count_list) % self.mod
            total_count = (total_count + count) % self.mod

        return total_count


Problem(1)
