#9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.

from random import randint as rnd


matrix = [[rnd(-10, 10) for _ in range(5)] for _ in range(3)]

print(f"Исходная матрица:")

for row in matrix:
    for elem in row:
        print("%5d" % (elem), end='')
    print()


min_col = []
min_el = 0
for i in range(len(matrix[0])):
    min_el = matrix[0][i]
    for j in range(len(matrix)):
        if matrix[j][i] < min_el:
            min_el = matrix[j][i]
    min_col.append(min_el)
        
#print(f'Минимальные элементы по столбцам:\n{min_col}')

max_in_min = min_col[0]
for el in range(len(min_col)):
    if min_col[el] > max_in_min:
        max_in_min = min_col[el]

print(f'Максимальный элемент среди минимальных элементов столбцов матрицы = {max_in_min}')
