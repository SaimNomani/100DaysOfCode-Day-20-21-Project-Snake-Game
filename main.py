from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import random
import time


def check_wall_collision():
    """return true if head of the snake collide with wall"""
    if snake.head_of_snake.xcor() > 290 or snake.head_of_snake.xcor() < -290 or snake.head_of_snake.ycor() > 290 or snake.head_of_snake.ycor() < -290:
        score.final_score()
        return True
    return False


def check_tail_collision():
    """return true if head of snake collide with any segment of snake"""
    for segment in snake.snake_segments[1:]:
        if snake.head_of_snake.distance(segment) < 5:
            score.final_score()
            return True
    return False


# screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('#9afe2e')
screen.title("Snake Game 🐍")
screen.tracer(0)

snake = Snake()
snake_food = Food()
score = Scoreboard()
# control keys
screen.listen()
screen.onkey(snake.move_up, 'Up')
screen.onkey(snake.move_down, 'Down')
screen.onkey(snake.turn_right, 'Right')
screen.onkey(snake.turn_left, 'Left')
is_on = True
SLEEP_TIME = 0.1
while is_on:
    screen.update()
    time.sleep(SLEEP_TIME)
    snake.move()
    # detect collision with wall or tail to end the game
    if check_tail_collision() or check_wall_collision():
        is_on = False
    # detect collision with food
    if snake.head_of_snake.distance(snake_food) < 15:
        snake.extend_snake()
        snake_food.generate_food()
        score.update_score()
        if score.get_score() % 10 == 0 and SLEEP_TIME >= 0.02:
            SLEEP_TIME -= 0.02
screen.exitonclick()
