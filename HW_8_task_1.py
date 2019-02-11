'''
1.	Определение количества различных подстрок с использованием хеш-функции.
Пусть дана строка S длиной N, состоящая только из маленьких латинских букв.
Требуется найти количество различных подстрок в этой строке.
'''

import hashlib


text = str(input('Введите строку, используя только строчные латинские буквы: '))
uniq_sub_str = set()
uniq_ = set()
for i in range(len(text)):
    for j in range(i+1, len(text)+1):
        sub = text[i:j]
        sub_hash = hashlib.sha1(sub.encode('utf-8')).hexdigest()
        uniq_.add(sub)
        uniq_sub_str.add(sub_hash)

print(f'Количество различных подстрок: {len(uniq_sub_str)}')

