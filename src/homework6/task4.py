""" Task 4: Максимум функции Эйлера


"""


def totient_maximum(max_value):
    func_max_value = 0
    result_number = 0

    for n in range(2, max_value):

        result = n

        p = 2
        while p * p <= n:

            if n % p == 0:
                while n % p == 0:
                    n = n // p
                result = result * (1.0 - (1.0 / float(p)))
            p = p + 1

        if n > 1:
            result = result * (1.0 - (1.0 / float(n)))
        print(n, result, n/ result)
        if n / result > func_max_value:
            func_max_value = n / result
            result_number = n

    return result_number

print(totient_maximum(10))