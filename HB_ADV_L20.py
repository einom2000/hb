import turtle

class Quanquan(object):
    def __init__(self, color, radius):
        self.yanse = color
        self.banjin = radius

    def color(self, color):
        turtle.pencolor(color)

    def draw(self):
        turtle.bgcolor('black')
        turtle.hideturtle()
        turtle.speed(0)
        turtle.circle(self.banjin)



kkk = Quanquan('blue', 10)
bbb = Quanquan('yellow', 12)
kkk.color('white')
kkk.draw()

turtle.mainloop()