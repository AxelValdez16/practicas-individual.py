# axel sebastian valdez
from turtle import *
from colorsys import *

bgcolor("black")
speed(0)
pensize(3)

h = 0

def color_random():
    global h
    color(hsv_to_rgb(h, 1, 1))
    h += 0.02

def linea(x1, y1, x2, y2):
    penup()
    goto(x1, y1)
    pendown()
    goto(x2, y2)

# A
color_random()
linea(-300, -100, -275, 100)
linea(-250, -100, -275, 100)
linea(-290, 0, -260, 0)

# X
color_random()
linea(-230, -100, -180, 100)
linea(-180, -100, -230, 100)

# E
color_random()
linea(-150, 100, -150, -100)
linea(-150, 100, -100, 100)
linea(-150, 0, -110, 0)
linea(-150, -100, -100, -100)

# L
color_random()
linea(-70, 100, -70, -100)
linea(-70, -100, -20, -100)

# V
color_random()
linea(20, 100, 45, -100)
linea(70, 100, 45, -100)

# A
color_random()
linea(100, -100, 125, 100)
linea(150, -100, 125, 100)
linea(110, 0, 140, 0)

# L
color_random()
linea(170, 100, 170, -100)
linea(170, -100, 220, -100)

# D
color_random()
linea(250, 100, 250, -100)
linea(250, 100, 300, 50)
linea(300, 50, 300, -50)
linea(300, -50, 250, -100)

# E
color_random()
linea(330, 100, 330, -100)
linea(330, 100, 380, 100)
linea(330, 0, 370, 0)
linea(330, -100, 380, -100)

# Z
color_random()
linea(410, 100, 460, 100)
linea(460, 100, 410, -100)
linea(410, -100, 460, -100)

hideturtle()
done()