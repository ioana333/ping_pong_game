from turtle import Turtle

numberOfPlayers = 0

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(5, 1)
        global numberOfPlayers
        numberOfPlayers += 1
        self.setPlayer()

    def setPlayer(self):
        if numberOfPlayers == 1:
            self.teleport(350, 0)
        elif numberOfPlayers == 2:
            self.teleport(-350, 0)
        else:
            del self

    def up(self):
        x = self.xcor()
        y = self.ycor() + 20
        if y < 250:
            self.goto(x, y)

    def down(self):
        x = self.xcor()
        y = self.ycor() - 20
        if y > -250:
            self.goto(x, y)