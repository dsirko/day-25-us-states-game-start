from turtle import Turtle


class write_board(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 270)
        self.write("Score: 0", align="center", font=("Arial", 15, "normal")
