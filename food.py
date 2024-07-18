from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5,0.5)
        self.color("blue")
        self.speed("fastest")
        x = random.randint(-230,230)
        y = random.randint(-230,230)
        self.goto(x,y)
    def redo(self):
        x = random.randint(-230, 230)
        y = random.randint(-230, 230)
        self.goto(x, y)
