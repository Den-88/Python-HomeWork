# *Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка; B, C, M, P – 3 очка; F, H, V, W, Y – 4 очка; K – 5 очков; J, X – 8 очков; Q,
# Z – 10 очков. А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка; Б, Г, Ё, Ь, Я – 3 очка; Й, Ы – 4 очка; Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские,
# либо только русские буквы.

# *Пример:*
# ноутбук
#     12

str = input('Введите слово: ')

res = 0
for i in str:
    if i in 'AEIOULNSTRАВЕИНОРСТ' or i in 'AEIOULNSTRАВЕИНОРСТ'.lower():
        res += 1
    elif i in 'DGДКЛМПУ' or i in 'DGДКЛМПУ'.lower():
        res += 2
    elif i in 'BCMPБГЁЬЯ' or i in i in 'BCMPБГЁЬЯ'.lower():
        res += 3
    elif i in 'FHVWYЙЫ' or i in 'FHVWYЙЫ'.lower():
        res += 4
    elif i in 'KЖЗХЦЧ' or i in 'KЖЗХЦЧ'.lower():
        res += 5
    elif i in 'JXШЭЮ' or i in 'JXШЭЮ'.lower():
        res += 8
    elif i in 'QZФЩЪ' or i in 'QZФЩЪ'.lower():
        res += 10

print(f'Cтоимость введенного слова: {res}')
