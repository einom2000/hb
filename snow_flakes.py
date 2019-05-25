import random
import turtle


def draw_branch():
    global radius
    flake_pen.circle(radius)

def random_pen():
    global radius, screen_width, screen_height
    flake_pen.penup()
    radius = random.randint(1, 4) * 10
    region = [int(-0.5 * screen_width + radius), int(0.5 * screen_height - radius),
              int(0.5 * screen_width - radius), int(-0.5 * screen_height + radius)]
    colors = ['red','orange', 'yellow','green', 'blue', 'cyan', 'purple', 'violet']
    flake_pen.color(colors[random.randint(0, len(colors) - 1)])
    flake_pen.pensize(random.randint(1, 3))
    flake_pen.setposition(random.randint(region[0], region[2]),
                          random.randint(region[3], region[1]))
    flake_pen.setheading(random.randint(0, 90))
    flake_pen.pendown()


def draw_flake():
    random_pen()
    draw_branch()


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

wn.listen()
wn.onkey(draw_flake, 'space')

while True:
    draw_flake()
    wn.update()