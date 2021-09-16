import numpy
s = "\n".join(iter(input, ""))
v = s.split('\n')
n = int(v[0])
if n == 1:
    print (0)
for m in v:
    print (m.split(' '))
input_arr = numpy.array(v[1:])\

print(input_arr, type(input_arr))