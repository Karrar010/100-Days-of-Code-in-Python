from turtle import Turtle

class Score_Board(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("./Day24/highscoredatalist.txt") as highscore_data: 
            self.high_score = int(highscore_data.read()) #initially add 0 to the file manually
        self.color("white")
        self.penup()
        self.goto(0,270) #position the score board to th top of center
        self.hideturtle() # the turtle shows up in position of score : 0 text
        self.update_score()
    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}  HighScore: {self.high_score}",True,align = "center", font = ("Arial",18,"normal"))
          
    def increase_score(self):
        self.score +=1
        self.goto(0,270)
        self.clear()
        self.write(f"Score: {self.score}  HighScore: {self.high_score}",True,align = "center", font = ("Arial",18,"normal"))

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("./Day24/highscoredatalist.txt", mode= "w") as highscore_data:
                highscore_data.write(f"{self.high_score}")
                
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0,270) #position the score board to th top of center
        self.hideturtle() # the turtle shows up in position of score : 0 text
        self.update_score()
    def game_over(self):
        self.goto(0,0)
        self.color("red")
        self.write("Game Over.",True,align = "center", font = ("Arial",20,"normal"))  