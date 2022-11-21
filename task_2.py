from turtle import *
from random import randint


def bar(n):
    for i in range(2):
        forward(20)
        left(90)
        forward(n)
        left(90)


penup()
backward(470)
pendown()
for i in range(20):

    bar(70 + i * 20 + randint(-10, 80))
    penup()
    forward(50)
    pendown()


exitonclick()

