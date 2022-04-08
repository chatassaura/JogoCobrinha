from turtle import Turtle
FONT = ('courier', 18, 'bold')
ALIGNMENT = 'center'


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.speed('fastest')
        self.scores = 0
        self.high_score = 0
        self.f_h_score = 0
        self.color("red")
        self.penup()
        self.hideturtle()
        self.goto(x=0, y=250)
        self.show()

    def show(self):
        self.clear()
        with open("../files/my_score.txt") as self.f_h_score:
            self.high_score = self.f_h_score.read()
        self.write(arg=f"Score: {self.scores} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def add_score(self):
        self.scores += 1

    def reset(self):
        if self.scores > int(self.high_score):
            with open("../files/my_score.txt", mode='w') as self.f_h_score:
                self.f_h_score.write(str(self.scores))
        self.scores = 0
        self.show()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(arg="GAME OVER!", align=ALIGNMENT, font=FONT)
