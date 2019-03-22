import turtle
import os


wn = turtle.Screen()
wn.setup(600, 600)
wn.bgcolor('black')


# draw board
board_pen = turtle.Turtle()
board_pen.color('blue')
board_pen.pensize(3)
board_pen.penup()
board_pen.speed(0)
board_pen.setposition(-300, -300)
board_pen.down()
for i in range(4):
    board_pen.fd(600)
    board_pen.lt(90)
board_pen.penup()
board_pen.hideturtle()

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

playerspeed = 15


# Create the enemy
enemy = turtle.Turtle()
enemy.color('red')
enemy.shape('circle')
enemy.penup()
enemy.speed(0)
enemy.setposition(-200, 250)

enemyspeed = 2


# Create the player's bullet
bullet = turtle.Turtle()
bullet.color('orange')
bullet.shape('triangle')
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.4, 0.4)
bullet.hideturtle()

bulletspeed = 20
bulletstate = 'ready'   # 'ready' and 'fire'


def move_left():
    x = player.xcor()
    x -= playerspeed
    if x < -280:
        x = -280
    player.setx(x)


def move_right():
    x = player.xcor()
    x += playerspeed
    if x > 280:
        x = 280
    player.setx(x)

def fire_bullelt():
    global  bulletsate

    x = player.xcor()
    y = player.ycor() + 10
    bullet.setposition(x, y)
    bullet.showturtle()



# Create kyboard bindings
wn.listen()
wn.onkey(move_left, 'Left')
wn.onkey(move_right, 'Right')
wn.onkey(fire_bullelt, 'space')

while True:
    x = enemy.xcor()
    x +=  enemyspeed
    enemy.setx(x)

    # Move the enemy back and down
    if enemy.xcor() > 280 or enemy.xcor() < -280:
        y = enemy.ycor()
        y -= 40
        enemy.sety(y)
        enemyspeed *= -1
    y = bullet.ycor()
    y += bulletspeed
    bullet.sety(y)
    #

    wn.update()
