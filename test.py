# test code
# def func(n, k):
#     if k == 0:
#         return(1)
#     if k > n:
#         return(0)
#     return(func(n-1, k)+func(n-1, k-1))

# print(func(*map(int, input().split())))

n = int(input())

for x in range(n):
    command, namespace, var = input().split()
    if command == 'creat':
        
    if comand == 'add':
        pass
    if command == 'get':
        pass
    print ('unkown command')

print(command, namespace, var)
