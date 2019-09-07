a = 1
b = 2
print(a + b)

class Add(object):

    def __init__(self, a , b):
        self.a = a
        self.b = b

    def add(self):
        print(a + b)


p = Add(1, 2)
p.add()



