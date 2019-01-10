"""3. В массиве случайных целых чисел поменять местами минимальный и
максимальный элементы."""


from random import randint as rnd


a = [0] * int(input('Число элементов в массиве: '))
for i in range(len(a)):
    a[i] = rnd(-1000, 1000)

print(f"Исходный массив:\n{a}")


min_el = 0
max_el = 0
ind_min = 0
ind_max = 0

for i in range(len(a)):
    if a[i] <= min_el:
        min_el = a[i]
        ind_min = i
    if a[i] > max_el:
        max_el = a[i]
        ind_max = i

a[ind_min], a[ind_max] = a[ind_max], a[ind_min]

print(f"Измененный массив:\n{a}")


