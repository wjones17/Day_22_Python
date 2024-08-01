import time
from turtle import Screen
from scoreboard import Scoreboard
from ball import Ball
from player_paddle import Player

screen = Screen()
screen.setup(width=800, height=600)
screen.title("My Pong Game")
screen.bgcolor("black")
screen.tracer(0)

right_paddle = Player((350,0))
left_paddle = Player((-350,0))
scoreboard = Scoreboard()
ball = Ball()
game_is_on = True
ball_is_moving = False

def reset_game():
    global right_paddle, left_paddle, scoreboard, game_is_on, screen, ball
    screen.clear()
    screen.title("My Pong Game")
    screen.bgcolor("black")
    screen.tracer(0)
    right_paddle = Player((350,0))
    left_paddle = Player((-350,0))
    ball = Ball()
    scoreboard = Scoreboard()
    screen.update()
    screen.listen()
    bind_keys()
    game_is_on = True
    game_loop()

def bind_keys():
    screen.onkeypress(key="Up", fun=right_paddle.move_up)
    screen.onkeypress(key="Down", fun=right_paddle.move_down)
    screen.onkeypress(key="w", fun=left_paddle.move_up)
    screen.onkeypress(key="s", fun=left_paddle.move_down)
    screen.onkeypress(key="space", fun=ball_Start)
    screen.onkeypress(key="r", fun=reset_game)

def ball_Start():
    global ball_is_moving
    ball_is_moving = True

def play_game():
    global ball_is_moving
    if ball_is_moving:
        ball.move()
    # Detect ball collision on top and bottom walls
        if(ball.ycor() > 280 or ball.ycor() < -280):
            ball.bounce()
        # Detect ball collision with paddles
        if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
            ball.hit()
        elif ball.xcor() > 380:
            scoreboard.left_player_points += 1
            scoreboard.update_points()
            ball_is_moving = False
            ball.reset()
        elif ball.xcor() < -380:
            scoreboard.right_player_points += 1
            scoreboard.update_points()
            ball_is_moving = False
            ball.reset()

screen.listen()
bind_keys()

def game_loop():
    global ball_is_moving, game_is_on, scoreboard, screen
    while game_is_on:
        time.sleep(0.05)
        play_game()
        screen.update()
        if scoreboard.left_player_points == 2:
            ball_is_moving = False
            game_is_on = False
            scoreboard.game_over("left")
        elif scoreboard.right_player_points == 2:
            ball_is_moving = False
            game_is_on = False
            scoreboard.game_over("right")

game_loop()
    



screen.exitonclick()
