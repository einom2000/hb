import math
c, h = 50, 30
d = input('pls:').split(',')
q = []
for i in d:
    value = math.sqrt((2 * c * int(i)) / h)
    q.append(int(value))
print(q)



