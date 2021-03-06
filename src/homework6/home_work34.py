string_num = '1 1 2 2 3 3 3 4 4 4 4'


def home_work():
    lst = string_num.split()
    pairs = 0
    numbers = {element: string_num.count(element) for element in lst}
    for key in numbers:
        num = 0
        while num < numbers[key] - 1:
            num += 1
            pairs += num
    print(pairs)


home_work()
