# Вводится число найти его максимальный делитель,
# являющийся степенью двойки. 10(2) 16(16), 12(4).
def degree_search(num):
    search_num = 1

    while num >= search_num and not num % search_num:
        search_num = search_num << 1

    return search_num >> 1
