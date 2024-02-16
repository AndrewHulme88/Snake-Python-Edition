import turtle
import time
import snake
import food
import score

def setup_game():
    global screen 
    screen = turtle.Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("Snake - Python Edition")
    screen.tracer(0)

    global snake_obj, food_obj, score_obj
    snake_obj = snake.Snake()
    food_obj = food.Food()
    score_obj = score.Score()

    screen.listen()
    screen.onkey(snake_obj.up, "Up")
    screen.onkey(snake_obj.down, "Down")
    screen.onkey(snake_obj.left, "Left")
    screen.onkey(snake_obj.right, "Right")

def play_game():
    global game_running
    game_running = True
    while game_running:
        screen.update()
        time.sleep(0.1)
        snake_obj.move()

        if snake_obj.head.distance(food_obj) < 20:
            food_obj.refresh()
            snake_obj.extend()
            score_obj.update_score()

        if (
            snake_obj.head.xcor() > 280 
            or snake_obj.head.xcor() < -280 
            or snake_obj.head.ycor() > 280 
            or snake_obj.head.ycor() < -280
        ):
            game_running = False
            score_obj.game_over()
            replay_game()
          

        for segment in snake_obj.segments:
            if segment == snake_obj.head:
                pass
            elif snake_obj.head.distance(segment) < 10:
                game_running = False
                score_obj.game_over()
                replay_game()

 

def replay_game():
    replay = screen.textinput("Game Over", "Do you want to play again? (yes/no)").lower()
    if replay != "yes":
        exit()
    else:
        screen.clear()
        snake_obj.reset()
        food_obj.reset()
        score_obj.reset()
        setup_game()
        play_game()

setup_game()
play_game()
screen.exitonclick()