# extracts rgb colors from a picture
#
# import colorgram
# colors = colorgram.extract('image.jpg', 84)
#
# rgb_colors = []
# for c in colors:
#     r = c.rgb.r
#     g = c.rgb.g
#     b = c.rgb.b
#     rgb = (r, g, b)
#     rgb_colors.append(rgb)
# print(rgb_colors)

# creating a hirst painting with the extracted rgb values
import turtle as t
import random

color_list = [(202, 166, 109), (152, 73, 47), (170, 153, 41),
(222, 202, 138), (53, 93, 124), (135, 32, 22), (132, 163, 184),
(48, 118, 88), (198, 91, 71), (16, 97, 75), (100, 73, 75),
(67, 47, 41), (147, 178, 147), (163, 142, 156), (234, 177, 165),
(55, 46, 50), (130, 28, 31), (184, 205, 174), (41, 60, 72), (83, 147, 126),
(181, 87, 90), (31, 77, 84), (47, 65, 83), (215, 177, 182), (19, 71, 63),
(175, 192, 212), (109, 123, 149), (173, 198, 205), (105, 136, 143), (72, 64, 55)]

t.colormode(255)
tim = t.Turtle()
tim.speed("fastest")
tim.penup()

tim.setheading(225)
tim.fd(308)
tim.setheading(0)


for dots in range(1, 101):
    tim.dot(20, random.choice(color_list))
    tim.fd(50)
    if dots % 10 == 0:
        tim.setheading(90)
        tim.fd(50)
        tim.setheading(180)
        tim.fd(500)
        tim.setheading(0)
