from turtle import Turtle
ALIGNEMENT = "center"
FONT = ("Courier",24,"normal")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,250)
        self.score = 0
        with open("data.txt") as data:
            self.height_score = int(data.read())
        
        self.update_score()
    
    def update_score(self):
        self.clear()
        self.write(f"Score:{self.score} High Score: {self.height_score}", align=ALIGNEMENT ,font=FONT)

    def reset(self):
        if self.score > self.height_score:
            self.height_score = self.score
            with open("data.txt",mode="w") as data:
                data.write(f"{self.height_score}")
            self.score = 0
            self.update_score()
    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER", align=ALIGNEMENT ,font=FONT)


    def increase_Score(self):
        self.score+=1
        self.update_score()
        
    