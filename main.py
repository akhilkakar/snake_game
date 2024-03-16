# created by Akhil Kakar
from turtle import Screen  # https://docs.python.org/3/library/turtle.html
from food import Food
from scoreboard import Scoreboard
import snake
import time

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_BACKGROUND_COLOR = "black"
KEY_UP = "Up"
KEY_DOWN = "Down"
KEY_LEFT = "Left"
KEY_RIGHT = "Right"

screen = Screen()
food = Food()
scoreboard = Scoreboard()

screen.setup(SCREEN_WIDTH , SCREEN_HEIGHT)
screen.bgcolor(SCREEN_BACKGROUND_COLOR)
screen.tracer(0)
new_snake = snake.Snake()

screen.listen()
screen.onkey(new_snake.up , KEY_UP)
screen.onkey(new_snake.down , KEY_DOWN)
screen.onkey(new_snake.left , KEY_LEFT)
screen.onkey(new_snake.right , KEY_RIGHT)

is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(0.1)
    new_snake.move()

    # collision detection
    if new_snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        new_snake.extend()

    # detect collision with wall
    if new_snake.head.xcor() > 280 or new_snake.head.xcor() < -280 or new_snake.head.ycor() > 280 or new_snake.head.ycor() < - 280:
        is_game_on = False
        scoreboard.game_over()

    # detect collision with tail
    for segment in new_snake.segments[1:0]:
        if new_snake.head.distance(segment) < 10:
            is_game_on = False
            scoreboard.game_over()

screen.exitonclick()
