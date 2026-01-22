from turtle import Turtle
import random 

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.color('orange')
        self.penup()
        self.shape('circle')
        self.shapesize(0.5,0.5)
        self.random_place()
    
    def random_place(self):
        randomx = random.randint(-200,200)
        randomy = random.randint(-200,200)
        self.goto(randomx, randomy)