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

d = 'Luca Chen, Mike Liu, Sunny Chen'
d = d.lower()
print(d)
d = d.upper()
print(d)
d = d.title()
print(d)
print('==================')
e = ['Luca Chen', 'Mike Liu', 'Sunny Chen']
s = '|'
d = s.join(e)
print(d)