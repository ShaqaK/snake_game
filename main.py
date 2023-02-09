import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import  Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Swish Swish Bish')

# Turning off the tracer
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

game_is_on = True

while game_is_on:
    # Snake body will show up in one piece
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect Collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect Collision with wall
    if snake.head.xcor() > 281 or snake.head.xcor() < -281 or snake.head.ycor() > 281 or snake.head.ycor() < -281:
        scoreboard.game_over()
        game_is_on = False

    # Detect Collision with tail
    for seg in snake.segments[1:]:
        if snake.head.distance(seg) < 10:
            scoreboard.game_over()
            game_is_on = False




screen.exitonclick()
