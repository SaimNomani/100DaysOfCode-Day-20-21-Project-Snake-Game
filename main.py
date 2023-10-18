from turtle import Turtle, Screen
import time
# screen setup
screen=Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Snake Game 🐍")
initial_positions=[(0,0), (-20,0), (-40,0)]
snake_segments=[]
screen.tracer(0)
for position in initial_positions:
    new_segment=Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    snake_segments.append(new_segment)
while True:
    screen.update()
    time.sleep(0.1)
    for segment in range(len(snake_segments)-1, 0, -1):
        new_x=snake_segments[segment-1].xcor()
        new_y=snake_segments[segment-1].ycor()
        snake_segments[segment].goto(new_x,new_y)
    snake_segments[0].forward(10)





screen.exitonclick()