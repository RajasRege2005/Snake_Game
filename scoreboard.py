from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.value = 0
        self.penup()
        self.color("white")
        self.goto(0,210)
        self.write(f"Score = {self.value}",False, align="center",font=("Arial",16,"normal"))
        self.hideturtle()
    def update(self):
        self.write(f"Score = {self.value}", False, align="center", font=("Arial", 16, "normal"))
    def score_increase(self):
        self.value+=1
        self.clear()
        self.write(f"Score = {self.value}", False, align="center", font=("Arial", 16, "normal"))
    def game_over(self):
        self.goto(0,0)
        self.write(arg="GAME OVER",move=False,align="center",font=("Arial",16,"bold"))