# Считывание в список последовательности чисел, введенных в одну строку
seq = list(map(int, input().split()))
print(seq, type(seq))

# Оставить в строке только буквы кирилицы. Ссылка https://egorovegor.ru/python-remove-unicode-character/
string_output = ''.join([i if ord(i) > 128 else '' for i in string])

# Вывести строку в обратном порядке (переворот строки)
x = 'forest'
''.join(reversed(list(x)))
# или
for i in reversed(x):
    print(i, end='')
