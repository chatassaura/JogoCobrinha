# TODO 1 Create a snake body - 3 squares
# TODO 2 how to move the snake
# TODO 3 how to control the snake - with the buttons
# TODO 4 detect collision with food - add a score for food
# TODO 5 create a scoreboard
# TODO 6 detect collision with wall - game over
# TODO 7 detect collision with tail - game over
from snake import Snake
from turtle import Screen
from time import sleep
from food import Food
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

screen.tracer(0)
screen.listen()
snake = Snake()
scoreboard = Scoreboard()
food = Food()


screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

screen.update()

game_is_on = True
while game_is_on:
    screen.update()
    snake.automatic_move()
    sleep(0.1)

    # if collide with the dfood
    if snake.head.distance(food) < 15:
        scoreboard.add_score()
        food.refresh()
        snake.extend()
    scoreboard.show()

    # if collide with the wall
    if snake.head.xcor() > 290 or snake.head.ycor() < -290 or snake.head.xcor() < -290 or snake.head.ycor() > 290:
        scoreboard.reset()
        snake.reset()

    # if head collide with the tail - trigger game over
    for segment in snake.hole_snake[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()

screen.exitonclick()
