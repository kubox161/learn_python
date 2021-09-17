# Test : https://contest.yandex.ru/contest/28730/problems/

# B. Кольцевая линия метро

s = list(map(int, input().split(' ')))
l1 = abs(s[1] - s[2]) - 1
l2 = s[0] - max(s[2], s[1]) + min(s[1], s[2]) - 1
print(min (l1, l2))