# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*
# 5
#     1 2 3 4 5
#     3
#     -> 1

from random import randint

n = int(input('Введите желаемое количество элементов в массиве: '))
a = []
for i in range(n):
    a.append(randint(0, 9))

print(f'Сгенерирован следующий массив: {a}')

x = int(input('Введите число Х для и будет определено, сколько раз оно встречается в нашем массиве: '))

res = 0
for i in a:
    if x == i:
        res += 1

print(f'Число {x} в нашем массиве встречается {res} раз/раза!')
