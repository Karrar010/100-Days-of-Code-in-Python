from turtle import Turtle


class Paddle(Turtle):
    def __init__ (self,player_location):
        super().__init__()
        # self.speed("fastest")
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid= 5, stretch_len= 1)
        self.penup() 
        # self.setheading(MOVING_UP)   # we mov left right then downward same is the case for all the others
        self.goto(player_location)
    def upward_player(self):
        new_y = self.ycor() + 30
        self.goto(self.xcor(),new_y)
    def downward_player(self):
        new_y = self.ycor() - 30
        self.goto(self.xcor(),new_y)