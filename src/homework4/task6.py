"""
Слова
Во входной строке записан текст. Словом считается последовательность
непробельных символов идущих подряд, слова разделены одним или большим
числом пробелов или символами конца строки.
Определите, сколько различных слов содержится в этом тексте.
"""
line = '''By fusing consulting talent with engineering expertise,
       we’re able to integrate vision and execution so you can
       quickly move from strategy to reality.'''
lst = line.split()
st = set(lst)
print(len(st))
