from turtle import Turtle
MOVE_DISTANCE = 20
MOVING_UP = 90
MOVING_RIGHT = 0
MOVING_LEFT = 180
MOVING_DOWN = 270

STARTING_POSITION = [(0,0),(-20,0),(-40,0)]
class Snake:
    def __init__(self) :
        self.all_3_squares_for_snake = []
        self.create_snake()
        self.head = self.all_3_squares_for_snake[0]

    def create_snake(self):
        for x in STARTING_POSITION:
            self.add_square_to_snake(x)

    def add_square_to_snake(self,position):
        nagin = Turtle()
        nagin.shape("square")
        nagin.color("white")
        nagin.penup()
        nagin.goto(position)
        self.all_3_squares_for_snake.append(nagin)
    
    def reset_snake(self): #after gameover remove the previous snake and start with a new snake
        for x in self.all_3_squares_for_snake:
            # x.goto(1000,1000) #random location outside of screen
            x.hideturtle() #both can be used to remove previous snake
            #this proess is similar to def __init__ func
        self.all_3_squares_for_snake.clear()
        self.create_snake()
        self.head = self.all_3_squares_for_snake[0] 

    def extend_snake(self):
        self.add_square_to_snake(self.all_3_squares_for_snake[len(self.all_3_squares_for_snake)-1].position()) #through this we add new square to th tail/lastsquare of snake

    def move(self):
            for x in range(len(self.all_3_squares_for_snake)-1,0,-1): # from 2,1 jumping by 1 step
                x_cor = self.all_3_squares_for_snake[x-1].xcor()   # keeping track of the 1,0 square coordinates remember (0,0) is 0 and (-20,0) is 1
                y_cor = self.all_3_squares_for_snake[x-1].ycor()
                self.all_3_squares_for_snake[x].goto(x_cor,y_cor)  #making the 1,2 sqaur to follow the path of 0 and 1 squares
            self.head.forward(MOVE_DISTANCE)   #since 2nd and 3rd squares are following square 1st and 2nd, 1st needs to make som movements
    
    def upward(self):
        if self.head.heading() != MOVING_DOWN: # because in snake game when moving up we can move downwards instead
            self.head.setheading(MOVING_UP)   # we mov left right then downward same is the case for all the others
    def downward(self):
        if self.head.heading() != MOVING_UP:  # through this condition the snake cant go back of itself
            self.head.setheading(MOVING_DOWN)
    def right(self):  
        if self.head.heading() != MOVING_LEFT:
            self.head.setheading(MOVING_RIGHT)
    def left(self):
        if self.head.heading() != MOVING_RIGHT:
            self.head.setheading(MOVING_LEFT)
