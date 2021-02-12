# Написать программу которая находит ближайшую
# степень двойки к введенному числу. 10(8), 20(16), 1(1), 13(16)
def degree_search(num):
    search_num = 2

    while num > search_num:
        search_num = search_num << 1

    if search_num - num > abs((search_num >> 1) - num):
        search_num = search_num >> 1
    else:
        pass

    return search_num
