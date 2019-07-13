import turtle
import random

def start():
    global is_game_start
    is_game_start = True


def write_name():
    kid_name.clear()
    kid_name.setposition(kid_car.xcor() - 15, kid_car.ycor() + 10)
    kid_name.write('KIDDS')
    luca_name.clear()
    luca_name.setposition(luca_car.xcor() - 15, luca_car.ycor() + 10)
    luca_name.write('LUCA')


wn = turtle.Screen()

wn.setup(700, 700)
wn.bgcolor('black')
wn.addshape('car.gif')

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
kid_a = random.uniform(0.1, 0.4)
luca_a = random.uniform(0.1, 0.4)

is_game_start = False
winner = ''

wn.listen()
wn.onkey(start, 'space')

while True:
    wn.update()
    if is_game_start:
        kid_dx += kid_a
        luca_dx += luca_a
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

