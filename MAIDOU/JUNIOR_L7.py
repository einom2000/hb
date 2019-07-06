import turtle

def start():
    global is_game_start
    is_game_start = True

wn = turtle.Screen()

wn.setup(700, 700)
wn.bgcolor('violet')
wn.addshape('car.gif')

kid_car = turtle.Turtle()
kid_car.shape('car.gif')
kid_car.penup()
kid_car.speed(0)
kid_car.setposition(-350, 150)

luca_car = turtle.Turtle()
luca_car.shape('car.gif')
luca_car.penup()
luca_car.speed(0)
luca_car.setposition(-350, -150)


dx = 0.1

is_game_start = False

wn.listen()
wn.onkey(start, 'space')

while True:
    wn.update()
    if is_game_start:
        dx += 0.1
        # turtle.setx(turtle.xcor() + dx)

