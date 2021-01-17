"""Слова
    Во входной строке записан текст. Словом считается последовательность
    непробельных символов идущих подряд, слова разделены одним или большим
    числом пробелов или символами конца строки. Определите, сколько различных
    слов содержится в этом тексте.
"""


my_string = ('fcgh gvf g gfgfg. hgfu.   kjhgf/kjbh.kdjcs.dfj335gdkhgj.srgh\n'
             'jhgfg?nbhvdfg gfdtyug   hgfu. hgfu. hgfu. hgfu.    hjfdgfghjb')

print(len(set(my_string.split())))
