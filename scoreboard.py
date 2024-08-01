from turtle import Turtle
STYLE = ('Courier', 50, 'italic')

class Scoreboard(Turtle):


    def __init__(self):
        super().__init__()
        self.left_player_points = 0
        self.right_player_points = 0
        self.update_points()
        self.draw_net()
        self.hideturtle()

    def update_points(self):
        self.clear()
        self.color("yellow")
        self.penup()
        self.goto(-100, 200)
        self.write(f"{self.left_player_points}", font=STYLE)
        self.goto(50, 200) 
        self.write(f"{self.right_player_points}", font=STYLE)

    def draw_net(self):
        tim = Turtle()
        positions = [(0,300), (0,200), (0,100), (0,0), (0,-100), (0,-200), (0,-300)]
        tim.shape("square")
        tim.shapesize(stretch_wid=3, stretch_len=0.1)
        tim.color("red")
        for position in positions:
            tim.penup()
            tim.goto(position)
            tim.stamp()

    def game_over(self, winner):
        tim = Turtle()
        tim.color("red")
        self.penup()
        self.goto(-110, 100)
        self.write("Game Over", font=('Courier', 30, 'italic'))
        self.goto(-300, 20)
        self.write(f"The winner is {winner} player!", font=('Courier', 30, 'italic'))

    def reset(self):
        self.left_player_points = 0
        self.right_player_points = 0
        self.update_points()
        self.draw_net()
        self.hideturtle()

        