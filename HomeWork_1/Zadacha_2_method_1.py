# Задача 2: Найдите сумму цифр трехзначного числа.

# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

n = input('Введите трехзначное число: ')

test_flag = len(n) == 3 and n.isdecimal()

while test_flag == False:
    n = input('Введено не трехзначное число! Повторите ввод: ')
    test_flag = len(n) == 3 and n.isdecimal()

sum = int(n[0]) + int(n[1]) + int(n[2])

print(f'Сумма цифр трехзначного числа = {sum}')