from time import sleep
from turtle import Screen
from player import Player
from ball import Ball
from score import Score

screen = Screen()

screen.setup(800, 600)
screen.tracer(0)
screen.bgcolor("black")
screen.title("PING - PONG")

player1 = Player()
player2 = Player()

screen.listen()
screen.onkeypress(player1.up, "Up")
screen.onkeypress(player1.down, "Down")
screen.onkeypress(player2.down, "s")
screen.onkeypress(player2.up, "w")

ball = Ball()
score = Score()

gameOn = True
while gameOn:
    sleep(ball.moveSpeed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounceY()

    if ball.distance(player1) < 50 and ball.xcor() > 320 or  ball.distance(player2) < 50 and ball.xcor() < -320:
        ball.bounceX()

    if ball.xcor() > 380:
        ball.resetPosition()
        score.increaseScore(2)

    if ball.xcor() < -380:
        ball.resetPosition()
        score.increaseScore(1)

    if score.player1Score == 10 or score.player2Score == 10:
        score.gameOver()
        gameOn = False

screen.exitonclick()