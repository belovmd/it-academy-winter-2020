"""
Найти самое длинное слово в введенном предложении. 
Учтите что в предложении есть знаки препинания.
"""
sentence = input('введите предложение: ')

def longest_word(sentence, punctuation = ',.?!:;"()-'):
    for symbol in punctuation:
        sentence = sentence.replace(symbol, '')  
        # убираем из предложения символы пунктуации
    words = sentence.split(' ')  
    # разделяем предложение на слова
    longest_word = ''

    for word in words:
        if not word.isalpha(): 
            # проверяет, состоит ли слово из букв, т.е. не учитываем числа и т.д.
            continue

        if len(word) > len(longest_word):  
            # если текущее слово больше последнего самого длинного,
            longest_word = word  
            # то заменыем самое длинное текущим словом

    return longest_word

 
longest = longest_word(sentence)
print(f'Самое длинное слово - "{longest}". Длинна {len(longest)} символов.')
