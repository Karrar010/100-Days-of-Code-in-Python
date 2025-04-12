from turtle import Turtle
import random

class khana(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len = 0.5, stretch_wid = 0.5) #this helps sizing th dot shaped food 
        self.color("blue")
        self.speed("fastest") 
        self.new_location()
    
    def new_location(self):
        random_xcor = random.randint(-280,280) # since it is a 600,600 screen so , x axis from -300 to 300
        random_ycor = random.randint(-280,280) # y axis from -300 to 300 so w write from -280,280
        self.goto(random_xcor,random_ycor)
