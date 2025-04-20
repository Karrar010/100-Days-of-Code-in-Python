import turtle
import pandas as pd
# 1. First of all set background and screen details
# 2. Take Screen input at a certain position 
# 3. at each input, match the input with the csv file
# 4.create a turtle set it at the corresponding location. 

TOTAL_SCORE = 50
player_score = 0
data = pd.read_csv("./Day25/us-states-game-start/50_states.csv")
screen = turtle.Screen()
screen.bgpic("./Day25/us-states-game-start/blank_states_img.gif")
screen.screensize(725,491)
screen.title("U.S. States Game")

def create_turtle(state_name,x,y):
    state = turtle.Turtle()
    # state.shape("")
    state.hideturtle()
    state.penup()
    state.goto(x,y)
    state.pendown()
    state.write(state_name) 
def get_states_coordinates(name_of_state):
    state_xcor= data[data["state"]== name_of_state].x
    state_ycor= data[data["state"]== name_of_state].y
    xy_coordinates = []
    xy_coordinates.append(int(state_xcor))
    xy_coordinates.append(int(state_ycor))
    return xy_coordinates

correct_guessed_states = []

while player_score < TOTAL_SCORE:
    state_name = screen.textinput(f"{player_score}/{TOTAL_SCORE} State Correct","Enter a State Name: ")
    if state_name == "Exit" or state_name == "exit":
        # missing_state = []
        # for state in data["state"]:
        #      if state.lower() not in correct_guessed_states:
        #           missing_state.append(state)
        #list comprehension: this does same task as above 4 lines
        missing_state = [state for state in data["state"] if state.lower() not in correct_guessed_states] 
        new_dataframe = pd.DataFrame(missing_state) #convert list to dataframe
        new_dataframe.to_csv("./Day25/us-states-game-start/missing_states.csv") #create a csv for states name not guessed
        break #exit game
    for state in data["state"]:
        if state.lower() ==  state_name.lower() and state_name.lower() not in correct_guessed_states: #does not allow repeated entries of same state name
                player_score+=1
                correct_guessed_states.append(state.lower())
                xy_coordinates = get_states_coordinates(state)
                create_turtle(state,xy_coordinates[0],xy_coordinates[1])
# print(missing_state)
# print(correct_guessed_states)
# turtle.mainloop()
screen.exitonclick()