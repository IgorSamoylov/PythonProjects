from turtle import *

def drawing_arm():
    for i in range(4):
        forward(25)
        drawing_lines()
    backward(100)
    left(60)

def drawing_lines():
    left(45)
    forward(50)
    backward(50)
    right(90)
    forward(50)
    backward(50)
    left(45)
    
pensize(5)
pencolor("skyblue")
for i in range(6):
    drawing_arm()
