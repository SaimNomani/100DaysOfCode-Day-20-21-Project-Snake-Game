from turtle import Turtle

INITIAL_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
SNAKE_MOVE_DIST = 10
UP=90
DOWN=270
RIGHT=0
LEFT=180


class Snake:
    def __init__(self):
        self.snake_segments = []
        self.create_snake()
        self.head_of_snake = self.snake_segments[0]

    def create_snake(self):
        for position in INITIAL_POSITIONS:
            new_segment = Turtle("square")
            new_segment.color("#4d7f17")
            new_segment.penup()
            new_segment.goto(position)
            self.snake_segments.append(new_segment)

    def move(self):
        for segment in range(len(self.snake_segments) - 1, 0, -1):
            new_x = self.snake_segments[segment - 1].xcor()
            new_y = self.snake_segments[segment - 1].ycor()
            self.snake_segments[segment].goto(new_x, new_y)
        self.head_of_snake.forward(SNAKE_MOVE_DIST)
    def get_head_of_snake(self):
        return self.head_of_snake

    def move_up(self):
        if self.head_of_snake.heading() != DOWN:
            self.head_of_snake.setheading(UP)

    def move_down(self):
        if self.head_of_snake.heading() != UP:
            self.head_of_snake.setheading(DOWN)

    def turn_right(self):
        if self.head_of_snake.heading() != LEFT:
            self.head_of_snake.setheading(RIGHT)

    def turn_left(self):
        if self.head_of_snake.heading() != RIGHT:
            self.head_of_snake.setheading(LEFT)
