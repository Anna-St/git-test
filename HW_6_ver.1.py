#5. В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.

#Решение №1:

#import cProfile
import sys
from random import randint as rnd
'''
def show_size(x):
    print(sys.getsizeof(x), type(x))
    if hasattr(x, '__iter__'):
        if not isinstance(x, str):
            for item in x:
                show_size(item)
                

def show_sum_size(x):
    summ = 0
    summ += sys.getsizeof(x)
#    print(x, sys.gets199050izeof(x))
    if hasattr(x, '__iter__'):
        if not isinstance(x, str):
            for item in x:
                summ += show_sum_size(item)
#                print(sys.getsizeof(x))
    return summ

                '''

def show_sum_size(x):
    summ = 0
    summ += sys.getsizeof(x)
#    print(locals(x))
#    print(x, sys.getsizeof(x))
    if hasattr(x, '__iter__'):
        if not isinstance(x, str):
            for item in x:
                summ += show_sum_size(item)
#                print(sys.getsizeof(x))
    return summ


def sum_size(x):
    summ = 0
    summ += sys.getsizeof(x)
#    print(f'Сейчас x это {x}')
    print(f'Сейчас summ это {summ}')    
    print(f'x сейчас это {x}')
    if isinstance(x, (dict, tuple, list)):
        if type(x) == dict:
            for i in x:
                print(f'i={i}')
                summ += sum_size(x[i])
        else:
            for j in range(len(x)):
#                print(f'i={i}')
                summ += sum_size(j)

                
#        print(f'Сейчас x это {x}')
            summ += sum_size(x[i])
#                print(sys.getsizeof(x))
#    print(summ)
    return summ        

        
    summ += sys.getsizeof(x)
#    print(locals(x))
#    print(x, sys.getsizeof(x))
    if hasattr(x, '__iter__'):
        if not isinstance(x, str):
            for item in x:
                summ += show_sum_size(item)
#                print(sys.getsizeof(x))
    return summ

def max_min(n):
#    d = []
    summ = 0
    a = [0] * n
    for i in range(len(a)):
        a[i] = rnd(-1000, 1000)

#    print(f"Исходный массив:\n{a}")
#    print(show_sum_size(a))
#    print(sys.getsizeof(a))
    neg_a = [] 

    for i in range(len(a)):
        if a[i] < 0:
            if a[i] not in neg_a:
                neg_a.append(a[i])
#                print(sys.getsizeof(i))

    max_neg = neg_a[0] 

    for i in range(len(neg_a)):
        if neg_a[i] > max_neg:
            max_neg = neg_a[i]
#            print(sys.getsizeof(i))
#    print(locals())

    s = locals()
    sum_ = 0
    for key in locals():
        sum_ += show_sum_size(s[key])
    print(sum_)
#    print(f'Затраты памяти на переменные: {sum_}')

#        print(show_sum_size(s[key]))
#    print(d)
#    for key in s:
#        summ += sys.getsizeof(key)
#    print(summ)
#    print(sys.getsizeof(a))
#    print(sys.getsizeof(neg_a))
#    print(sys.getsizeof(max_neg))
#    print(a, sys.getsizeof(a))
#    print(neg_a, sys.getsizeof(neg_a))
#    print(max_neg, sys.getsizeof(max_neg))
#    print(f'show {show_size(a)}')
#    print(f'show sum {show_sum_size(d)}')
    return (a.index(max_neg), max_neg, sum_size(locals()))

print(f'Позиция элемента, значение элемента, затраты на память: {max_min(100)}')
#print(f'show {show_size(max_min)}')
#print(f'show sum {show_sum_size(d)}')
#print(f'show sum {show_sum_size(max_min(100))}')

'''

#Решение №2:

#import cProfile
from random import randint as rnd


def max_min_1(n):

    a = [0] * n
    for i in range(len(a)):
        a[i] = rnd(-1000, 1000)

#    print(f"Исходный массив:\n{a}")

    for i in range(len(a)):
        if a[i] < 0:
            max_neg = a[i]
            break

    for i in range(len(a)):
        if a[i] < 0 and a[i] > max_neg:
            max_neg = a[i]

    return (a.index(max_neg), max_neg)


#Решение №3:

#import cProfile
import random


def max_neg(size):
    MIN_ITEM = -800
    MAX_ITEM = 750
    array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(size)]
#    print(array)

    i = 0
    index = -1
    while i < len(array):   
        if array[i] < 0 and index == -1:
            index = i
        elif 0 > array[i] > array[index]:
            index = i
        i += 1

    if index != -1:
        return (array[index], index)

#print(max_neg(100))



#Решение №4:

#import cProfile
import random


def max_neg_1(size):
    MIN_ITEM = -800
    MAX_ITEM = 750
    array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(size)]
#    print(array)

    num = float('-inf')
    for i, item in enumerate(array):
        if 0 > item > num:
            num = item
            index = i

    if num != float('-inf'):
        return (array[index], index)

#print(max_neg(100))

'''
