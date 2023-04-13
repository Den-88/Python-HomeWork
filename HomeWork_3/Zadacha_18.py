# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к
# заданному числу X. Пользователь в первой строке вводит натуральное число N –
# количество элементов в массиве. В последующих  строках записаны N целых чисел Ai.
# Последняя строка содержит число X

# *Пример:*
# 5
#     1 2 3 4 5
#     6
#     -> 5

from random import randint

min = 0
max = 9
n = int(input('Введите желаемое количество элементов в массиве: '))
x = int(input(f'Введите число Х от {min} до {max} для поиска самого близкого по величине к нему элемента в массиве: '))
a = []
for i in range(n):
    a.append(randint(min, max))

flag = False
near_min = None
near_max = None
for i in a:
    if i == x:
        flag = True
    if i < x and (near_min == None or (x - i) < (x - near_min)):
        near_min = i
    elif i > x and (near_max == None or (i - x) < (near_max - x)):
        near_max = i

print(f'Сгенерирован следующий массив: {a}')
if flag:
    print(f'В массиве имеется элемент {x} равный заданному числу Х!')
elif (x - near_min) < (near_max - x):
    print(f'Ближайший по величине элемент равен {near_min}')
elif (x - near_min) > (near_max - x):
    print(f'Ближайший по величине элемент равен {near_max}')
else:
    print(f'Ближайший по величине меньший элемент равен {near_min}, ближайший по величине больший элемент равен {near_max}')
