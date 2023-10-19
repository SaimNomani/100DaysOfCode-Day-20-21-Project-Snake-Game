from turtle import Turtle, Screen
from snake import Snake
import time
# screen setup
screen=Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Snake Game 🐍")
screen.tracer(0)

snake=Snake()

while True:
    screen.update()
    time.sleep(0.1)
    snake.move()
screen.exitonclick()