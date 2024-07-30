from turtle import Screen
from player_paddle import Player

screen = Screen()
screen.setup(width=800, height=600)
screen.title("My Pong Game")
screen.bgcolor("black")
screen.tracer(0)

player_paddle= Player()
game_is_on = True

screen.listen()
screen.onkeypress(key="Up", fun=player_paddle.move_up)
screen.onkeypress(key="Down", fun=player_paddle.move_down)

while game_is_on:
    screen.update()

screen.exitonclick()