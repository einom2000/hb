import turtle
import random
import math
import winsound
import sys

# Create game window
wn = turtle.Screen()
wn.setup(700, 700)
wn.bgcolor('black')
wn.title('pingpong')

boarder_pen = turtle.Turtle()
boarder_pen.color('cyan')
boarder_pen.pensize(5)
boarder_pen.hideturtle()
boarder_pen.penup()
boarder_pen.speed(0)
boarder_pen.setposition(-300, -300)
boarder_pen.setheading(90)
boarder_pen.pendown()
for _ in range(3):
    boarder_pen.fd(600)
    boarder_pen.rt(90)

# Customize the player paddle shape
paddle_w_half = 40 / 2      # 10 units wide
paddle_h_half = 10 / 2      # 40 units high
paddle_shape = turtle.Shape("compound")
paddle_points = ((-paddle_h_half, -paddle_w_half),
                 (-paddle_h_half, paddle_w_half),
                 (paddle_h_half, paddle_w_half),
                 (paddle_h_half, -paddle_w_half))
paddle_shape.addcomponent(paddle_points, 'white')
wn.register_shape("paddle", paddle_shape)

# Customize the playerpaddle shape in super long
paddle2_w_half = 80 / 2
paddle_h_half = 10 / 2      # 40 units high
paddle_shape2 = turtle.Shape("compound")
paddle_points2 = ((-paddle_h_half, -paddle2_w_half),
                 (-paddle_h_half, paddle2_w_half),
                 (paddle_h_half, paddle2_w_half),
                 (paddle_h_half, -paddle2_w_half))
paddle_shape2.addcomponent(paddle_points2, 'red')
wn.register_shape("paddle2", paddle_shape2)

# Create player paddle
player = turtle.Turtle()
player.speed(0)
player.turtlesize(1)
player.showturtle()
player.penup()
player.shape('paddle')
player.setposition(0, -250)
player_move_pixels = 0
player_speed = 5

# Create Ball
ball = turtle.Turtle()
ball.penup()
ball.shape('circle')
ball.shapesize(0.5, 0.5)
ball_raduis = 10 * 0.5
ball_move_pixels_x = 3
ball_move_pixels_y = 2
ball.color('white')

def move_left():
    global player_move_pixels, player_speed
    player_move_pixels -= player_speed
    if player_move_pixels < (-1 * player_speed):
        player_move_pixels = -1 * player_speed


def move_right():
    global player_move_pixels
    player_move_pixels += player_speed
    if player_move_pixels > player_speed:
        player_move_pixels = player_speed


def update_paddle():
    global player_move_pixels, paddle_w_half, count
    # showing the paddle
    x = player.xcor()
    x += player_move_pixels
    print(paddle_w_half, (paddle_w_half + (count % 2) * 20), count)
    if x < -300 + (paddle_w_half + (count % 2) * 20):
        x = -300 + (paddle_w_half + (count % 2) * 20)
    if x > 300 - (paddle_w_half + (count % 2) * 20):
        x = 300 - (paddle_w_half + (count % 2) * 20)
    player.setx(x)

def super():
    global count
    count += 1
    if count % 2 == 1:
        player.shape('paddle2')
        player.speed(0)
        player.turtlesize(1)
        player.showturtle()
    else:
        player.shape('paddle')
        player.speed(0)
        player.turtlesize(1)
        player.showturtle()


def reset_ball():
    global ball_move_pixels_x, ball_move_pixels_y
    ball.setposition(0, 0)
    speed_x = random.randint(3, 4)
    speed_y = random.randint(3, 4)
    direction_x = 1
    direction_y = 1
    if random.randint(0, 100) > 50:
        direction_x = -1
    if random.randint(0, 100) > 50:
        direction_y = -1
    ball_move_pixels_x = speed_x * direction_x
    ball_move_pixels_y = speed_y * direction_y


def update_ball():
    global ball_move_pixels_x, ball_move_pixels_y, ball_raduis
    global paddle_w_half, paddle_h_half, count
    if ball.ycor() + ball_raduis >= 295:
        ball_move_pixels_y *= -1
    if ball.xcor() - ball_raduis <= -295\
            or ball.xcor() + ball_raduis >= 295:
        ball_move_pixels_x *= -1
    if ball.ycor() - ball_raduis <= -250 + paddle_h_half \
            and player.xcor() - (paddle_w_half + (count % 2) * 20) <= ball.xcor() <= \
            player.xcor() + (paddle_w_half + (count % 2) * 20):
        ball_move_pixels_y *= -1
    if ball.ycor() + ball_raduis <= -280:
        return False
    ball.setx(ball.xcor() + ball_move_pixels_x)
    ball.sety(ball.ycor() + ball_move_pixels_y)
    return True


wn.listen()
wn.onkey(move_left, 'Left')
wn.onkey(move_right, 'Right')
wn.onkey(super, 'space')

reset_ball()
is_ball_ok = True
count = 0
while is_ball_ok:
    update_paddle()
    is_ball_ok = update_ball()



