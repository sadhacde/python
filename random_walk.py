import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = (r, g, b)
    return rgb


colors = [
    'lightpink', 'lightcoral', 'lightseagreen', 'lightskyblue',
    'lightgreen', 'lightsteelblue', 'lightblue', 'lightcyan',
    'lightgray', 'lightgrey', 'lightpink', 'lightsalmon',
    'lightsteelblue', 'lightyellow', 'lime', 'limegreen'
    ]
directions = [0, 90, 180, 360]
sizes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
tim.pensize(15)
tim.speed("fastest")

for _ in range(200):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))
