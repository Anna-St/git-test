#5. В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.

#Решение №1:

#import cProfile
from random import randint as rnd


def max_min(n):

    a = [0] * n
    for i in range(len(a)):
        a[i] = rnd(-1000, 1000)

#    print(f"Исходный массив:\n{a}")

    neg_a = [] 

    for i in range(len(a)):
        if a[i] < 0:
            if a[i] not in neg_a:
                neg_a.append(a[i])

    max_neg = neg_a[0] 

    for i in range(len(neg_a)):
        if neg_a[i] > max_neg:
            max_neg = neg_a[i]

    return (a.index(max_neg), max_neg)

#print(max_min(100))


"""Результаты timeit:
100 loops, best of 5: 20.1 usec per loop - (10)
100 loops, best of 5: 48.2 usec per loop - (25)
100 loops, best of 5: 201 usec per loop - (100)
100 loops, best of 5: 3.57 msec per loop - (1000)
"""


"""Результаты cProfile:
cProfile.run('max_min(10)')
62 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 HW_4_1_1.py:7(max_min)
       10    0.000    0.000    0.000    0.000 random.py:174(randrange)
       10    0.000    0.000    0.000    0.000 random.py:218(randint)
       10    0.000    0.000    0.000    0.000 random.py:224(_randbelow)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        3    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        4    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
       10    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
       10    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
        1    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}


cProfile.run('max_min(25)')
146 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 HW_4_1_1.py:7(max_min)
       25    0.000    0.000    0.000    0.000 random.py:174(randrange)
       25    0.000    0.000    0.000    0.000 random.py:218(randint)
       25    0.000    0.000    0.000    0.000 random.py:224(_randbelow)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        3    0.000    0.000    0.000    0.000 {built-in method builtins.len}
       12    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
       25    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
       26    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
        1    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}


cProfile.run('max_min(100)')
562 function calls in 0.001 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 HW_4_1_1.py:7(max_min)
      100    0.000    0.000    0.000    0.000 random.py:174(randrange)
      100    0.000    0.000    0.000    0.000 random.py:218(randint)
      100    0.000    0.000    0.000    0.000 random.py:224(_randbelow)
        1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
        3    0.000    0.000    0.000    0.000 {built-in method builtins.len}
       49    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
      100    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
      105    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
        1    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}


cProfile.run('max_min(1000)')
5411 function calls in 0.005 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.004    0.004 <string>:1(<module>)
        1    0.002    0.002    0.004    0.004 HW_4_1_1.py:7(max_min)
     1000    0.001    0.000    0.002    0.000 random.py:174(randrange)
     1000    0.000    0.000    0.002    0.000 random.py:218(randint)
     1000    0.001    0.000    0.001    0.000 random.py:224(_randbelow)
        1    0.000    0.000    0.005    0.005 {built-in method builtins.exec}
        3    0.000    0.000    0.000    0.000 {built-in method builtins.len}
      380    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
     1000    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
     1023    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
        1    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}
"""

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


"""Результаты timeit:
100 loops, best of 5: 19.1 usec per loop - (10)
100 loops, best of 5: 44.6 usec per loop - (25)
100 loops, best of 5: 171 usec per loop - (100)
100 loops, best of 5: 1.71 msec per loop - (1000)
"""

"""Результаты cProfile:
cProfile.run('max_min_1(10)')
59 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 HW_4_1_2.py:8(max_min_1)
       10    0.000    0.000    0.000    0.000 random.py:174(randrange)
       10    0.000    0.000    0.000    0.000 random.py:218(randint)
       10    0.000    0.000    0.000    0.000 random.py:224(_randbelow)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        3    0.000    0.000    0.000    0.000 {built-in method builtins.len}
       10    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
       11    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
        1    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}


cProfile.run('max_min_1(25)')
133 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 HW_4_1_2.py:8(max_min_1)
       25    0.000    0.000    0.000    0.000 random.py:174(randrange)
       25    0.000    0.000    0.000    0.000 random.py:218(randint)
       25    0.000    0.000    0.000    0.000 random.py:224(_randbelow)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        3    0.000    0.000    0.000    0.000 {built-in method builtins.len}
       25    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
       25    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
        1    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}


cProfile.run('max_min_1(100)')
510 function calls in 0.001 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 HW_4_1_2.py:8(max_min_1)
      100    0.000    0.000    0.000    0.000 random.py:174(randrange)
      100    0.000    0.000    0.000    0.000 random.py:218(randint)
      100    0.000    0.000    0.000    0.000 random.py:224(_randbelow)
        1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
        3    0.000    0.000    0.000    0.000 {built-in method builtins.len}
      100    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
      102    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
        1    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}


cProfile.run('max_min_1(1000)')
5035 function calls in 0.003 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.003    0.003 <string>:1(<module>)
        1    0.000    0.000    0.003    0.003 HW_4_1_2.py:8(max_min_1)
     1000    0.001    0.000    0.002    0.000 random.py:174(randrange)
     1000    0.000    0.000    0.002    0.000 random.py:218(randint)
     1000    0.001    0.000    0.001    0.000 random.py:224(_randbelow)
        1    0.000    0.000    0.003    0.003 {built-in method builtins.exec}
        3    0.000    0.000    0.000    0.000 {built-in method builtins.len}
     1000    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
     1027    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
        1    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}
"""

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


