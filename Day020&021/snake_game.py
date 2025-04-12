from turtle import Turtle, Screen
from snake import Snake
import time
from Food import khana
from scoreboard import Score_Board

screen = Screen()
screen.title("Snake Game")
screen.setup(width = 600,height = 600)
screen.bgcolor("black")
screen.tracer(0)

snake = Snake() 
food = khana()
score = Score_Board()

screen.listen()
screen.onkey(key= "Up", fun = snake.upward)
screen.onkey(key= "Right", fun =snake.right)
screen.onkey(key= "Left", fun = snake.left)
screen.onkey(key= "Down", fun = snake.downward)

game_on_hai = True
number_of_contacts = 0
while game_on_hai:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # to detect contact btw the snake and food
    if snake.head.distance(food) < 15: #bc since food is at a size 10x10
        food.new_location()
        snake.extend_snake()
        score.increase_score() # keeping track of score
    
    # detect collisioon with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 295 or snake.head.ycor() < -290: # after coordinats 280,-280 we get wall of screen
        game_on_hai = False                              # i have written 295 bc gameover came even before contact near upper wall
        score.game_over()
    
    # detect collision with tail
    # for x in snake.all_3_squares_for_snake: 
        # if x != snake.head and snake.head.distance(x) < 10:#since the snake.head and all_3_sqaure[0] is same so this will cause issue

    for x in snake.all_3_squares_for_snake[1:]: # through list slicing we avoid writing the if x != snake.head statement       
        if  snake.head.distance(x) < 10:
            game_on_hai = False
            score.game_over()

screen.exitonclick()