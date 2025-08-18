import random
from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)

snake = Snake()
ai_snake = Snake(start_positions=[(100, 0), (80, 0), (60, 0)], color="red")
food = Food()
scoreboard = Scoreboard()

# Key bindings
screen.listen()
screen.onkey(snake.go_up, "Up")
screen.onkey(snake.go_down, "Down")
screen.onkey(snake.go_left, "Left")
screen.onkey(snake.go_right, "Right")


ai_step = 0

# Game loop
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    ai_step += 1
    if ai_step % 3 != 0:
        ai_snake.move_towards(food)

    #Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh(snake.segments)
        snake.grow("white")
        scoreboard.increase_score()

    # Detect collision with food for ia
    if ai_snake.head.distance(food) < 15:
        food.refresh(ai_snake.segments)
        ai_snake.grow("red")

    # Check for player collision with wall
    head = snake.segments[0]
    if abs(head.xcor()) > 290 or abs(head.ycor()) > 290:
        game_is_on = False

    #Player collision with itself
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False

    # Check AI collision with wall
    ai_head = ai_snake.head
    if abs(ai_head.xcor()) > 290 or abs(ai_head.ycor()) > 290:
        ai_snake.reset()

    # AI collision with itself
    for segment in ai_snake.segments[1:]:
        if ai_snake.head.distance(segment) < 10:
            ai_snake.reset()

    # ----- PLAYER hits AI BODY (Game Over) -----
    for segment in ai_snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False

    # ----- AI hits PLAYER BODY (AI dies + respawns + bonus points) -----
    for segment in snake.segments[1:]:
        if ai_snake.head.distance(segment) < 10:
            ai_snake.reset()
            scoreboard.bonus_points(2)
    # Head to head collision
    if snake.head.distance(ai_snake.head) < 10:
        game_is_on = False  # or ai_snake.reset() + scoreboard.bonus_points(2)

scoreboard.game_over()
screen.exitonclick()
