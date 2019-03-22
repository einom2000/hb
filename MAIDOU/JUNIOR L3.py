'''from random import randint
from turtle import *

t = Turtle()
t.screen.tracer(0, 0)
t.screen.bgcolor('black')

x = 1

while x < 400:
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    w = randint(2, 7)
    a = randint(900, 1000) / 10

    colormode(255)
    width(w)
    pencolor(r, g, b)

    fd(50 + x)
    rt(a)

    x += 1

t.screen.exitonclick()
t.screen.mainloop()
'''
# import turtle
#
# turtle.setup(width=600, height=500)
# turtle.reset()
# turtle.hideturtle()
# turtle.speed(0)
# turtle.bgcolor('black')
#
# reddish  = []
# orangey  = []
# yellowy  = []
# greenish = []
# blueish  = []
# rainbow  = []
#
# for i in range(20):
#     temp_r = 1.00
#     temp_g = 0.00
#     temp_b = 0.00
#     reddish.append((temp_r, round(temp_g + i * 0.025, 2), temp_b))
# for i in range(20):
#     temp_r = 1.00
#     temp_g = 0.50
#     temp_b = 0.00
#     orangey.append((temp_r, round(temp_g + i * 0.025, 2), temp_b))
# for i in range(20):
#     temp_r = 1.00
#     temp_g = 1.00
#     temp_b = 0.00
#     yellowy.append((round(temp_r - i * 0.05, 2), temp_g, temp_b))
# for i in range(20):
#     temp_r = 0.00
#     temp_g = 1.00
#     temp_b = 0.00
#     greenish.append((temp_r, round(temp_g - i * 0.05, 2),
#                      round(temp_b + i * 0.05, 2)))
# for i in range(20):
#     temp_r = 0.00
#     temp_g = 0.00
#     temp_b = 1.00
#     blueish.append((round(temp_r + i * 0.05, 2), temp_g, temp_b))
#
# rainbow = reddish + orangey + yellowy + greenish + blueish
#
# for i in range(1000):
#     color = rainbow[i // 10]
#     turtle.color(color)
#     turtle.forward(i // 7)
#     turtle.right(98)
#
#
# turtle.exitonclick()

import argparse
import random
import shapely.geometry as geometry
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def main(args):
    # Styles
    plt.style.use("ggplot")

    # Creating figure
    fig = plt.figure()
    line, = plt.plot([], [], ".")

    # Limit axes
    plt.xlim(0, 1)
    plt.ylim(0, 1)

    # Titles
    title = "Chaos Game"
    plt.title(title)
    fig.canvas.set_window_title(title)

    # Getting data
    data = get_data(args.frames)

    # Creating animation
    line_ani = animation.FuncAnimation(
        fig=fig,
        func=update_line,
        frames=args.frames,
        fargs=(data, line),
        interval=args.interval,
        repeat=False
    )

    # To save the animation install ffmpeg and uncomment
    # line_ani.save("chaos_game.gif")

    plt.show()


def get_data(n):
    """
    Get data to plot
    """
    leg = 1
    triangle = get_triangle(leg)
    cur_point = gen_point_within_poly(triangle)
    data = []
    for _ in range(n):
        data.append((cur_point.x, cur_point.y))
        cur_point = next_point(triangle, cur_point)
    return data


def get_triangle(n):
    """
    Create right triangle
    """
    ax = ay = 0.0
    a = ax, ay

    bx = 0.5 * n
    by = 0.75 * (n ** 2)
    b = bx, by

    cx = n
    cy = 0.0
    c = cx, cy

    triangle = geometry.Polygon([a, b, c])
    return triangle


def gen_point_within_poly(poly):
    """
    Generate random point inside given polygon
    """
    minx, miny, maxx, maxy = poly.bounds
    while True:
        x = random.uniform(minx, maxx)
        y = random.uniform(miny, maxy)
        point = geometry.Point(x, y)
        if point.within(poly):
            return point


def next_point(poly, point):
    """
    Generate next point according to chaos game rules
    """
    vertices = poly.boundary.coords[:-1]  # Last point is the same as the first one
    random_vertex = geometry.Point(random.choice(vertices))
    line = geometry.linestring.LineString([point, random_vertex])
    return line.centroid


def update_line(num, data, line):
    """
    Update line with new points
    """
    new_data = zip(*data[:num]) or [(), ()]
    line.set_data(new_data)
    return line,


if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser(description="Chaos Game by Suenweek (c) 2017")
    arg_parser.add_argument("-f", dest="frames", type=int, default=1000)
    arg_parser.add_argument("-i", dest="interval", type=int, default=10)

    main(arg_parser.parse_args())