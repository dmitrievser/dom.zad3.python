# Задача 1. Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
#
# Пример:
# 	[2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random

random_list = []
for i in range(0, 10):
    n = random.randint(0, 9)
    random_list.append(n)

sum = 0
for i in range(1, len(random_list), 2):
    sum += random_list[i]

print('Сгенерированный список: ', random_list)
print('Cумма элементов списка, стоящих на нечётной позиции =', sum)

# Задача 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#
# Пример:
# o	[2, 3, 4, 5, 6] => [12, 15, 16];
# o	[2, 3, 5, 6] => [12, 15]

import random

random_list = []
for i in range(0, 5):
    n = random.randint(0, 9)
    random_list.append(n)

multi_list = []
for i in range(0, len(random_list) // 2 + 1):
    p = (random_list[i] * random_list[len(random_list) - i - 1])
    multi_list.append(p)

print('Сгенерированный список: ', random_list)
print(multi_list)

# Задача 3. Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
#
# Пример:
# o	[1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random

numb_list = []
dr_list = []
for i in range(0, 10):
    n = round(random.uniform(0, 9), random.randint(1, 2))
    n = (int(n * 100)) / 100
    numb_list.append(n)
for i in range(len(numb_list)):
    dr = (int(numb_list[i]*100)) % 100
    dr_list.append(dr)

max_dr = max(dr_list)
min_dr = min(dr_list)

print(numb_list)
print((max_dr - min_dr) / 100)

# Задача 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное 
# (встроенными методами пользоваться нельзя).
#
# Пример:
# o	45 -> 101101
# o	3 -> 11
# o	2 -> 10

num = int(input('Введите целое число: '))
osn = int(input('Введите основание системы счисления: '))

new_num = []
while num != 0:
    ost = num % osn
    new_num.append(ost)
    num //= osn

new_num.reverse()
print(*new_num, sep='')

# Задача 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
#
# Пример:
# o	для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

num = int(input('Введите целое число: '))


def fib(n):
    if n in [1, 2]:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def neg_fib(n):
    if n == 0:
        return 0
    if n == 1:
        return neg_fib(n - 1) + 1
    else:
        return (neg_fib(n - 2) - neg_fib(n - 1))


list_fib = []
for el in range(1, num + 1):
    list_fib.append(fib(el))

# list_neg_fib = []
# for el in range(0, num + 1):
#     list_neg_fib.append(neg_fib(el))
# list_neg_fib.reverse()

list_neg_fib = []
for el in range(num, -1, -1):
    list_neg_fib.append(neg_fib(el))

print(list_neg_fib + list_fib)