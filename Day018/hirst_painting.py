from turtle import Turtle,Screen
import random
tim_the_turtle = Turtle()

# Can take colour out of images
# import colorgram #library helpful in extracting colors from an image 
# colors = colorgram.extract("image.jpg",10) #this extract the top 10 colors from the image
# rgb_colors = []
# for x in colors:
#     r = x.rgb.r 
#     g  = x.rgb.g 
#     b  = x.rgb.b 
#     new_colors = (r,g,b)
#     rgb_colors.append(new_colors)

# print(rgb_colors) #Now remove the top colors closest to (255,255,255) as they all resemble white
# color_list = rgb_colors

color_list = ["red","blue","green","purple","orange","pink","violet","black","yellow"]

tim_the_turtle.penup()
tim_the_turtle.setposition(-200,-100)
FIXED_XCOR = tim_the_turtle.xcor()
tim_the_turtle.speed("fastest")
# print(tim_the_turtle.position())
tim_the_turtle.pendown()
def draw_hirst_painting(length,height):
    for x in range(height):
        for y in range(length):
            tim_the_turtle.color(random.choice(color_list))
            tim_the_turtle.dot(20,random.choice(color_list))
            tim_the_turtle.penup()
            tim_the_turtle.forward(50)
            tim_the_turtle.pendown()
        if x==height-1:#we remove the turtle after making 100 dots
            tim_the_turtle.hideturtle() #you can also get rid of the turtle from the start of painting if you wish   x goes from 0 to 9 so height - 1
        # print(x)
        tim_the_turtle.penup()
        tim_the_turtle.setposition(FIXED_XCOR,tim_the_turtle.ycor()+40) #this will help jumping up after each horizontal movement right above the dots in parallel 

draw_hirst_painting(10,10)
#you could add a condition for changing the diameter of the dot using if 
#conditional statements when the number of dots is low increase the diameter of dots vice versa

screen = Screen()
screen.exitonclick()