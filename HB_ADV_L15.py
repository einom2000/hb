import turtle, random, sys, math, os, winsound

# Creat Screen Obj.
wn = turtle.Screen()
wn.setup(700, 700)
wn.bgcolor('black')
wn.title('Ping Pong')
# wn.tracer(0)

# Create Boarder
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

# Create a Ball
ball = turtle.Turtle()
ball.color('white')
ball.speed(0)
ball.shape('circle')
ball.turtlesize(.5)
ball.showturtle()
ball.penup()
ball.setposition(0, 0)

ball_move_pixel_x = 5
ball_move_pixel_y = 3

#Create a Player Bar
bar_length = 40
player = turtle.Turtle()
player.speed(0)
player.color('white')
player.hideturtle()
player.pensize(10)
player.penup()
player.setposition(-20, -90)
player.pendown()
player.fd(bar_length)
player.penup()
player_move_pixel = 10


def move_left():
    x = player.xcor() - bar_length
    player.pendown()
    player.color('black')
    player.back(player_move_pixel)
    player.penup()
    player.setx(x)
    player.pendown()
    player.color('white')
    player.back(player_move_pixel)
    player.penup()
    player.setx(x + bar_length - player_move_pixel)
    pass


def move_right():
    pass


is_game_on = True

wn.listen()
wn.onkey(move_left, 'Left')
wn.onkey(move_right, 'Right')

while is_game_on:
    ball_x = ball.xcor()
    ball_y = ball.ycor()
    if ball_x > 290 or ball_x < -290:
        ball_move_pixel_x *= -1
    elif ball_y > 292:
        ball_move_pixel_y *= -1
    elif ball_y < -292:
        is_game_on = False
    ball_x += ball_move_pixel_x
    ball_y += ball_move_pixel_y
    ball.setposition(ball_x, ball_y)

winsound.Beep(800, 1200)


