import turtle
import os
import random
import math
import sys
import winsound
import keyboard

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

display_score = turtle.Turtle()
display_score.hideturtle()
display_score.speed(0)
display_score.color('white')
display_score.penup()
display_score.setposition(-140, 250)


turtle.color('white')
turtle.penup()
turtle.hideturtle()
turtle.goto(-250, 250)
turtle.write('SCORE=', font=style, align="left")
turtle.goto(130, 250)
turtle.write('LIFE=', font=style, align='left')

life_left = 3

display_life = turtle.Turtle()
display_life.hideturtle()
display_life.speed(0)
display_life.color('white')
display_life.penup()
display_life.setposition(220, 250)
display_life.write(str(life_left), font=style, align='left')


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


def wait_for_start():
    turtle.color
    while True:

        pass
    pass

# is_game_on = True

wn.listen()
wn.onkey(move_left, 'Left')
wn.onkey(move_right, 'Right')
wn.onkey(change_paddle, 'space')

count = 0
paddle_speed = 0

wait_for_start()

while life_left != 0:

    update_paddle()
    ball_x = ball.xcor()
    ball_y = ball.ycor()
    player_x = player.xcor()
    display_score.write(str(score), font=style, align="left")
    if ball_x >= 290 or ball_x <= -295:
        ball_move_pixel_x *= -1
    elif ball_y >= 292:
        ball_move_pixel_y *= -1

    # half player thickness and half ball radius = 5?
    elif ball_y <= -270 + 10 and count % 2 == 0 and \
            player_x - bar_length / 2 <= ball_x <= player_x + bar_length:
        ball_move_pixel_y *= -1
        score += 100
        display_score.clear()
    elif ball_y <= -270 + 10 and count % 2 != 0 and \
            player_x - bar2_length / 2 <= ball_x <= player_x + bar2_length:
        ball_move_pixel_y *= -1
        score += 30
        display_score.clear()
    elif ball_y <= -292:
        life_left -= 1
        display_life.clear()
        display_life.write(str(life_left), font=style, align='left')
        if life_left != 0:
            ball.setposition(0, 0)
            ball_x = ball.xcor()
            ball_y = ball.ycor()
            wait_for_start()
    ball_x += ball_move_pixel_x
    ball_y += ball_move_pixel_y
    ball.setposition(ball_x, ball_y)

turtle.color('red')
turtle.goto(-90,0)
style = ('Courier', 30, 'bold')
turtle.write('GAME OVER!', font=style, align='left')
winsound.Beep(800, 1200)

while not keyboard.is_pressed(' '):
    pass

sys.exit()












