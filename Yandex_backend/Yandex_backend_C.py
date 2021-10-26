import time
from collections import deque
s = "\n".join(iter(input, ""))
v = s.split('\n')
# v = open('input.txt', encoding="utf8").read().split("\n")
n = v[0].split(' ')
time_error = int(n[0])
num_error = int(n[1])
q = deque("", num_error)
answer = -1
for r in v[1:]:
    if "] ERROR " in r:
        p = r.partition(" ERROR ")
        t = time.strptime(p[0], '[%Y-%m-%d %X]')
        t_sec = int(time.mktime(t))
        q.append(t_sec)
        if len(q)>=num_error and q[num_error-1] - q[0] <= time_error-1:
            answer = p[0].replace('[', '').replace(']', '')
            break
print (answer)