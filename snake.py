from turtle import Turtle
coordinates = [(0, 0), (-20, 0), (-40, 0)]
dist = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
class Snake:
    def __init__(self):
        self.snake_segments = []
        self.create_snake()
    def create_snake(self):
        for coordinate in coordinates:
            self.add_to_snake(coordinate)
    def add_to_snake(self,coordinate):
        new_turtle = Turtle("square")
        new_turtle.color("white")
        new_turtle.penup()
        new_turtle.goto(coordinate)
        self.snake_segments.append(new_turtle)
    def extend(self):
        self.add_to_snake(self.snake_segments[-1].position())
    def move(self):
        for seg in range(len(self.snake_segments) - 1, 0, -1):
            x = self.snake_segments[seg - 1].xcor()
            y = self.snake_segments[seg - 1].ycor()
            self.snake_segments[seg].goto(x, y)
        self.snake_segments[0].forward(dist)
    def up(self):
        if self.snake_segments[0].heading() != DOWN:
            self.snake_segments[0].setheading(UP)
    def down(self):
        if self.snake_segments[0].heading() != UP:
            self.snake_segments[0].setheading(270)

    def right(self):
        if self.snake_segments[0].heading() !=LEFT:
            self.snake_segments[0].setheading(RIGHT)

    def left(self):
        if self.snake_segments[0].heading() != RIGHT:
            self.snake_segments[0].setheading(LEFT)

    def directions(self):
        for seg in range(0,len(self.snake_segments)):
            x = self.snake_segments[seg].xcor()
            y= self.snake_segments[seg].ycor()
            if x>250:
                self.snake_segments[seg].goto(-250, y)

            elif x< -250:
                self.snake_segments[seg].goto(250, y)
            elif y> 250:
                self.snake_segments[seg].goto(x,-250)
            elif y< -250:
                self.snake_segments[seg].goto(x,250)
