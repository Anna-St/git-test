'''
1.	Определение количества различных подстрок с использованием хеш-функции.
Пусть дана строка S длиной N, состоящая только из маленьких латинских букв.
Требуется найти количество различных подстрок в этой строке.
'''

import hashlib


text = str(input('Введите строку, используя только строчные латинские буквы: '))
uniq_sub_str = set()

for i in range(len(text)):
    for j in range(i+1, len(text)+1):
        sub_hash = hashlib.sha1(text[i:j].encode('utf-8')).hexdigest()
        uniq_sub_str.add(sub_hash)

print(f'Количество различных подстрок: {len(uniq_sub_str)}')

