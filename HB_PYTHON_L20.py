import turtle
import time
import random

ball_total = 10
balls = []
colors = ['red', 'blue', 'green', 'yellow', 'cyan',
          'magenta', 'violet', 'ivory', 'silver',
          'purple', 'brown', 'white', 'gray']

screen_width = 700
screen_height = 700

# create a screen
wn = turtle.Screen()
wn.bgcolor('black')
wn.title('我是中文窗口屏幕对象哈哈！')
wn.setup(screen_width, screen_height)
wn.tracer(0)

# create a balls' list
for _ in range(0, ball_total):
    ball = turtle.Turtle()
    ball.shape('circle')
    ball.color(random.choices(colors))
    ball.speed(0)
    ball.penup()
    ball.goto(random.randint(screen_width // -2, screen_width // 2),
              random.randint(0, screen_height // 2))
    ball.dx = random.uniform(0, 2)
    ball.dy = random.uniform(-1, 2)
    ball.gravity = random.uniform(0.1, 0.3)
    ball.pendown()
    balls.append(ball)


# main loop
while True:
    wn.update()
    for ball in balls:
        ball.dy -= ball.gravity
        ball.sety(ball.ycor() + ball.dy)
        ball.setx(ball.xcor() + ball.dx)

        if ball.xcor() < -350 or ball.xcor() > 350:
            ball.dx *= -1

        if ball.ycor() <= -350:
            ball.dy *= -1
            # ball.color(random.choices(colors))


