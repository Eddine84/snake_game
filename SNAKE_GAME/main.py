
#  SNAKE GAME 

from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food() 
score = Score()
screen.listen()


game_is_on = True

screen.onkey(key="Up",fun=snake.up)
screen.onkey(key="Left",fun=snake.left)
screen.onkey(key="Right",fun=snake.right)
screen.onkey(key="Down",fun=snake.down)
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refrech()
        score.increase_Score()
        snake.extend()
    
    if snake.head.xcor() > 280 or snake.head.xcor()< -280 or snake.head.ycor() > 280 or snake.head.ycor()< -280:
        score.reset()
        snake.reset()

     

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score.reset()
            snake.reset()

    
    

screen.exitonclick()













#  TURTLES RACE 

# import turtle
# import random
# is_race_start = False
# colors = ["red","orange","yellow", "green", "blue", "purple"]
# y_positions = [-70,-40,-10,20,50,80]
# turtles = []
# screen = turtle.Screen()
# screen.setup(width=500, height=400)
# user_bet = screen.textinput(title="Make your bet", prompt="which turtle will win the race? enter a color:  ")

# for index in range(0,6):
#     new_turtle = turtle.Turtle(shape="turtle")
#     new_turtle.color(colors[index])
#     new_turtle.penup()
#     new_turtle.goto(x=-230, y=y_positions[index])
#     turtles.append(new_turtle)

# if user_bet:
#     is_race_start = True

# distances = []
# while is_race_start:

#     for index, new_turtle in enumerate(turtles):
#         if new_turtle.xcor() > 210:
#             turtle_winner = new_turtle.pencolor()
#             if user_bet == turtle_winner:
#                 print("you win ")
#             else:
#                 print("you loose")
#             is_race_start = False

#         random_distance = random.randint(0,10)
#         new_turtle.forward(random_distance)   
            


# screen.listen()
# screen.exitonclick()