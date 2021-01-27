empty_symbol = ' '
cut_line_post = '...'
separator = ' | '
hist_symbol = '.'
lines_separator = '\n'
value_multiplier = 10


# генерируем строку, которые потом запишем в файл
def build(values, labels, max_label_length=30):
    result = ''
    for index in range(len(values)):
        label = __get_label__(labels[index], max_label_length)
        value = hist_symbol * int(float(values[index]) * value_multiplier)
        # полная строка гистограммы
        line = label + separator + value + values[index] + lines_separator
        result += line
    return result


# если длина названия фильмов больше чем заданная(30 в нашем случае),
# то мы обрезаем его и дописываем в конце троеточие, делается это,
# что гистограмма была на одном уровне на каждой строке
# иначе, если напротив - меньше чем заданная, до добавляем туда прбелов,
# чтобы вышло тоже 30
def __get_label__(label, max_label_length):
    if len(label) > max_label_length:
        return label[0:max_label_length - len(cut_line_post)] + cut_line_post
    else:
        return label + empty_symbol * (max_label_length - len(label))
