from turtle import *

def drawing_arm(): 
    forward(50)
    drawing_lines()
    forward(50)
    drawing_lines()
    backward(100)
    left(30)

def drawing_lines():
    left(60)
    forward(50)
    backward(50)
    right(120)
    forward(50)
    backward(50)
    left(60)

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


    
    
pensize(5)
pencolor("skyblue")
for i in range(12):
    drawing_arm()
