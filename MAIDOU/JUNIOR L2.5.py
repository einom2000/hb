from turtle import Turtle
import random
t = Turtle()
t.screen.bgcolor('black')
colors = ['red', 'orange', 'yellow', 'green', 'cyan',
          'blue', 'purple']
t.hideturtle()
t.screen.tracer(0, 0)

for i in range(600):
    t.color(colors[i  % 7])
    t.width(i / 100 + 1)
    t.forward(i)
    t.left(59)

t.screen.exitonclick()
t.screen.mainloop()