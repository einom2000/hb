import turtle
import os

# Create a screen object
wn = turtle.Screen()
wn.setup(700, 700)
wn.bgcolor('black')
wn.title('I love you Mama!')

# Create Boarder
boarder_pen = turtle.Turtle()
boarder_pen.color('cyan')
boarder_pen.pensize(5)
boarder_pen.penup()
boarder_pen.speed(0)
boarder_pen.setposition(-300, -300)
boarder_pen.pendown()
for i in range(4):
    boarder_pen.fd(600)
    boarder_pen.lt(90)
boarder_pen.penup()
boarder_pen.hideturtle()

# Create Player
player = turtle.Turtle()
player.speed(0)
player.color('yellow')
player.turtlesize(1)
player.showturtle()
player.shape('triangle')
player.setheading(90)
player.penup()
player.setposition(0, -250)
player_move_pixels = 15

# Create enemy:
enemy = turtle.Turtle()
enemy.speed(0)
enemy.color('magenta')
enemy.turtlesize(1.5)
enemy.showturtle()
enemy.shape('circle')
enemy.penup()
enemy.setposition(-250, 250)
enemy_move_pixels = 2

def move_left():
    x = player.xcor()
    x -= player_move_pixels
    if x < -280:
        x = -280
    player.setx(x)

def move_right():
    x = player.xcor()
    x += player_move_pixels
    if x > 280:
        x = 280
    player.setx(x)


wn.listen()
wn.onkey(move_left, 'Left')
wn.onkey(move_right, 'Right')

while True:
    x = enemy.xcor()
    x += enemy_move_pixels
    enemy.setx(x)
    if x > 280 or x < -280:
        enemy_move_pixels *= -1





    wn.update()







