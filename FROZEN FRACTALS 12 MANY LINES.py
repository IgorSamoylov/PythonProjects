from turtle import *

def drawing_arm():
    for i in range(3):
        forward(25)
        drawing_lines()
    forward(25)
    drawing_lines2()
    backward(100)
    left(30)

def drawing_lines():
    left(45)
    forward(50)
    backward(50)
    right(90)
    forward(50)
    backward(50)
    left(45)

def drawing_lines2():
    left(45)
    forward(50)
    drawing_small_lines()
    backward(50)
    right(90)
    forward(50)
    drawing_small_lines()
    backward(50)
    left(45)

def drawing_small_lines():
    left(45)
    forward(25)
    backward(25)
    right(90)
    forward(25)
    backward(25)
    left(45)

   
pensize(5)
pencolor("skyblue")
for i in range(12):
    drawing_arm()
