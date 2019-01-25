"""1. Пользователь вводит данные о количестве предприятий,
их наименования и прибыль за 4 квартала (т.е. 4 отдельных числа)
для каждого предприятия. Программа должна определить среднюю прибыль
(за год для всех предприятий) и вывести наименования предприятий,
чья прибыль выше среднего и отдельно вывести наименования предприятий,
чья прибыль ниже среднего."""


import collections


num = int(input('Введите количество предприятий: '))

D = collections.defaultdict()

for i in range(1, num+1):
    name = str(input(f'Введите название {i}-ого предприятия: '))
    lst = map(float, input('Введите для {name} прибыль за 1-4 кварталы, разделяя значения запятыми: ').split(','))
    D[name] = list(lst)


mid_profit = 0
sums = []
names = []
s_sums = {}

for key in D:
    mid_profit += sum(D[key])
    sums.append(sum(D[key]))
    names.append(key)
    s_sums[key] = sum(D[key])

mid_profit = mid_profit/num
gr_sum = []
ls_sum = []

for key in s_sums:
    if s_sums[key] > mid_profit:
        gr_sum.append(key)
    elif s_sums[key] < mid_profit:
        ls_sum.append(key)
    else:
        continue
    

print(f'Предприятия, у которых прибыль выше среднего: {", ".join(gr_sum)}')
print(f'Предприятия, у которых прибыль ниже среднего: {", ".join(ls_sum)}')
