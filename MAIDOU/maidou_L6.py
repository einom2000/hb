import turtle
import random
import math

class Draw_circle(object):
    def __init__(self, x, y, color, pensize, radius):
        self.x = x
        self.y = y
        self.color = color
        self.pensize = pensize
        self.radius = radius
        self.status = True

    def draw(self):
        turtle.penup()
        turtle.hideturtle()
        if self.status:
            turtle.pencolor(self.color)
        else:
            turtle.pencolor('black')
        turtle.pensize(self.pensize)
        turtle.speed(0)
        turtle.goto(self.x, self.y)
        turtle.pendown()
        turtle.circle(self.radius)


def is_collision():
    pass
    return is_overlap

wn = turtle.Screen()
wn.setup(700, 700)
wn.bgcolor('black')
wn.title('麦豆的作品')

circles = []
colors =['yellow', 'white', 'red', 'blue',
         'cyan', 'violet', 'orange', 'purple',
         'green', 'gray', 'brown', 'ivory',
         'magenta', 'turquoise']

for _ in range(0, 30):
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    color = random.choice(colors)
    pensize = random.randint(1, 5)
    radius = random.randint(20, 50)
    c = Draw_circle(x, y, color, pensize, radius)
    circles.append(c)

for quanquan in circles:
    quanquan.draw()

while True:
    for quanquan in circles:
        if random.randint(0, 3) == 1:
            quanquan.status = not quanquan.status
            quanquan.draw()
            if not quanquan.status:
                index = circles.index(quanquan)
                for i in range(0, len(circles)):
                    if i != index:
                        distance = math.sqrt(math.pow((circles[i].x - quanquan.x), 2) +
                                             math.pow((circles[i].y - quanquan.y), 2))
                        if distance <= circles[i].radius + quanquan.radius + 10:
                            if circles[i].status:
                                circles[i].draw()

wn.mainloop()
