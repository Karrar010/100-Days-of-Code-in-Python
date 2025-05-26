from turtle import Turtle, Screen
import random

all_turtles = []
colors = ["black","red","blue","green","yellow","purple"]
speed = [0,2,4,6,8,10,12,14,15,17,20]

def place_turtles_at_start():
    diff_in_ycor = -60
    for index in range(6): #for multiple object instances
        diff_in_ycor+= 60
        turtle_object  =Turtle()
        turtle_object.shape("turtle")
        turtle_object.color(colors[index])
        turtle_object.penup()
        # turtle_object.color()
        turtle_object.setposition(-200,-160+diff_in_ycor)
        all_turtles.append(turtle_object)


screen   = Screen()
screen.title("Turtle Race")
screen.setup(500,400)
your_winner  = screen.textinput("Place your bet","Which Turtle will Win? \nRacers are black,red,blue,green,yellow,purple ")
place_turtles_at_start()

race_continues = True
while race_continues:
    for x in all_turtles:
        x.forward(random.choice(speed))
        if x.xcor()>= 250:    # as total x axis is 500 hundred so end of it will be 250
            race_continues = False
            if x == your_winner:
                print(f"Congrats You Win, your bet {x} won the race")
            else:
                print(f"You Lose, {x.pencolor()} won the race and your bet on {your_winner} was wrong")
                break
   

screen.exitonclick()