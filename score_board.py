from turtle import Turtle, Screen
import time
window = Screen()

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('azure')
        self.penup()
        self.goto(0,230)
        self.hideturtle()
        self.update_score()
        
    def update_score(self):
        self.goto(0, 250)
        self.color('azure')
        self.write(f"Score: {self.score}", align='center', font=('arial', 20, 'normal'))

    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_score()
    
    def game_over(self):
        self.goto(0,0)
        time.sleep(1.5)
        window.clear()
        window.bgcolor('bisque4')
        self.color('azure')
        self.write(f" Game Over\n\nFinal Score: {self.score}", align='center', font=('arial', 20, 'bold'))

        
    