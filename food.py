import random
from turtle import Turtle  # https://docs.python.org/3/library/turtle.html
from random import Random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.refresh()

    def refresh(self):
        x_cor = random.randint(-280, 280)
        y_cor = random.randint(-280, 280)
        self.setpos(x_cor, y_cor)
