import turtle

def start():
    global is_game_start
    is_game_start = True

wn = turtle.Screen()

wn.setup(700, 700)
wn.bgcolor('violet')
wn.addshape('car.gif')


turtle.shape('car.gif')
turtle.penup()
turtle.goto(-350, 0)


dx = 0.1

is_game_start = False

wn.listen()
wn.onkey(start, 'space')

while True:
    wn.update()
    if is_game_start:
        dx += 0.1
        turtle.setx(turtle.xcor() + dx)

