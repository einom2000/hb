from turtle import *
from turtle import Turtle

n = 19
for i in range(n):
    forward(30)
    left(180 - ((n - 2) * 180) / n)
colors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange']
for i in range(500):
    pencolor(colors[i % 6])
    width(i / 100 + 1)
    forward(i)
    left(59)

# maidou = Turtle()
# maidou.screen.bgcolor('black')
# colors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange']
# maidou.screen.tracer(0, 0)
#
# for i in range(300):
#     maidou.color(colors[i % 6])
#     maidou.pensize(int(i / 30) + 1)
#     # maidou.circle(i)
#     maidou.fd(i)
#     maidou.left(59)
#
# maidou.screen.exitonclick()
# maidou.screen.mainloop()
colors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange']
for angle in range(0, 360, 15):
    setheading(angle)
    pencolor(colors[int(angle / 15) % 6])
    forward(100)
    write(str(angle) + 'D')
    backward(100)
exitonclick()