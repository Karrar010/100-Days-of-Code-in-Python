from turtle import Turtle,Screen

pencil = Turtle() #let the Turtle object name be pencul for this project
pencil.color("green")
pencil.setheading(90)
screen = Screen()

def move_forward():
    pencil.forward(20)
def backward():
    pencil.backward(20)
def turn_right():  #turn right or clockwise motion
    pencil.setheading(pencil.heading()-20)
def turn_left():
    pencil.setheading(pencil.heading()+20)
def cancel():
    pencil.reset()
screen.listen()  
screen.onkey(key = "Up",fun = move_forward) #when func is passed as argument to another function we dont write 
                                           #the () with it as the parenthesis () triggers the function there
                                           
screen.onkey(key = 'Down',fun = backward)    # This is the HIGHER ORDER FUNCTION concept where we pass a func into 
                                            # a func where a func requires another func
screen.onkey(key = 'Right',fun = turn_right) # here we are passing the keyword args i.e key  = "" , func = func()
screen.onkey(key = 'Left',fun = turn_left)
screen.onkey(key = 'c',fun = cancel)

screen.exitonclick()