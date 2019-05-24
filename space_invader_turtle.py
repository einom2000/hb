import turtle
import os, sys
import random
import math


wn = turtle.Screen()
wn.setup(600, 600)
wn.bgpic('bg5.gif')
image = 'turtle.gif'
player_image = 'plane.gif'
wn.addshape(image)
wn.addshape(player_image)
# wn.register_shape('tenor.gif')



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
player.shape(player_image)
player.setheading(90)
player.penup()
player.setposition(0, -250)

playerspeed = 15


enemies = []

for i in range(10):
    # Create the enemy
    enemy = turtle.Turtle()
    enemy.color('red')
    enemy.shape(image)
    enemy.penup()
    enemy.speed(0)
    enemy.setposition(random.randint(-250, 250), random.randint(100, 250))
    # print(i * (int((600 - 300 - 60) / 5) - 60))
    enemies.append(enemy)

enemyspeed = 2


# Create the player's bullet
bullets = []
bullet_max_num = 20

for i in range(bullet_max_num):
    bullet = turtle.Turtle()
    bullet.color('orange')
    bullet.shape('triangle')
    bullet.penup()
    bullet.speed(0)
    bullet.setheading(90)
    bullet.shapesize(0.4, 0.4)
    bullet.hideturtle()
    bullets.append([bullet, {'bulletstate': 'ready', 'bulletspeed': 20}])

    # bulletspeed = 20
    # bulletstate = 'ready'   # 'ready' and 'fire'

bullet_load = 10
bullet_load_pen = turtle.Turtle()
bullet_load_pen.color('white')
bullet_load_pen.pensize(2)
bullet_load_pen.penup()
bullet_load_pen.speed(0)
bullet_load_pen.setposition(-280, 280)
# bullet_load_pen.down()
# bullet_load_pen.hideturtle()
# bullet_load_pen.write('bulllet remain:')
# bullet_load_pen.up()
bullet_load_pen.setposition(-200, 300)
bullet_load_pen.down()
bullet_load_pen.write(bullet_load)
bullet_load_pen.up()

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
    global bullets, bullet_max_num, bullet_load

    if bullet_load > 0:
        for i in range(bullet_max_num):
            if bullets[i][1].get('bulletstate')== 'ready':
                x = player.xcor()
                y = player.ycor() + 10
                bullets[i][0].setposition(x, y)
                bullets[i][0].showturtle()
                bullet_load -= 1
                bullets[i][1]['bulletstate'] = 'on_fire'
                return
    return

def is_collision(objecta, objectb):
    ax = objecta.xcor()
    ay = objecta.ycor()
    bx = objectb.xcor()
    by = objectb.ycor()
    if math.sqrt(math.pow((ax - bx), 2) + math.pow((ay - by), 2)) <= 15:
        return True
    else:
        return False

def print_bullet_load(num):
    pass

# Create keyboard bindings
wn.listen()
wn.onkey(move_left, 'Left')
wn.onkey(move_right, 'Right')
wn.onkey(fire_bullelt, 'space')

while True:
    for i in range(bullet_max_num):
        y = bullets[i][0].ycor()

        if y >= 280:
            bullets[i][0].hideturtle()
            bullets[i][0].sety(-350)
            bullets[i][1]['bulletstate'] = 'ready'

        if bullets[i][1].get('bulletstate') == 'on_fire':
            y += bullets[i][1].get('bulletspeed')
            bullets[i][0].sety(y)

    # Move the enemy back and down
    for enemy in enemies:
        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)
        if enemy.xcor() > 280 or enemy.xcor() < -280:
            for every_enemy_in_role in enemies:
                y = every_enemy_in_role.ycor()
                y -= 40
                every_enemy_in_role.sety(y)
            enemyspeed *= -1
        for i in range(bullet_max_num):
            if is_collision(enemy, bullets[i][0]):
                bullets[i][0].hideturtle()
                bullets[i][0].sety(-350)
                bullets[i][1]['bulletstate'] = 'ready'
                enemy.hideturtle()
                index = enemies.index(enemy)
                enemies.pop(index)
    if len(enemies) == 0:
        win = turtle.Turtle()
        win.hideturtle()
        win.pensize(4)
        win.color('red')
        win.write('YOU WIN !', align="center", font=("Arial", 30, "bold"))


    #

    wn.update()
