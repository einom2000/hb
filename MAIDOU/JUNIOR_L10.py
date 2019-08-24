a = 'He said:\'he is a \"boy\"\'.'
print(a)

b = '\'Luca Chen\''
print(b + ' = ' + str(len(b) - 2))

c = 'abcdefghijklmnopqrstuvwxyz'
print(c[0], c[25])
print(c[:3], c[23:26], c[-3:])

c_new = ''
c_len = int(len(c) / 2)
max_index = len(c) - 1
for i in range(0, c_len):
    c_new += c[max_index - i] + c[i]
print(c_new)

d = 'Luca Chen|Mike Liu|Sunny Chen'
d = d.lower()
print(d)
d = d.upper()
print(d)
d = d.title()
print(d)

d1 = d.find('Chen')
print(d1)
d2 = d[d1 + 4:].find('Chen') + d1 + 4
print(d2)
print(d[d1: d1 + 4], d[d2: d2 + 4])

e = d.split('|')
print(e)
print(type(e))

print(len(e))

d = d.replace('|', '/')
print(d)

d = d.replace('Chen', 'Gao')
print(d)

d = d.replace('Gao', 'Chen')
print(d)


print(e)
s = '*****'.join(e)
print(s)
