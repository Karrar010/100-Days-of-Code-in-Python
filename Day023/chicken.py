from turtle import Turtle

class Chicken(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.left(90)
        self.penup()
        self.goto(0,-220) 
    def jump_forward(self):
        self.forward(20)