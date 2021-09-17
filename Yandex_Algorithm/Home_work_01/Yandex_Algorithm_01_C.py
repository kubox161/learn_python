# Test : https://contest.yandex.ru/contest/28730/problems/

# C. Даты

date_str = list(map(int, input().split(' ')))
def date_type (x, y, z):
    ans = 0
    if y > 12 or x > 12 or x == y:
        ans = 1
    return ans
print(date_type(*date_str))