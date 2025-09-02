
from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.shapesize(1, 1)
        self.goto(0, 0)
        self.xMove = 10
        self.yMove = 10
        self.moveSpeed = 0.1

    def move(self):
        x = self.xcor() + self.xMove
        y = self.ycor() + self.yMove
        self.goto(x, y)

    def bounceY(self):
        self.yMove *= -1

    def bounceX(self):
        self.xMove *= -1
        self.moveSpeed *= 0.8

    def resetPosition(self):
        self.goto(0, 0)
        self.bounceX()
        self.moveSpeed = 0.1