import turtle
t= turtle.Turtle()
t.speed(0)
t.width(3)
def gul(p, d):
    for b in range(p):
        t.forward(d / p)
        t.right(360 / p)

for r in ["blue", "orange", "red"]:
    t.color(r)
    for l in range(10):
        gul(5, 400)
        t.left(12)


import turtle

# Bu kod ishlaydi!

def balloon(t, color):
    t.speed(0)
    t.color(color)

    # Shar chizadi.
    for side in range(30):
        t.forward(10)
        t.left(12)

    # Shar tugunini chizadi.
    t.right(60)
    for side in range(3):
      t.forward(10)
      t.right(120)

    # Shar ipini chizadi.
    t.color("gray")
    t.right(30)
    t.forward(100)


t = turtle.Turtle()

t.penup()
t.back(100)
t.pendown()
balloon(t, "red")

t.penup()
t.home()
t.pendown()
balloon(t, "blue")

t.penup()
t.home()
t.forward(100)
t.pendown()
balloon(t, "purple")

t.hideturtle()

# This program draws a string of beads.
# Change it so that the beads' colors
# alternate:  red, blue, red, blue ...

import turtle

def bead(tur):
    tur.right(75)
    for _ in range(12):
        tur.forward(10)
        tur.left(30)
    tur.left(75)

t = turtle.Turtle()
t.speed(0)
t.width(2)

# Move to the left before starting.
t.penup()
t.back(200)
t.pendown()

# Draw ten beads.
#for n in range(10):
 #   if n%2 == 0:
  #      t.color("blue")
  #  else:
   #     t.color("red")
    #if n%6 == 5:
        #t.color("#fff")
   # bead(t)
    #t.forward(40)

import turtle
t = turtle.Turtle()
t.color("white")
t.width(1)
t.speed(0)
t.hideturtle()

def square(number):
    return number*number


for n in range(540):
    if n%5 == 0:
        t.color("#f00")
    if n%5 == 1:
        t.color("#f90")
    if n%5 == 2:
        t.color("#0f0")
    if n%5 == 3:
        t.color("#09f")
    if n%5 == 4:
        t.color("#00f")
    angle = square(28)
    t.right(143)
    t.forward(200)

import turtle
t = turtle.Turtle()
t.color("white")
t.width(1)
t.speed(0)
t.hideturtle()

def square(number):
    return number*number


for n in range(540):
    
    angle = square(n)
    t.right(angle + .5)
    t.forward(8)