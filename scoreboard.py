from turtle import Turtle, Screen

ALIGNMENT = 'center'
FONT = ('Arial', 20, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pencolor('white')
        self.current_score = 0
        self.penup()
        self.goto(0, 260)
        self.generate_scoreboard()

    def generate_scoreboard(self):
        self.write(f"Score: {self.current_score}", move=False, align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.clear()
        self.current_score += 1
        self.generate_scoreboard()
