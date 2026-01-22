from turtle import Screen, Turtle
from food import Food 
from snake import Snake
from score_board import Scoreboard
import time, os, random

window = Screen()
window.bgcolor('bisque4')
window.setup(width=1000, height=550)
window.title('لعبة الثعبان - في الطريق الى القمة ')

# حدود الحلبة
for i in range(1):
    borderer = Turtle()
    borderer.pensize(10)
    borderer.penup()
    borderer.color('orange')
    borderer.hideturtle()
    borderer.goto(540,299)
    borderer.pendown()
    borderer.goto(-540,299)
    borderer.goto(-540,-299)
    borderer.goto(540,-299)
    borderer.goto(540,299)

omer = Snake()
eat = Food()
score = Scoreboard()

on_go = True
while on_go:
    omer.move()
    window.listen()
    window.onkey(omer.up, "Up")
    window.onkey(omer.down, "Down")
    window.onkey(omer.right, "Right")
    window.onkey(omer.left, "Left")

    if omer.head.distance(eat) < 15:
        eat.random_place()
        omer.tail()
        score.increase_score()    
        
    if omer.head.xcor() > 500 or omer.head.xcor() < -500 or omer.head.ycor() > 270 or omer.head.ycor() < -270:
        on_go = False
        score.game_over()

    # الاصطدام بالذيل

    for i in omer.turtles[:-1]:
        if omer.head.distance(i) < 10:
            on_go = False
            score.game_over()



window.exitonclick()
