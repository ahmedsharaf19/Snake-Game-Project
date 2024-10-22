from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Snake Game ")
screen.bgcolor('black')
screen.tracer(0)

player_name = screen.textinput(title="Snake Game (Ahmed Sharaf)", prompt=("Enter Player Name "))

score = Score(player_name)
snake = Snake()
food = Food()
screen.listen()
screen.onkey(snake.Up, 'Up')
screen.onkey(snake.Down, 'Down')
screen.onkey(snake.Right, 'Right')
screen.onkey(snake.Left, 'Left')

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.Move()

    # Eating Food
    if snake.head.distance(food) < 15:
        food.set_food()
        snake.big_snake()
        score.increase_score(player_name)
        
    # Collision With The Wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -285 or snake.head.ycor() > 280 or snake.head.ycor() < -285:
        game_is_on = False
        score.game_over()

    # Collision With The Tail
    for segment_snake in snake.squares_seg[1:]:
        if snake.head.distance(segment_snake) < 10:
            game_is_on = False
            score.game_over()
            break


screen.exitonclick()