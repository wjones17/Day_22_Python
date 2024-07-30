from turtle import Turtle

class Player(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(position)

    def move_up(self):
        self.goto(self.xcor(), self.ycor() + 20)
        
    def move_down(self):
        self.goto(self.xcor(), self.ycor() - 20)