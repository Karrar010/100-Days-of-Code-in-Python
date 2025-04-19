from turtle import Turtle

class Level(Turtle):
    def __init__(self,level_no):
        super().__init__()
        self.hideturtle()
        self.goto(-270,200)
        self.update_level(level_no)
    def update_level(self,level_no):
        self.clear()
        self.write(f"Level {level_no}",align= "left" , font= ("Ariel",15,"normal"))
    def collision(self):
        self.goto(0,0)
        self.write("GAME OVER",align= "center", font= ("carrier",30,"normal"))