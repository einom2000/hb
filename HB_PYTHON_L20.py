import turtle
import time
import random

ball_total = 1000
balls = []
colors = ['red', 'blue', 'green', 'yellow', 'cyan',
          'magenta', 'violet', 'ivory', 'silver',
          'purple', 'brown', 'white', 'gray']

# create a screen
wn = turtle.Screen()
wn.bgcolor('black')
wn.title('我是中文窗口屏幕对象哈哈！')
wn.setup(700, 700)
wn.tracer(0)

# create a balls' list
for _ in range(0, ball_total):
    ball = turtle.Turtle()
    ball.shape('circle')
    ball.color(random.choices(colors))
    ball.speed(0)
    ball.penup()
    ball.goto(random.randint(-200, 200),
              random.randint(-200, 200))
    ball.dx = random.randint(0, 3)
    ball.dy = random.randint(-2, 2)
    balls.append(ball)

GRAVITY = 0.1
# main loop
while True:
    wn.update()
    for ball in balls:
        ball.dy -= GRAVITY
        ball.sety(ball.ycor() + ball.dy)
        ball.setx(ball.xcor() + ball.dx)

        if ball.xcor() < -350 or ball.xcor() > 350:
            ball.dx *= -1

        if ball.ycor() <= -350:
            ball.dy *= -1
            ball.color(random.choices(colors))


