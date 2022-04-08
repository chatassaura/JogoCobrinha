from turtle import Turtle


class Snake:
    def __init__(self):
        self.hole_snake = []
        self.width_snake = 3
        self.create_snake()
        self.way = 0
        self.head = self.hole_snake[0]

    def create_snake(self):
        for id_snake in range(self.width_snake):
            self.add_segment()

    def add_segment(self):
        snakes = Turtle("circle")
        snakes.penup()
        snakes.color("green")
        if len(self.hole_snake) > 1:
           snakes.goto(self.hole_snake[-1].pos())
        self.hole_snake.append(snakes)

    def extend(self):
        self.width_snake += 1
        self.add_segment()

    def automatic_move(self):

        for seg_num in range(len(self.hole_snake)-1, 0, -1):
            newx = self.hole_snake[seg_num-1].xcor()
            newy = self.hole_snake[seg_num-1].ycor()
            self.hole_snake[seg_num].goto(newx, newy)

        self.head.setheading(self.way)
        self.head.forward(20)

    def reset(self):
        for seg in self.hole_snake:
            seg.hideturtle()
        self.hole_snake.clear()
        self.width_snake = 3
        self.create_snake()
        self.head = self.hole_snake[0]

    def up(self):
        if self.head.heading() != 270:
            self.way = 90

    def down(self):
        if self.head.heading() != 90:
            self.way = 270

    def left(self):
        if self.head.heading() != 0:
            self.way = 180

    def right(self):
        if self.head.heading() != 180:
            self.way = 0
