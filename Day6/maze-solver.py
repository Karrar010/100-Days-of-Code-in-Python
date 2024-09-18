# This code was for an online platform maze solver

def turn_right():
    turn_left()
    turn_left()
    turn_left()
while not at_goal():
    if wall_in_front():
        if right_is_clear():
            turn_right()
            move()
    if wall_on_right() and wall_in_front():
        turn_left()
        if wall_in_front():
            turn_left()
            move()   
    elif front_is_clear() and right_is_clear():
        turn_right()
        move()
    elif front_is_clear(): 
        move()

