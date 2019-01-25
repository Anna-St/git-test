"""2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""

#ПРЕЖДЕ ЧЕМ ЗАПУСКАТЬ на больших числах, лучше закомментить строку print(f'Произведение равно {mini_mult_16(num_1, num_2)}'), т.к. функция очень ресурсоемкая

from collections import deque


num_1 = input('Введите символы 1-ого числа, через запятую (буквы должны быть прописные!): ').split(",")
num_2 = input('Введите символы 2-ого числа, через запятую(буквы должны быть прописные!) : ').split(",")

#готовим таблицу сложения
add_table = {}
sign_16 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F']
key = 0
value = 0

for i in range(len(sign_16)):
    for j in range(len(sign_16)):
        key = str(sign_16[i]) + '+' + str(sign_16[j])
        if j + i < 16:
            value = sign_16[j+i]
            add_table[key] = [value, 0]
        else:
            value = sign_16[j+i-16]
            add_table[key] = [value, 1]   

#print(add_table)


def add_16(num1, num2):
    num1 = deque(num1)
    num2 = deque(num2)
    
#выравниваем длину слагаемых
    if len(num1) < len(num2):
        for i in range(len(num2) - len(num1)):
            num1.appendleft('0')
    elif len(num2) < len(num1):
        for i in range(len(num1) - len(num2)):
            num2.appendleft('0')

    sum_i = 0
    p = 0
    summ = deque()

    for i in reversed(range(len(num1))):
        proto_key = str(num2[i]) + '+' + str(p)
        key = str(num1[i]) + '+' + str(add_table[proto_key][0])
        sum_i = add_table[key][0]
        p = add_table[key][1]
        summ.appendleft(str(sum_i))
    if p == 1:
        summ.appendleft('1')
    return list(summ)

print(f'Сумма равна {list(add_16(num_1, num_2))}')


#базовая функция умножения, основанная на сложении num2 раз числа num1. Жрёт ресурсов немеренно
def mini_mult_16(num1,num2):
    if len(num1) < len(num2): #е понимаю пока помчему, но если длина первого короче, то считается в разы дольше
        num1, num2 = num2, num1

    mult = '0'
    counter = deque()
    while counter != list(num2):
        mult = add_16(mult, num1)
        counter = add_16('1', counter)
    return mult

print(f'Произведение равно {mini_mult_16(num_1, num_2)}')

#попробуем оптимизировать и делать с использованием таблицы умножения
#заготовка таблицы умножения
mult_table = {}
key_m = 0

for j in range(len(sign_16)):
    key_m = str(0) + '*' + str(sign_16[j])
    mult_table[key_m] = 0
    key_m = str(sign_16[j]) + '*' + str(0)
    mult_table[key_m] = 0

for i in range(1,len(sign_16)):
    for j in range(1,len(sign_16)):
        key_m = str(sign_16[i]) + '*' + str(sign_16[j])
        value = mini_mult_16(str(sign_16[i]),str(sign_16[j]))
        mult_table[key_m] = value
        
#print(mult_table)

"""
дальше не успела ещё((((

def mult_16(n1, n2):
    mult = deque()
    mult_i = 0
    z = 0
    for i in reversed(range(len(n1))):
        for j in reversed(range(len(n2))):
            key_ver = str(n2[j]) + '*' + str(z)
            print(type(key_ver))
            mult_i = mult_table[key_ver][-1] #???
            print(mult_i)
            if len(mult_table[key_ver]) == 2:
                z = mult_table[key_ver][0]
            else: z = 0
            mult.appendleft(str(mult_i))
    if z > 0:
        summ.appendleft(z)
    return list(summ)
            
print(f'Произведение равно {mult_16(num_1, num_2)}')
"""












