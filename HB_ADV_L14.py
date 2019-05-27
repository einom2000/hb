import turtle
import os
import random
import math
import sys
import winsound

# Create a screen object
wn = turtle.Screen()
wn.setup(700, 700)
player_plane_image = 'plane.gif'
enemy_image = 'alien.gif'
wn.addshape(player_plane_image)
wn.addshape(enemy_image)
wn.bgpic('bg5.gif')
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
player.shape(player_plane_image)
player.setheading(90)
player.penup()
player.setposition(0, -250)
player_move_pixels = 10

# Create enemies:
enemies = []
for i in range(50):
    e = turtle.Turtle()
    e.speed(0)
    e.color('magenta')
    e.turtlesize(1.5)
    e.showturtle()
    e.shape(enemy_image)
    e.penup()
    e.setposition(-250 + i * random.randint(40, 60), 250)
    enemies.append(e)

enemy_move_pixels = 2

# Create Bullet
# bullets = [[b1, temp], [b2, temp], [b3, temp]....]
bullets = []
max_bullets = 1
for i in range(max_bullets):
    b = turtle.Turtle()
    b.speed(0)
    b.color('orange')
    b.turtlesize(0.3)
    b.hideturtle()
    b.shape('triangle')
    b.setheading(90)
    b.penup()
    b.setposition(0, -400)
    temp = {'bullet_move_pixels': 30, 'bullet_status': 'ready'}
    bullets.append([b, temp])


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


def fire():
    global bullets
    for bullet in bullets:
        if bullet[1].get('bullet_status') == 'ready':
            # winsound.Beep(300,300)
            x = player.xcor()
            bullet[0].setposition(x, -245)
            bullet[0].showturtle()
            bullet[1]['bullet_status'] = 'on_fire'
            return
    return


def is_collision(a, b):   # a = (x1, y1), b = (x2, y2)
    x1 = a[0]
    y1 = a[1]
    x2 = b[0]
    y2 = b[1]
    dis = math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))
#dis = math.sqrt(math.pow((a[0] - b[0]), 2) + math.pow((a[1] - b[1]), 2))
    if dis <= 30:
        return True
    else:
        return False

wn.listen()
wn.onkey(move_left, 'Left')
wn.onkey(move_right, 'Right')
wn.onkey(fire, 'space')

while True:
    for enemy in enemies:
        x = enemy.xcor()
        x += enemy_move_pixels
        enemy.setx(x)
        if x > 280 or x < -280:
            enemy_move_pixels *= -1
            enemy_move_pixels += 3 * enemy_move_pixels / abs(enemy_move_pixels)
            for every_enemy in enemies:
                y = every_enemy.ycor()
                y -= 50
                every_enemy.sety(y)

    for bullet in bullets:
        if bullet[1].get('bullet_status') == 'on_fire':
            y = bullet[0].ycor()
            y += bullet[1].get('bullet_move_pixels')
            bullet[0].sety(y)
        if bullet[0].ycor() >= 300:
            bullet[1]['bullet_status'] = 'ready'
            bullet[0].hideturtle()
            bullet[0].sety(-400)

# check if bullet collides the enemy
    for enemy in enemies:
        a = (enemy.xcor(), enemy.ycor())
        for bullet in bullets:
            b = (bullet[0].xcor(), bullet[0].ycor())
            if is_collision(a, b):
                bullet[0].hideturtle()
                bullet[0].sety(-400)
                bullet[1]['bullet_status'] = 'ready'
                winsound.Beep(1200, 300)
                enemy.hideturtle()
                indx = enemies.index(enemy)
                enemies.pop(indx)

    if len(enemies) == 0:
        win = turtle.Turtle()
        win.hideturtle()
        win.pensize(4)
        win.color('red')
        win.write('YOU WIN !', align='center',
                  font=('Arial', 30, 'bold'))
        winsound.Beep(1600, 1000)
        sys.exit()

    wn.update()







