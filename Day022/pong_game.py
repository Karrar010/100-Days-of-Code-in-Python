from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Score,Barrier
import time


player1_location = (-350,0)
player2_location = (350,0)
player1_Score = 0   
player2_Score = 0   
score1_location = (-40,220)
score2_location = (40,220) 

screen = Screen()
screen.bgcolor("black")
screen.setup(width = 800,height = 600)
screen.title("PONG GAME")
screen.tracer(0)

player1 = Paddle(player1_location)
player2 = Paddle(player2_location)

ball = Ball()

p1_score = Score(player1_Score,score1_location)
p2_score = Score(player2_Score,score2_location)
net = Barrier()





screen.listen()
screen.onkey(fun= player1.upward_player, key="f")
screen.onkey(fun= player1.downward_player, key="v")
screen.onkey(fun= player2.upward_player, key="h")
screen.onkey(fun= player2.downward_player, key="b")


game_on = True
while game_on:
    time.sleep(ball.ball_speed) # slows the ball movement and makes it visible
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()
        print("wall bounce")

    if ball.distance(player1) < 60 and ball.xcor() < -340 or ball.distance(player2) <  60 and ball.xcor() > 340:
        print("paddle bounce")
        ball.bounce_change_dir()

    if ball.xcor() > 380:
        ball.reset_ball()
        player1_Score += 1
        p1_score.update_score(player1_Score,score1_location)
    elif ball.xcor() < -380:
        ball.reset_ball()
        player2_Score += 1
        print("ball start dir change")
        p2_score.update_score(player2_Score,score2_location)

screen.exitonclick()