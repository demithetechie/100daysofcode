# import colorgram
#
# colors = colorgram.extract('image.jpg', 30)
# rgb = []
# formattedrgb = []
# for color in colors:
#     rgb.append(color.rgb)
#
# for colour in rgb:
#     red = colour[0]
#     green = colour[1]
#     blue = colour[2]
#     new_tuples = (red, green, blue)
#     formattedrgb.append(new_tuples)
#
# print(formattedrgb)

import turtle as t
from turtle import Screen

painter = t.Turtle()
s = Screen()
s.colormode(255)
painter.penup()
x = -300
y = -300
count = 0
painter.setposition(x, y)

colour_list = [
(201, 164, 112), (238, 246, 241), (152, 75, 49), (221, 201, 138),
(171, 153, 42), (56, 95, 126), (139, 31, 19), (134, 163, 184),
(197, 93, 73), (48, 121, 88), (98, 75, 77), (142, 178, 148),
(75, 41, 33), (165, 145, 156), (15, 99, 71), (234, 175, 164),
(54, 45, 47), (32, 61, 77), (145, 21, 25), (21, 83, 89),
(182, 205, 175), (85, 147, 127), (44, 66, 87), (178, 94, 98),
(222, 177, 184), (8, 68, 51), (108, 127, 151)]

for i in range(10):
    for j in range(10):
        new_colour = colour_list[count]
        painter.pendown()
        painter.dot(20, new_colour)
        painter.penup()
        x += 50
        count += 1
        painter.setposition(x, y)
        if count == len(colour_list):
            count = 0
    y += 50
    x = -300
    painter.setposition(x, y)

s.exitonclick()