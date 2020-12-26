"""
    Task 2. List practice


    Task 2-1. Используйте генератор списков чтобы получить следующий:
    ['ab', 'ac', 'ad', 'bb', 'bc', 'bd']
"""
str_ = "abcd"
list_ = [symbol1 + symbol2 for symbol1 in str_[:2] for symbol2 in str_[1:]]
print("2-1", list_)


"""
    Task 2-2. Используйте на предыдущий список slice чтобы получить следующий:
    ['ab', 'ad', 'bc']
"""
print("2-2", list_[::2])


"""
    Task 2-3. Используйте генератор списков чтобы получить следующий:
    ['1a', '2a', '3a', '4a']
"""
num_list = [f"{num}a" for num in range(1, 5)]
print("2-3", num_list)


"""
    Task 2-4. Одной строкой удалите элемент '2a' из прошлого списка и
    напечатайте его
"""
el_position = num_list.index("2a")
el = num_list.pop(el_position)
print("2-4", el, num_list)


"""
    Task 2-5. Скопируйте список и добавьте в него элемент '2a' так чтобы в
    исходном списке этого элемента не было.
"""
num_list_copied = num_list[:]
num_list_copied.insert(el_position, el)
print("2-5", num_list, num_list_copied)
