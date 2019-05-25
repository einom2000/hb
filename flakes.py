# Python Turtle - Spirograph - www.101computing.net/python-turtle-spirograph/
import turtle
from math import cos, sin
from time import sleep
import random
import keyboard

def get_random_color():
    R = random.randrange(0, 257, 10) / 255
    B = random.randrange(0, 257, 10) / 255
    G = random.randrange(0, 257, 10) / 255
    myPen.color((R, G, B))

while True:
    turtle.tracer(0)
    window = turtle.Screen()
    window.bgcolor("#FFFFFF")

    mySpirograph = turtle.Turtle()
    mySpirograph.hideturtle()
    # mySpirograph.tracer(0)
    mySpirograph.speed(0)
    mySpirograph.pensize(2)


    myPen = turtle.Turtle()
    myPen.hideturtle()
    # myPen.tracer(0)
    myPen.speed(0)
    myPen.pensize(3)
    get_random_color()

    change_pattern = False
    R = random.randint(125, 200)
    r = random.randint(50, 120)
    d = random.randint(120, 250)

    angle = 0

    myPen.penup()
    myPen.goto(R - r + d, 0)
    myPen.pendown()

    theta = 0.2
    steps = int(6 * 3.14 / theta)



    while not change_pattern:
        get_random_color()
        for t in range(0, steps):
            if keyboard.is_pressed(' '):
                change_pattern = True
            mySpirograph.clear()
            mySpirograph.penup()
            mySpirograph.setheading(0)
            mySpirograph.goto(0, -R)
            mySpirograph.color("#999999")
            mySpirograph.pendown()
            mySpirograph.circle(R)
            angle += theta

            x = (R - r) * cos(angle)
            y = (R - r) * sin(angle)
            mySpirograph.penup()
            mySpirograph.goto(x, y - r)
            mySpirograph.color("#222222")
            mySpirograph.pendown()
            mySpirograph.circle(r)
            mySpirograph.penup()
            mySpirograph.goto(x, y)
            mySpirograph.dot(5)

            x = (R - r) * cos(angle) + d * cos(((R - r) / r) * angle)
            y = (R - r) * sin(angle) - d * sin(((R - r) / r) * angle)
            mySpirograph.pendown()
            mySpirograph.goto(x, y)
            # mySpirograph.setheading((R-r)*degrees(angle)/r)
            # mySpirograph.forward(d)
            mySpirograph.dot(5)
            myPen.goto(mySpirograph.pos())

            mySpirograph.getscreen().update()
            sleep(0.05)

    sleep(0.5)
    # Hide Spirograph
    mySpirograph.clear()
    mySpirograph.getscreen().update()
    window.clear()



