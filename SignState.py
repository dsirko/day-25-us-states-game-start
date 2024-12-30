from turtle import Turtle
FONT = ("Arial", 10, "normal")
ALIGNMENT = "center"


class SignState(Turtle):
    def __init__(self, name, x, y):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("red")
        self.goto(x, y)
        self.name = name

    def write_state(self):
        self.write(f"{self.name}", align=ALIGNMENT, font=FONT)

    def reset(self):
        self.clear()
        self.write_state()
