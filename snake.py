from turtle import Turtle, Screen
import random, time

window = Screen()
window.tracer(0)

class Snake:
    def __init__(self):
        self.turtles = []
        self.positions = ((-40,0),(-20,0),(0,0),(20,0),(40,0))
        self.create_snake()
        self.head = self.turtles[-1]
    
    def create_snake(self):
        for i in range(len(self.positions)):
            new_turtle = Turtle('square')
            new_turtle.penup()
            new_turtle.color('white')
            new_turtle.goto(self.positions[i])
            self.turtles.append(new_turtle)
 
    def move(self):
        for i in range(len(self.turtles)-1):
            self.turtles[i].goto(self.turtles[i + 1].pos())
        self.head.forward(20)
        window.update()
        time.sleep(0.08)
        
    def tail(self):
        new_segment = Turtle('square')
        new_segment.penup()
        new_segment.color('white')
        new_segment.goto(self.turtles[0].pos())
        self.turtles.insert(0, new_segment)

    def right(self):
        self.head.setheading(0)
    def down(self):
        self.head.setheading(270)
    def left(self):
        self.head.setheading(180)
    def up(self):
        self.head.setheading(90)



