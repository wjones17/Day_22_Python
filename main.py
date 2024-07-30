import time
from turtle import Screen
from ball import Ball
from player_paddle import Player

screen = Screen()
screen.setup(width=800, height=600)
screen.title("My Pong Game")
screen.bgcolor("black")
screen.tracer(0)

right_paddle = Player((350,0))
left_paddle = Player((-350,0))
ball = Ball()
game_is_on = True

screen.listen()
screen.onkeypress(key="Up", fun=right_paddle.move_up)
screen.onkeypress(key="Down", fun=right_paddle.move_down)
screen.onkeypress(key="w", fun=left_paddle.move_up)
screen.onkeypress(key="s", fun=left_paddle.move_down)

while game_is_on:
    time.sleep(0.05)
    ball.move()
    screen.update()
    # Detect ball collision on top and bottom walls
    if(ball.ycor() > 280 or ball.ycor() < -280):
        ball.bounce()
    # Detect ball collision with paddles
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.hit()

screen.exitonclick()
