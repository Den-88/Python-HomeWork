# Задача 2: Найдите сумму цифр трехзначного числа.

# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

n = input('Введите трехзначное число: ')

test_flag = len(n) == 3 and n.isdecimal()

while test_flag == False:
    n = input('Введено не трехзначное число! Повторите ввод: ')
    test_flag = len(n) == 3 and n.isdecimal()

sum = int(n) // 100 + int(n) // 10 % 10 + int(n) % 10

print(f'Сумма цифр трехзначного числа = {sum}')
