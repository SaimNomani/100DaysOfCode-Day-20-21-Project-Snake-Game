from turtle import Turtle, Screen

ALIGNMENT = 'center'
FONT = ('Courier', 20, 'bold')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pencolor('#004000')
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

    def final_score(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"Game Over!!\n\n", move=False, align=ALIGNMENT, font=FONT)
        self.write(f" Final Score: {self.current_score}", move=False, align='center', font=FONT)
