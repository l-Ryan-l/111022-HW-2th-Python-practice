# №1. Напишите программу, которая принимает на вход вещественное число и
# показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

x = input('Введите число: ')
summ_of_digits = 0

for i in str(x):
    if i != '.':
        summ_of_digits += int(i)

print(summ_of_digits)

# №2. Напишите программу, которая принимает на вход число N и
# выдает набор произведений чисел от 1 до N.
# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

n = int(input('Введите число N: '))
res = 1
print(f'Результат для введенного N = {n}: [', end='')
for i in range(1, n):
    res = res * i
    print(res, end=', ')
print(f'{res * n}' ']')

# №3. Задайте список из n чисел последовательности (1+ 1/n)^n
# и выведите на экран их сумму.
# Пример:
# Для n = 4: {1: 2, 2: 2.5, 3: 2.37, 4: 2.44}
# Сумма:

n = int(input('Введите число N: '))
list = []
summ = 0
for i in range(1, n+1):
    sequence = (1 + 1/i) ** i
    list.append(sequence)

for i in list:
    summ += i
print(int(summ * 100) / 100)

# №4. Задайте список из N элементов, заполненных числами
# из промежутка [-N, N]. Реализуйте алгоритм перемешивания списка.


import random
from random import randint

n = int(input('Введите длину списка: '))
list = []
for i in range(-n, n+1):
    list.append(randint(-n, n))
print(f'Исходный список: {list}')
random.shuffle(list)
print(f'Перемешанный список: {list}')


# 5 Даны два массива:
# [1, 2, 3, 2, 0] и [5, 1, 2, 7, 3, 2]
# Надо вернуть их пересечение
# [1, 2, 2, 3]
# (порядок не важен)

list_a = [1, 2, 3, 2, 0]
list_b = [5, 1, 2, 7, 3, 2]
list_intersection = []

for i in list_a:
    if i in list_b:
        list_intersection.append(i)
print(list_intersection)