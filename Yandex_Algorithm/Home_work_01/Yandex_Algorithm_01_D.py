# Test : https://contest.yandex.ru/contest/28730/problems/

# D. Строительство школы
# Подсказка медиана распределения
n = input()
home_x = list(map(int, input().split(' ')))
def school_x (n, x):
    ans = x[int(n)//2]
    return ans
print(school_x(n, home_x))