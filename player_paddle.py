from turtle import Turtle

STARTING_POSITIONS = [(350, 0), (-350, 0)]

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(STARTING_POSITIONS[0])

    def move_up(self):
        self.goto(self.xcor(), self.ycor() + 20)
        
    def move_down(self):
        self.goto(self.xcor(), self.ycor() - 20)