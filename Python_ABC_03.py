# Работаем с файлом IMDbnames_f.csv
# О каком количестве людей содержатся данные в этом файле (сколько в нем строк)?
rows = open('IMDbnames_f.csv', encoding="utf8").read().split("\n")
print(*rows[0:50], sep="\n")
print(len(rows))

# Выведите первые 10 имен актеров в этом файле.
for r in rows[0:10]:
    cols = r.split('#')
    print(cols[1])

# Сколько людей в этом файле имеют фамилию Brando?
i = 0
for r in rows:
    cols = r.split("#")
    if cols[1].endswith(" Brando"):
        i += 1
print(i)

# У скольких записей отмечено natural causes в причине смерти? Оно может быть написано с большой или маленькой буквы, а также быть частью поля, например: natural causes, after suffering a stroke
i = 0
for r in rows:
    cols = r.split("#")
    if "natural causes" in cols[5].lower():
        i += 1
print(i)

# Выведите в порядке встречаемости в файле имена тех людей, у которых рост выше 200 см.
i = 0
for r in rows:
    cols = r.split("#")
    if cols[2].isdigit():
        if int(cols[2]) > 200:
            print(cols[1])

# Выведите в порядке встречаемости в файле имена тех нынее живущих людей, у которых рост выше 200 см.
# Пронумеруйте список начина я с 1, под число отдайте 3 символа, под Имя: 40, выравнивание по правому краю с заполнением точками (показан частичный вывод).
#   3) ........Florian Henckel von Donnersmarck
#   4) ........................Lance W. Dreesen
#   5) ............................Brad Garrett
#   6) ..........................Montell Jordan
#   7) ...........................Dennis Rodman
#   8) ..........................Richard Ashton
#   9) .........................Martin Bayfield
#  10) .........................Abraham Benrubi
#  11) ..............................Ray Benson
i = 1
for r in rows:
    cols = r.split('#')
    if cols[2].isdigit():
        if int(cols[2]) >= 200 and cols[4] == "":
            space = 3 - len(str(i))
            dot = 40 - len(cols[1])
            print(" " * space, i, ") ", "." * dot, cols[1], sep='')
            i += 1

# Выведите имя самого высокого актера, рост которого лежит в диапазоне [200, 300] см. Вы будет удивлены, но это не человек.
names = []
max1 = 0
for r in rows:
    cols = r.split("#")
    if cols[2].isdigit():
        if 200 <= int(cols[2]) <= 300:
            if int(cols[2]) > max1:
                max1 = int(cols[2])
                names = cols[1]
print(names)

# Найдите саму часто встречающуюся фамилию в данном файле.

names = {}
for r in rows:
    cols = r.split("#")
    second_name = cols[1].rsplit(maxsplit=1)[-1]
    if second_name not in names.keys():
        # count = int(names.get(second_name))
        # names[second_name] = count + 1
        names[second_name] = 1
    names[second_name] += 1
# max_second_name = max(names.values())
# print(list(names.keys())[list(names.values()).index(max_second_name)])
print(max(names, key=names.get))

# from collections import Counter
# print(len(names))
# counter = 0
# num = names[0]
# for i in names:
#     if names.count(i) > counter:
#         counter = names.count(i)
#         num = i
#
# num = max(set(names), key = names.count)
#
# print(num)

