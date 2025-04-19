#1. first show the background
#2. bring the chicken to starting position
#3. Make the chicken move forward
#4. Make the chicken return to original position after reaching a certain position
#5. Create cars object
#6. Make them move in RTL direction
#7. At collision game over
#8. Each Car with their on color
#9. Make random number of cars popup in 200 to -180 region
#10. Increase the speed of cars after each level 
#11. Make level board
from turtle import Turtle,Screen
from chicken import Chicken
from vehicles import Vehicle
from level_record import Level
import time

screen = Screen()
screen.setup(width=600, height=500)
screen.bgcolor("white")
screen.tracer(0)

    
level_tracker = 0

player = Chicken()
gadi = Vehicle()
level_scorecard = Level(level_tracker)

screen.listen()
screen.onkey(fun= player.jump_forward, key= "Up")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.3)

    gadi.create_vehicles()
    gadi.car_forward()

    # level complete
    if player.ycor() > 220:
        level_tracker += 1
        level_scorecard.update_level(level_tracker)
        gadi.increase_vehicle_speed()
        player.goto(0,-220)

    #collision between chicken and car
    for car in gadi.all_vehicles:
        if player.distance(car) < 20:
            level_scorecard.collision()
            game_on = False
    
screen.exitonclick()



