import time
from turtle import Screen, Turtle
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Swish Swish Bish')
# Turning off the tracer
screen.tracer(0)

snake = Snake()

game_is_on = True
while game_is_on:
    # Snake body will show up in one piece
    screen.update()
    time.sleep(0.1)
    snake.move()













screen.exitonclick()