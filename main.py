from turtle import Screen
from player_paddle import Player

screen = Screen()
screen.setup(width=800, height=600)
screen.title("My Pong Game")
screen.bgcolor("black")
screen.tracer(0)

right_paddle= Player((350,0))
left_paddle= Player((-350,0))
game_is_on = True

screen.listen()
screen.onkeypress(key="Up", fun=right_paddle.move_up)
screen.onkeypress(key="Down", fun=right_paddle.move_down)
screen.onkeypress(key="w", fun=left_paddle.move_up)
screen.onkeypress(key="s", fun=left_paddle.move_down)

while game_is_on:
    screen.update()

screen.exitonclick()