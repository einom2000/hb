import turtle
import os
import random
import math
import sys
import winsound

# create screen  object
wn = turtle.Screen()
wn.setup(700, 700)
wn.bgcolor('black')
wn.title('PingPong')

# create boarder
boarder_pen = turtle.Turtle()
boarder_pen.color('white')
boarder_pen.pensize(5)
boarder_pen.penup()
boarder_pen.speed(0)
boarder_pen.setheading(90)
boarder_pen.setposition(-300, -300)
boarder_pen.pendown()
for _ in range(3):
    boarder_pen.fd(600)
    boarder_pen.rt(90)
boarder_pen.penup()
boarder_pen.hideturtle()

# create a ball
ball = turtle.Turtle()
ball.color('orange')
ball.speed(0)
ball.shape('circle')
ball.turtlesize(1)
ball.showturtle()
ball.penup()
ball.setposition(0, 0)

ball_move_pixel = 2

ball_move_pixel_x = 5
ball_move_pixel_y = 3

# create player bar
bar_length = 80 // 2
bar_height = 10 // 2
bar2_length = 160 // 2
bar = [bar_length, bar2_length]
# short paddle
bar_shape = turtle.Shape('compound')
bar_points = ((-bar_height, -bar_length),
              (-bar_height, bar_length),
              (bar_height, bar_length),
              (bar_height, -bar_length))
bar_shape.addcomponent(bar_points, 'white')
wn.register_shape('paddle', bar_shape)
# long paddle
bar_shape2 = turtle.Shape('compound')
bar_points = ((-bar_height, -bar2_length),
              (-bar_height, bar2_length),
              (bar_height, bar2_length),
              (bar_height, -bar2_length))
bar_shape2.addcomponent(bar_points, 'red')
wn.register_shape('paddle2', bar_shape2)

player = turtle.Turtle()
player.shape('paddle')
player.speed(0)
player.showturtle()
player.penup()
player.setposition(-10, -270)

player_move_pixel = 10

score = 0
style = ('Courier', 20, 'bold')
life = 3

# show fixed text:
turtle.color('yellow')
turtle.penup()
turtle.hideturtle()
turtle.goto(-250, 250)
turtle.write('SCORE=', font=style, align='left')
turtle.goto(130, 250)
turtle.write('LIFE=', font=style, align='left')

# show score and life:
displayed_score = turtle.Turtle()
displayed_score.hideturtle()
displayed_score.speed(0)
displayed_score.color('yellow')
displayed_score.penup()
displayed_score.setposition(-140, 250)

displayed_score.write(str(score), font=style, align=
                      'left')

displayed_life = turtle.Turtle()
displayed_life.hideturtle()
displayed_life.speed(0)
displayed_life.color('yellow')
displayed_life.penup()
displayed_life.setposition(220, 250)

displayed_life.write(str(life), font=style, align=
                      'left')


def move_left():
    global count, paddle_speed
    if count % 2 == 0:
        width = bar_length
    else:
        width = bar2_length
    x = player.xcor()
    if x <= -300 + width:
        paddle_speed = 0
    else:
        paddle_speed = -1


def move_right():
    global count, paddle_speed
    if count % 2 == 0:
        width = bar_length
    else:
        width = bar2_length
    x = player.xcor()
    print(x)
    if x >= 300 - width:
        paddle_speed = 0
    else:
        paddle_speed = 1


def change_paddle():
    global count
    if count % 2 == 0:
        player.shape('paddle2')
        count += 1
    else:
        player.shape('paddle')
        count += 1


def update_paddle():
    global paddle_speed, player_move_pixel, count
    x = player.xcor()
    x += player_move_pixel * paddle_speed
    # paddle in range
    if count % 2 == 0 and \
            -300 + bar_length <= x <= 300 - bar_length:
        player.setx(x)
    elif count % 2 != 0 and \
            -300 + bar2_length <= x <= 300 - bar2_length:
        player.setx(x)
    # short paddle on the edges
    elif count % 2 == 0 and x <= -300 + bar_length:
        player.setx(-300 + bar_length)
    elif count % 2 == 0 and x >= 300 - bar_length:
        player.setx(300 - bar_length)
    # long paddle on the edges
    elif count % 2 != 0 and x <= -300 + bar2_length:
        player.setx(-300 + bar2_length)
    elif count % 2 != 0 and x >= 300 - bar2_length:
        player.setx(300 - bar2_length)




is_game_on = True

wn.listen()
wn.onkey(move_left, 'Left')
wn.onkey(move_right, 'Right')
wn.onkey(change_paddle, 'space')

count = 0
paddle_speed = 0

while life != 0:
    update_paddle()
    ball_x = ball.xcor()
    ball_y = ball.ycor()
    player_x = player.xcor()
    if ball_x >= 290 or ball_x <= -295:
        ball_move_pixel_x *= -1
    elif ball_y >= 292:
        ball_move_pixel_y *= -1
    # check if the ball hits the bar
    elif ball_y <= -270 + 10 and \
            player_x - bar[count % 2] <= ball_x <= player_x + bar[count % 2]:
        score += 100 - 70 * (count % 2)
        displayed_score.clear()
        displayed_score.write(str(score), font=style, align='left')
        ball_move_pixel_y *= -1
    elif ball_y <= -292:
        life -= 1
        displayed_life.clear()
        displayed_life.write(str(life), font=style, align='left')
        if life != 0:
            ball.setposition(0, 0)
            ball_x = 0
            ball_y = 0
    ball_x += ball_move_pixel_x
    ball_y += ball_move_pixel_y
    ball.setposition(ball_x, ball_y)

winsound.Beep(800, 1200)












