# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой,
# а некоторые – гербом. Определите минимальное число монеток, которые нужно
# перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть

from random import randint

n = int(input('Введите количество монеток: '))
m = []
for i in range(n):
    m.append(randint(0, 1))

print(f'Сгенерирован следующий массив: {m}')

o = 0
r = 0
for i in range(n):
    if m[i] == 0:
        r += 1
    else:
        o += 1

if r > o:
    print(f'Минимальное количество монет, которые нужно перевернуть: {o}')
else:
    print(f'Минимальное количество монет, которые нужно перевернуть: {r}')
