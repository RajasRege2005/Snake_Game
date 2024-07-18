from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard


screen = Screen()
screen.title("Snake game")
screen.setup(500,500)
screen.bgcolor("black")
screen.tracer(0)


snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")

is_on = True
while is_on:
    screen.update()
    time.sleep(0.07)
    snake.move()
    snake.directions()
    if snake.snake_segments[0].distance(food) < 15:
        food.redo()
        snake.extend()
        score.score_increase()
    for segment in snake.snake_segments[1:]:
        if snake.snake_segments[0].distance(segment) < 10:
            is_on = False
            score.game_over()


screen.exitonclick()







