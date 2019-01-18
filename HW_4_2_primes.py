#2. аписать два алгоритма нахождения i-ого посчёту постого числа.

#Решение №1 - без использования "решета Эратосфена":

#import cProfile


#num = int(input())

def _not_sieve(num):
    result = [2]
    i = 3

    while len(result) < num:
        if (i > 10) and (i % 5 == 0):
            i +=2
        for j in result:
            if j*j - 1 > i:
                result.append(i)
                break
            if (i % j == 0):
                break
        else:
            result.append(i)
        i +=2
    return result[-1]


#print(f'{num}-ое простое число = {_not_sieve(num)}')



"""Результаты timeit:
100 loops, best of 5: 9.37 usec per loop - (10)
100 loops, best of 5: 35.3 usec per loop - (25)
100 loops, best of 5: 287 usec per loop - (100)
100 loops, best of 5: 5.64 msec per loop - (1000)
"""


"""Результаты cProfile:

cProfile.run('_not_sieve(10)')
26 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 _not_sieve.py:6(_not_sieve)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
       13    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        9    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}



cProfile.run('_not_sieve(25)')
         68 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 _not_sieve.py:6(_not_sieve)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
       40    0.000    0.000    0.000    0.000 {built-in method builtins.len}
       24    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}



cProfile.run('_not_sieve(100)')
         321 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 _not_sieve.py:6(_not_sieve)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
      218    0.000    0.000    0.000    0.000 {built-in method builtins.len}
       99    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


cProfile.run('_not_sieve(1000)')
         4172 function calls in 0.010 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.010    0.010 <string>:1(<module>)
        1    0.010    0.010    0.010    0.010 _not_sieve.py:6(_not_sieve)
        1    0.000    0.000    0.010    0.010 {built-in method builtins.exec}
     3169    0.000    0.000    0.000    0.000 {built-in method builtins.len}
      999    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

"""

#Решение №2 - с использованием алгоритма "Решето Эратосфена":


#import cProfile


#num = int(input())

def _sieve(num):
    
    def sieve(n):
        sieve = [i for i in range(n)]
        sieve[1] = 0

        for i in range(2, n):
            if sieve[i] != 0:
                j = i + i
                while j < n:
                    sieve[j] = 0
                    j += i

        result = [i for i in sieve if i != 0]
        return result

    n = 2
    while True:
        if len(sieve(n)) == num:
           break
        n += 1

    return (sieve(n)[-1])
      

#print(f'{num}-ое простое число = {_sieve(num)}')

"""Результаты timeit:
100 loops, best of 5: 171 usec per loop - (10)
100 loops, best of 5: 1.55 msec per loop - (25)
100 loops, best of 5: 51.8 msec per loop - (100)"""


"""Результаты cProfile:
cProfile.run('_sieve(10)')
123 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
       30    0.000    0.000    0.000    0.000 _sieve_1.py:18(<listcomp>)
        1    0.000    0.000    0.000    0.000 _sieve_1.py:5(_sieve)
       30    0.000    0.000    0.000    0.000 _sieve_1.py:7(sieve)
       30    0.000    0.000    0.000    0.000 _sieve_1.py:8(<listcomp>)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
       29    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


cProfile.run('_sieve(25)')
395 function calls in 0.002 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.002    0.002 <string>:1(<module>)
       98    0.000    0.000    0.000    0.000 _sieve_1.py:18(<listcomp>)
        1    0.000    0.000    0.002    0.002 _sieve_1.py:5(_sieve)
       98    0.001    0.000    0.002    0.000 _sieve_1.py:7(sieve)
       98    0.000    0.000    0.000    0.000 _sieve_1.py:8(<listcomp>)
        1    0.000    0.000    0.002    0.002 {built-in method builtins.exec}
       97    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


cProfile.run('_sieve(100)')
2171 function calls in 0.054 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.054    0.054 <string>:1(<module>)
      542    0.007    0.000    0.007    0.000 _sieve_1.py:18(<listcomp>)
        1    0.001    0.001    0.054    0.054 _sieve_1.py:5(_sieve)
      542    0.042    0.000    0.053    0.000 _sieve_1.py:7(sieve)
      542    0.005    0.000    0.005    0.000 _sieve_1.py:8(<listcomp>)
        1    0.000    0.000    0.054    0.054 {built-in method builtins.exec}
      541    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

"""

"""
ВЫВОД:
Не смотря на то что количество вызов функций в первом решении больше,
сам алгоритм на несколько порядков быстрее, чем с использованием "решета".
Например, для входного значения 100:
решение 1 - 287 usec per loop,
решение 2 - 51.8 msec per loop.
"""
