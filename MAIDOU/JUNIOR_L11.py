# # list
# a = []
# # this is an empty list
# b = ''
# b = b + 'a'
# if b == ' a':
#     print(True)
# else:
#     print(False)
#
# a.append('a')
# print(a)
#
# a.append('b')
# print(a)
#
#
#
# a = ['a', 'b']
# print(a[1])
#
# b = 'ab'
# print(b[1])
#
# print(a[1] == b[1])
# print(a == b)
#
# a[1] = 'c'
# # b[1] = 'c'
# b = b.replace('b', 'c')
# # TypeError: 'str' object does not support item assignment
# print(a)
# print(b)
import turtle
import random

bt = 100
bs = []
clrs = ['red', 'blue', 'green', 'yellow', 'cyan',
          'magenta', 'violet', 'ivory', 'silver',
          'purple', 'brown', 'white', 'gray']

w = 700
h = 700

s = turtle.Screen()
s.bgcolor('black')
s.setup(w, h)
s.tracer(0)

for _ in range(0, bt):
    b = turtle.Turtle()
    b.shape('circle')
    b.turtlesize(random.uniform(1, 3))
    b.color(random.choices(clrs))
    b.speed(0)
    b.penup()
    b.goto(random.randint(w // -2, w // 2),
           random.randint(h // -2, h // 2))
    b.dx = random.uniform(0, 2)
    b.dy = random.uniform(-1, 2)
    b.g = random.uniform(0.1, 0.3)
    bs.append(b)

while True:
    s.update()
    for b in bs:
        b.dy -= b.g
        b.sety(b.ycor() + b.dy)
        b.setx(b.xcor() + b.dx)

        if b.xcor() < -350 or b.xcor() > 350:
            b.dx *= -1

        if b.ycor() <= -350:
            b.dy *= -1









