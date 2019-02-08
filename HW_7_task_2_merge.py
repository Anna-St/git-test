"""2. Отсортируйте по возрастанию методом слияния одномерный
вещественный массив, заданный случайными числами на промежутке [0; 50).
Выведите на экран исходный и отсортированный массивы."""

import random 

array = [0] * int(input('Сколько элементов должном быть в массиве? '))
#fl = int(input('До какого знака после запятой хотите округлить числа в массиве? '))
for i in range(len(array)):
    #если с округлением, то array[i] = round(random.uniform(0, (50 - random.random())), fl) 
    array[i] = random.uniform(0, (50 - random.random()))
#очень хотелось взять numpy.random.uniform,
#поскольку он исключает верхнюю границу,
#но вы вроде как просили numpy не использовать   


print(f'Исходный массив: \n{array}')

def merge(left, right):
    lst = []
    while left and right:
        #сравниваем 0-ые элементы подмассивов, наименьший добавляем в результат, и удаляем из сравниваемого подмассива
        if left[0] < right[0]: 
            lst.append(left.pop(0))
        else:
            lst.append(right.pop(0))
    #когда элементы в одном из подмассивов для сравнения закончились, элементы из другого дописываем в результат 
    if left:
        lst.extend(left)
    if right:
        lst.extend(right)
    return lst
 
def merge_sort(lst):
    #дробим массивы на подмасссивы и передаем на слияние
    if len(lst) >= 2:
        mid = int(len(lst) / 2)
        lst = merge(merge_sort(lst[:mid]), merge_sort(lst[mid:]))
    return lst

print(f'Отсортированный по возрастанию массив: \n{merge_sort(array)}')
