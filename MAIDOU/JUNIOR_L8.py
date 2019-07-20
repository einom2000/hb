import turtle
import time

def start():
    global is_game_start
    line1 = turtle.Turtle()
    line1.hideturtle()
    line1.color('yellow')
    line1.penup()
    line1.goto(0, 0)
    line1.pendown()
    style = ('Courier', 80, 'bold')
    for i in range(3, 0, -1):
        line1.write(str(i), font=style, align='center')
        time.sleep(1.2)
        line1.clear()
    is_game_start = True


def write_name():
    kid_name.clear()
    kid_name.setposition(kid_car.xcor() - 15, kid_car.ycor() + 10)
    kid_name.write('KIDDS')
    luca_name.clear()
    luca_name.setposition(luca_car.xcor() - 15, luca_car.ycor() + 10)
    luca_name.write('LUCA')


def luca_acc():
    global luca_alpha
    luca_alpha += 0.5
    pass


def kid_acc():
    global kid_alpha
    kid_alpha += 0.5
    pass


wn = turtle.Screen()

wn.setup(700, 700)
wn.bgcolor('black')
wn.addshape('car.gif')

# 画起点，画终点
line = turtle.Turtle()
line.hideturtle()
line.penup()
line.color('yellow')
line.pensize(9)
line.setposition(-320, 350)
line.setheading(90)
for _ in range(10):
    line.pendown()
    line.back(35)
    line.penup()
    line.back(35)
line.penup()
line.goto(348, 350)
line.pendown()
line.back(700)
line.penup()
line.goto(343, 350)
line.pendown()
line.back(700)


kid_car = turtle.Turtle()
kid_car.shape('car.gif')
kid_car.penup()
kid_car.speed(0)
kid_car.setposition(-350, 150)

kid_name = turtle.Turtle()
kid_name.penup()
kid_name.pencolor('green')
kid_name.hideturtle()
kid_name.speed(0)
kid_name.setposition(kid_car.xcor() - 15, kid_car.ycor() + 10)
kid_name.write('KIDDS')

luca_car = turtle.Turtle()
luca_car.shape('car.gif')
luca_car.penup()
luca_car.speed(0)
luca_car.setposition(-350, -150)

luca_name = turtle.Turtle()
luca_name.penup()
luca_name.pencolor('orange')
luca_name.hideturtle()
luca_name.speed(0)
luca_name.setposition(luca_car.xcor() - 15, luca_car.ycor() + 10)
luca_name.write('LUCA')


kid_dx = 0.1
luca_dx = 0.1
kid_alpha = 0
luca_alpha = 0

is_game_start = False
winner = ''

wn.listen()
wn.onkey(start, 'space')
wn.onkey(kid_acc, 'l')
wn.onkey(luca_acc, 'a')

while True:
    wn.update()
    if is_game_start:
        kid_dx += kid_alpha
        luca_dx += luca_alpha

        if kid_dx > 0.25:
            kid_alpha -= 0.25
        else:
            kid_alpha = 0
            kid_dx = 0.1
        if luca_dx > 0.25:
            luca_alpha -= 0.25
        else:
            luca_alpha = 0
            luca_dx = 0.1

        kid_car.setx(kid_car.xcor() + kid_dx)
        luca_car.setx(luca_car.xcor() + luca_dx)
        write_name()
    if kid_car.xcor() >= 350:
        winner = 'KID'
        break
    elif luca_car.xcor() >= 350:
        winner = 'LUCA'
        break

font = ('Courier', 30, 'bold')
turtle.color('red')
turtle.penup()
turtle.hideturtle()
turtle.goto(0, 0)
turtle.write(winner + ' WON!', font=font, align='center')
wn.mainloop()

