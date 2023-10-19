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
screen.listen()
screen.onkey(snake.move_up,'Up')
screen.onkey(snake.move_down,'Down')
screen.onkey(snake.turn_right,'Right')
screen.onkey(snake.turn_left,'Left')
while True:
    screen.update()
    time.sleep(0.1)
    snake.move()
screen.exitonclick()