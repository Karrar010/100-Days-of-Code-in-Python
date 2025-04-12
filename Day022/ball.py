from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        self.xcor_change = 10  
        self.ycor_change = 10  
        self.ball_speed = 0.08
    def move(self):
        new_xcor = self.xcor() + self.xcor_change
        new_ycor = self.ycor() + self.ycor_change
        self.goto(new_xcor,new_ycor) # so that ball will move to top right corner

    def bounce(self):
        self.ycor_change *= -1
    def bounce_change_dir(self):
        self.xcor_change *= -1
        self.ball_speed *= 0.99
    def reset_ball(self):
        self.goto(0,0)
        self.ball_speed = 0.08
        self.bounce_change_dir()
    