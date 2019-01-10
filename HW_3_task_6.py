"""6. В одномерном массиве найти сумму элементов, находящихся между
минимальным и максимальным элементами. Сами минимальный и максимальный
элементы в сумму не включать."""


from random import randint as rnd


a = [0] * int(input('Число элементов в массиве: '))
for i in range(len(a)):
    a[i] = rnd(-1000, 1000)

print(f"Исходный массив:\n{a}")


min_el = 0
max_el = 0

for i in range(len(a)):
    if a[i] < min_el: 
        min_el = a[i]
    elif a[i] > max_el:
        max_el = a[i]
        
summ = 0

if a.index(min_el) < a.index(max_el):
    for j in range(a.index(min_el)+1, a.index(max_el)):
        summ = summ + a[j]
else:
    for j in range(a.index(max_el)+1, a.index(min_el)):
        summ = summ + a[j]

print(f'Сумма между минимальным {min_el} и максимальным {max_el} элементами массива = {summ}')
