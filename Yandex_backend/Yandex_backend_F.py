#list_request = open('input.txt', encoding="utf8").read().split("\n")
s = "\n".join(iter(input, ""))
list_request = s.split('\n')
first_string = list_request[0].split(' ')
num_request = int(first_string[0])
max_cash = int(first_string[1])
cash = dict()
min_cash = 0
l = 0
for i in range(num_request):
    string = list_request[i+1].split(' ')
    if string[0] not in cash and l < max_cash:
        print (i+1, "PUT", string[0])
        cash[string[0]] = int(string[1])
    elif string[0] not in cash and l == max_cash and int(string[1]) > cash[min_cash]:
        print(i+1, "DELETE", min_cash)
        print(i+1, "PUT", string[0])
        cash.pop(min_cash)
        cash[string[0]] = int(string[1])
    elif string[0] in cash and int(string[1]) > cash[min_cash]:
        print(i+1, "UPDATE", string[0])
        cash[string[0]] = int(string[1])
    min_cash = min(cash, key=cash.get)
    l = len(cash)