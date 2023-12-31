from turtle import Turtle
import random
from snake import Snake
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color("red")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed('fastest')
        self.generate_food()


    def generate_food(self):
        random_x = random.randint(-270, 270)
        random_y = random.randint(-270, 270)
        self.goto(random_x, random_y)