"""Результаты timeit:
100 loops, best of 5: 21.2 usec per loop - (10)
100 loops, best of 5: 50.5 usec per loop - (25)
100 loops, best of 5: 201 usec per loop - (100)
100 loops, best of 5: 2.02 msec per loop - (1000)
"""


"""Результаты cProfile:
cProfile.run('max_neg(10)')
69 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 HW_4_1_3.py:10(<listcomp>)
        1    0.000    0.000    0.000    0.000 HW_4_1_3.py:7(max_neg)
       10    0.000    0.000    0.000    0.000 random.py:174(randrange)
       10    0.000    0.000    0.000    0.000 random.py:218(randint)
       10    0.000    0.000    0.000    0.000 random.py:224(_randbelow)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
       11    0.000    0.000    0.000    0.000 {built-in method builtins.len}
       10    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
       13    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}


cProfile.run('max_neg(25)')
167 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 HW_4_1_3.py:10(<listcomp>)
        1    0.000    0.000    0.000    0.000 HW_4_1_3.py:7(max_neg)
       25    0.000    0.000    0.000    0.000 random.py:174(randrange)
       25    0.000    0.000    0.000    0.000 random.py:218(randint)
       25    0.000    0.000    0.000    0.000 random.py:224(_randbelow)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
       26    0.000    0.000    0.000    0.000 {built-in method builtins.len}
       25    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
       36    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}


cProfile.run('max_neg(100)')
653 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 HW_4_1_3.py:10(<listcomp>)
        1    0.000    0.000    0.000    0.000 HW_4_1_3.py:7(max_neg)
      100    0.000    0.000    0.000    0.000 random.py:174(randrange)
      100    0.000    0.000    0.000    0.000 random.py:218(randint)
      100    0.000    0.000    0.000    0.000 random.py:224(_randbelow)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
      101    0.000    0.000    0.000    0.000 {built-in method builtins.len}
      100    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
      147    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}


cProfile.run('max_neg(1000)')
6313 function calls in 0.003 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.003    0.003 <string>:1(<module>)
        1    0.000    0.000    0.003    0.003 HW_4_1_3.py:10(<listcomp>)
        1    0.000    0.000    0.003    0.003 HW_4_1_3.py:7(max_neg)
     1000    0.001    0.000    0.002    0.000 random.py:174(randrange)
     1000    0.000    0.000    0.002    0.000 random.py:218(randint)
     1000    0.001    0.000    0.001    0.000 random.py:224(_randbelow)
        1    0.000    0.000    0.003    0.003 {built-in method builtins.exec}
     1001    0.000    0.000    0.000    0.000 {built-in method builtins.len}
     1000    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
     1307    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
"""

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

"""Результаты timeit:
100 loops, best of 5: 19.7 usec per loop - (10)
100 loops, best of 5: 45.6 usec per loop - (25)
100 loops, best of 5: 176 usec per loop - (100)
100 loops, best of 5: 1.77 msec per loop - (1000)
"""

"""Результаты cProfile:
cProfile.run('max_neg_1(10)')
58 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 HW_4_1_4.py:10(<listcomp>)
        1    0.000    0.000    0.000    0.000 HW_4_1_4.py:7(max_neg_1)
       10    0.000    0.000    0.000    0.000 random.py:174(randrange)
       10    0.000    0.000    0.000    0.000 random.py:218(randint)
       10    0.000    0.000    0.000    0.000 random.py:224(_randbelow)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
       10    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
       13    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}


cProfile.run('max_neg_1(25)')
134 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 HW_4_1_4.py:10(<listcomp>)
        1    0.000    0.000    0.000    0.000 HW_4_1_4.py:7(max_neg_1)
       25    0.000    0.000    0.000    0.000 random.py:174(randrange)
       25    0.000    0.000    0.000    0.000 random.py:218(randint)
       25    0.000    0.000    0.000    0.000 random.py:224(_randbelow)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
       25    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
       29    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}


cProfile.run('max_neg_1(100)')
529 function calls in 0.001 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 HW_4_1_4.py:10(<listcomp>)
        1    0.000    0.000    0.000    0.000 HW_4_1_4.py:7(max_neg_1)
      100    0.000    0.000    0.000    0.000 random.py:174(randrange)
      100    0.000    0.000    0.000    0.000 random.py:218(randint)
      100    0.000    0.000    0.000    0.000 random.py:224(_randbelow)
        1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
      100    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
      124    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}


cProfile.run('max_neg_1(1000)')
5332 function calls in 0.003 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.003    0.003 <string>:1(<module>)
        1    0.000    0.000    0.003    0.003 HW_4_1_4.py:10(<listcomp>)
        1    0.000    0.000    0.003    0.003 HW_4_1_4.py:7(max_neg_1)
     1000    0.001    0.000    0.002    0.000 random.py:174(randrange)
     1000    0.000    0.000    0.003    0.000 random.py:218(randint)
     1000    0.001    0.000    0.001    0.000 random.py:224(_randbelow)
        1    0.000    0.000    0.003    0.003 {built-in method builtins.exec}
     1000    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
     1327    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
"""

"""ВЫВОДЫ:
Все решения довольно схожи. Разницы в алгоритмах как в другой задаче, добиться не удалось(
Принципиального различия ни в количестве вызовов функций, 
ни в скорости работы алгоритмов - нету.
Хотя на больших массивах (см. 1000) разница в обработке может доходить до 1,5-2 раз.
"""








