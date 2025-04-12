from turtle import Turtle

class Score(Turtle):
    def __init__(self,point,location):
        super().__init__()
        self.update_score(point,location)
    def update_score(self,point,location):
        self.penup() 
        self.goto(location)
        self.color("white")
        self.clear()
        self.write(f"{point}",True,align="center",font=("Arial",40,"normal"))
        self.hideturtle()

class Barrier(Turtle): 
    def __init__(self):
        super().__init__()
        self.penup() 
        self.goto(0,-300)
        self.color("white")
        self.write("\n | \n | \n | \n | \n | \n | \n | \n | \n | \n | \n | \n | \n | \n | ",True,align= "Center", font= ("Arial",30,"normal"))
        self.hideturtle()