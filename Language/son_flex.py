import turtle

def shakil(s, r):  
                        # "s" bu burchaklar miqdori
    k = 1000           #Bu joyda "k" shakilning tomonlar yig`indisi.

    length = k / s
    
    t = turtle.Turtle()
    t.speed(r)
    t.color("#09f")
    for side in range(s):
        t.forward(length)
        t.right(360 / s)
    t.hideturtle()

#shakil(6, 0)

import turtle
jack = turtle.Turtle()
jack.color("#09f")
jack.speed(0)

def draw_square():
    for side in range(4):
        jack.forward(100)
        jack.right(90)

for square in range(80):
    draw_square()
    jack.forward(5)
    jack.left(5)