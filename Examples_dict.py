# Как соединить два словаря
# В Python 3.5+:
x = {'a': 1, 'b': 2}
y = {'b': 3, 'c': 4}

z = {**x, **y}

>>> z
{'c': 4, 'a': 1, 'b': 3}

# В Python 2.x :

>>> z = dict(x, **y)
>>> z
{'a': 1, 'c': 4, 'b': 3}

# В этих примерах Python мержит ключи словарей в порядке, указанном в выражении. При этом дубликаты перезаписываются слева направо.