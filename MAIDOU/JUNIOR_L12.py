a = 'He said:\'he is a \"boy\"\'.'
print(a)

#  '\\\'
b = '\'\\\\\\\''
print(b)

c = 'abcdefghijklmnopqrstuvwxyz'
print(c[0] + ', ' + c[-2])
# a, y
# defghijklmnopqrstuvw
print(c[3:-3])

d = 'luca chen'
print(d.title())
print(d.upper())
print(d.lower())
print(d.replace('chen', 'luca').upper())

# Luca Chen
# LUCA CHEN
# LUCA LUCA

e = 'luca|gao|zhao|lee|yao'
# Luca, Gao, Zhao, Lee, Yao

f = 'luca|gao|zhao|lee|yao'
# LUCA LEE ZHAO
print(f[:4].upper(), f[f.find('lee'):f.find('lee') + 3].upper()\
      , f[f.find('zhao'): f.find('zhao') + 4].upper())

g = '1 + 2 + 3 + 4 + 5 + 6 + 7'
# list! [1,2,3,4,5,6,7]
print(g.split(' + '))

h = 'a++b++c++d++e++f'
# 'a***b***c***d***e***f'
print(h.replace('++','***'))
print('***'.join(h.split('++')))

#-----------------------------------------------------

n = ['a', 'b', 'c']
m = 'abc'

print(n[0] == m[0])
n[0] = 'b'
print(n)
m = m.replace('a', 'b')
print(m)

print(n[:2])
print(m[:2])

q = [1,2,3,4,5,6]
q = q[::-5]
print(q)

r = '1234567890'
# 13579
print(r[::2])
# 24680
print(r[1::2])
# 97531
print(r[-2::-2])
# 08642
print(r[-1::-2])
