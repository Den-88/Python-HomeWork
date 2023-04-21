# Доп. задача на полиндром

word = list(input('Введите слово: '))
flag = True

for i in range(len(word) // 2):
    if word[i] != word[- i - 1]:
        flag = False

if flag:
    print('Это полиндром!')
else:
    print('Это не полиндром!')