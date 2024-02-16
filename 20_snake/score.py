from turtle import Turtle



class Score(Turtle):

    score = 0

    def __init__(self):
        super().__init__()

        self.color("white")
        self.hideturtle()
        self.penup()
        self.speed("fastest")
        self.goto(0, 270)
        self.write("Score: " + str(self.score), align="center", font=("Courier", 20, "normal"))

    def game_over(self):
        self.goto(0, 50)
        self.write("GAME OVER", align="center", font=("Courier", 30, "normal"))

    def update_score(self):
        self.clear()
        self.score += 1
        self.write("Score: " + str(self.score), align="center", font=("Courier", 20, "normal"))