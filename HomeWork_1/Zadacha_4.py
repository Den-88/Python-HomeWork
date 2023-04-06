# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они
# сделали S журавликов. Сколько журавликов сделал каждый ребенок, если известно,
# что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в
# два раза больше журавликов, чем Петя и Сережа вместе?

# *Пример:*
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10

s = input('Введите количество журавликов, которое дети сделали вместе: ')

test_flag = s.isdecimal() and int(s) % 6 == 0

while test_flag == False:
    s = input('Для решения данной задачи должно быть введено число, кратоное 6! Повторите ввод: ')
    test_flag = s.isdecimal() and int(s) % 6 == 0

s = int(s)
print(f'Дети сделали следующее количество журавликов:\nПетя - {int(s / 6)}\nСережа - {int(s / 6)}\nКатя - {int(s / 6 * 4)}')
