# Test : https://contest.yandex.ru/contest/28730/problems/

# A. Interactor

# inter_list = map(int, open('input.txt', encoding = "utf8").read().split('\n'))
# inter_list = map(int, '\n'.join(iter(input, '')).split('\n'))
prog_num = int(input())
interactor_num = int(input())
checker_num = int(input())
def interactor(prog_num, interactor_num, checker_num):
    ans = interactor_num
    if interactor_num == 0 and prog_num != 0:
        ans = 3
    elif interactor_num == 4 and prog_num != 0:
        ans = 3
    elif interactor_num == 0 and prog_num == 0:
        ans = int(checker_num)
    elif interactor_num == 1:
        ans = int(checker_num)
    elif interactor_num == 4 and prog_num == 0:
        ans = 4
    elif interactor_num == 6:
        ans = 0
    elif interactor_num == 7:
        ans = 1
    return ans
print(interactor(prog_num, interactor_num, checker_num))
