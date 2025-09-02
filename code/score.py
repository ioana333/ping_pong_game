
from turtle import Turtle

ALIGN = "center"
FONT = ("Digital-7", 40, "normal")
FONT2 = ("Digital-7", 100, "normal")

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.player1Score = 0
        self.player2Score = 0
        self.writeScore()

    def increaseScore(self, player):
        if player == 1:
            self.player1Score += 1
        else:
            self.player2Score += 1
        self.writeScore()

    def writeScore(self):
        self.clear()
        self.goto(0, 250)
        self.write(f"{self.player2Score} - {self.player1Score}", align=ALIGN, font=FONT)

    def gameOver(self):
        self.clear()
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGN, font=FONT2)