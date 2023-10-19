from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import random
import time

# screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Snake Game 🐍")
screen.tracer(0)

snake = Snake()
snake_food = Food()
score=Scoreboard()
screen.listen()
screen.onkey(snake.move_up, 'Up')
screen.onkey(snake.move_down, 'Down')
screen.onkey(snake.turn_right, 'Right')
screen.onkey(snake.turn_left, 'Left')
while True:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head_of_snake.distance(snake_food) < 15:
        score.update_score()
        snake_food.generate_food()
screen.exitonclick()
