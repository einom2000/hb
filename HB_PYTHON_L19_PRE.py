import turtle
import time
import random


wn = turtle.Screen()
wn.bgcolor('black')
wn.title('Bouncing Ball')
wn.tracer(0)


ball_number = 300
balls = []
colors = ['red', 'blue', 'green', 'magenta', 'violet', 'purple', 'silver', 'white', 'gray', 'cyan', 'brown', 'orange']


for _ in range(0, ball_number):
    ball = turtle.Turtle()
    ball.shape('circle')
    ball.color(random.choice(colors))
    ball.penup()
    ball.speed(0)
    ball.goto(random.randint(-200, 200), random.randint(-200, 200))
    ball.dx = random.randint(0, 3)
    ball.dy = random.randint(-2, 2)
    balls.append(ball)

gravity = 0.1
while True:
    wn.update()
    time.sleep(0.01)
    for ball in balls:
        ball.dy -= gravity
        ball.sety(ball.ycor() + ball.dy)
        ball.setx(ball.xcor() + ball.dx)

        if ball.xcor() < -300 or ball.xcor() > 300:
            ball.dx *= -1

        if ball.ycor() < -300:
            ball.dy *= -1