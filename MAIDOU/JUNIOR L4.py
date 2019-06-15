import turtle
import time
import random

font = 'Courier'
size = 0
style = 'bold'
colors = ['white', 'pink', 'red', 'green', 'brown', 'purple', 'blue', 'yellow', 'cyan']
length = len(colors) -1

turtle.hideturtle()
turtle.bgcolor('black')
turtle.color('yellow')

while True:
    for i in range(0, 100):
        #turtle.bgcolor(colors[i % length])
        turtle.color(colors[length - i % length])
        turtle.write('我我我!', font=(font, i, style), align='center')
        time.sleep(0.1)
        turtle.clear()

    while input('press enter!') != '':
        pass

    for i in range(100, 1, -1):
        # turtle.bgcolor(colors[i % length])
        turtle.color(colors[length - i % length])
        turtle.write('我我我!', font=(font, i, style), align='center')
        time.sleep(0.1)
        turtle.clear()

    while input('press enter!') != '':
        pass


