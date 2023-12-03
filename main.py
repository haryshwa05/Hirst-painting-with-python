

# import colorgram


# rgb = []
# colors = colorgram.extract("example.jpg", 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb.append((r, g, b))
# print(rgb)

#above part of the program is to get the colors needed from another example hirst painting

import turtle as tr
import random


tr.colormode(255)
color_list = [(213, 154, 96), (52, 107, 132), (179, 77, 31), (202, 142, 31), (115, 155, 171), (124, 79, 99), (122, 175, 156), (229, 236, 239), (226, 198, 131), (242, 247, 244), (192, 87, 108), (11, 50, 64), (55, 38, 19), (45, 168, 126), (47, 127, 123), (200, 121, 143), (168, 21, 29), (228, 92, 77), (244, 162, 160), (38, 32, 35), (2, 25, 24), (78, 147, 171), (170, 23, 18), (19, 79, 90), (101, 126, 158), (235, 166, 171), (177, 204, 185), (49, 62, 84)]

turt = tr.Turtle()
turt.speed("fastest")
turt.penup()
turt.hideturtle()



turt.setheading(225)
turt.forward(300)
turt.setheading(0)
no_of_dots = 100

for count in range(1, no_of_dots + 1):
    turt.dot(20, random.choice(color_list))
    turt.forward(50)

    if count % 10 == 0:
        turt.setheading(90)
        turt.forward(50)
        turt.setheading(180)
        turt.forward(500)
        turt.setheading(0)




screen = tr.Screen()
screen.exitonclick()