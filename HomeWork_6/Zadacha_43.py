# Задача No43. 
# Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу. 
# Считается, что любые два элемента, равные друг другу образуют одну пару, которую 
# необходимо посчитать. Вводится список чисел. Все числа списка находятся на разных строках.

# Ввод: 
# 12323
# Вывод:
# 2

from random import randint

min_random = 0
max_random = 9
n = int(input('Введите желаемое количество элементов в массиве: '))

a = []
for i in range(n):
    a.append(randint(min_random, max_random))

print('Сгенерирован следующий массив:')
print(a)

res = 0
exclude = []
for i in a: 
    if i not in exclude:
        temp = 0
        for j in a:
          if i == j:
               temp += 1
        res += temp // 2
        exclude.append(i)

print(f'Количество пар значений: {res}')
    

