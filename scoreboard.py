from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(x=0, y=267)
        self.write(arg=f"Score: {self.score} ", align=ALIGNMENT, font=FONT)
        self.hideturtle()

    def update_scoreboard(self):
        self.write(arg=f"score: {self.score} ", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()