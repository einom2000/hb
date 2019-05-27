import random
import turtle
import cv2


def draw_branch(shape):
    global radius
    flake_pen.fillcolor(color)
    flake_pen.begin_fill()
    if shape == 'oval':
        for _ in range(2):
            flake_pen.circle(radius, 90)
            flake_pen.circle(radius / 3, 90)
    elif shape == 'circle':
        flake_pen.circle(radius)
    elif shape == 'tri':
        for _ in range(3):
            flake_pen.fd(radius)
            flake_pen.lt(120)
    elif shape == 'diamond':
        for _ in range(2):
            flake_pen.fd(radius)
            flake_pen.lt(120)
            flake_pen.fd(radius)
            flake_pen.lt(60)

    elif shape == 'trap':
        for _ in range(2):
            flake_pen.fd(radius * 2)
            flake_pen.lt(120)
            height = radius /2
            flake_pen.fd(radius - height / 2)
            flake_pen.lt(60)
    elif shape == 'square':
        for _ in range(4):
            flake_pen.fd(radius)
            flake_pen.lt(90)

    flake_pen.end_fill()


def random_pen():
    global radius, screen_width, screen_height, flake_x, flake_y, color
    flake_pen.penup()
    radius = random.randint(1, 4) * 10
    region = [int(-0.5 * screen_width + radius), int(0.5 * screen_height - radius),
              int(0.5 * screen_width - radius), int(-0.5 * screen_height + radius)]
    colors = ['red', 'yellow', 'orange', 'green', 'brown', 'gold', 'magenta', 'silver', 'white', 'blue', 'cyan', 'purple', 'violet']
    color = colors[random.randint(0, len(colors) - 1)]
    flake_pen.color(color)
    flake_pen.pensize(random.randint(1, 3))
    flake_x = random.randint(region[0], region[2])
    flake_y = random.randint(region[3], region[1])
    flake_pen.setposition(flake_x, flake_y)
    flake_pen.setheading(random.randint(0, 90))
    flake_pen.pendown()


def draw_flake():
    random_pen()
    shape = shapes[random.randint(0, len(shapes) - 1)]
    draw_branch(shape)


screen_width = 700
screen_height = 700
wn = turtle.Screen()
wn.setup(screen_width, screen_height)
wn.bgcolor('black')
wn.title('just press space to make flakes')

flake_pen = turtle.Turtle()
flake_pen.hideturtle()
flake_pen.speed(0)
flake_pen.penup()

radius = 0
flake_x = 0
flake_y = 0
color = 'white'
# shapes = ['circle', 'tri', 'diamond', 'oval', 'square', 'trap']
shapes = ['trap', 'trap']
wn.listen()
wn.onkey(draw_flake, 'space')

while True:
    random_pen()
    draw_branch(shapes[random.randint(0, len(shapes) - 1)])
    wn.update()