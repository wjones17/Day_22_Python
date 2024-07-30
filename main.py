from turtle import Turtle, Screen, width

screen = Screen()
screen.setup(width=800, height=600)
screen.title("My Pong Game")
screen.bgcolor("black")
screen.tracer(0)

STARTING_POSITIONS = [(350, 0), (-350, 0)]

paddle = Turtle("square")
paddle.shapesize(stretch_wid=5, stretch_len=1)
paddle.color("white")
paddle.penup()
paddle.goto(STARTING_POSITIONS[0])
game_is_on = True

def move_up():
    paddle.goto(paddle.xcor(), paddle.ycor() + 20)
    
def move_down():
    paddle.goto(paddle.xcor(), paddle.ycor() - 20)

screen.listen()
screen.onkeypress(key="Up", fun=move_up)
screen.onkeypress(key="Down", fun=move_down)

while game_is_on:
    screen.update()

screen.exitonclick()