from turtle import Turtle, Screen
import random

tim = Turtle()
pastel_colors = [
    'lightpink', 'lightcoral', 'lightseagreen', 'lightskyblue',
    'lightgreen', 'lightsteelblue', 'lightblue', 'lightcyan',
    'lightgray', 'lightgrey', 'lightpink', 'lightsalmon',
    'lightsteelblue', 'lightyellow', 'lime', 'limegreen'
]

nsides = 3
while nsides <= 9:
    for r in range(nsides):
        tim.forward(50)
        tim.right(360/nsides)
    nsides += 1
    tim.color(random.choice(pastel_colors))

screen = Screen()
screen = exitonclick()
