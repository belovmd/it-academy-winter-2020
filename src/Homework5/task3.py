'''
Реализовать функцию get_ranges которая получает на
вход непустой список неповторяющихся целых чисел,
отсортированных по возрастанию, которая этот список “сворачивает”
 get_ranges([0, 1, 2, 3, 4, 7, 8, 10]) // "0-4,7-8,10"
 get_ranges([4,7,10]) // "4,7,10"
 get_ranges([2, 3, 8, 9]) // "2-3,8-9"
 '''


def get_ranges(lst):
    result = ''
    prev_n = None
    lenght = len(lst)

    for i, n in enumerate(lst):

        if prev_n is None:
            prev_n = n
            result = str(n)
            continue

        if prev_n + 1 == n:
            if i + 1 == lenght:
                result += f'-{n}'
                break
            prev_n = n
            continue

        else:
            result += f'-{prev_n},{n}'
            prev_n = n

    return result


arr = [0, 1, 2, 3, 4, 7, 8, 10]
res = get_ranges(arr)
print(res)
