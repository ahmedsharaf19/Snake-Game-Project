from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:
    squares_seg = []
    def __init__(self):
        self.create_snake()
        self.head = self.squares_seg[0]
    
    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_tim = Turtle('square')
            new_tim.color('green')
            new_tim.penup()
            new_tim.goto(position)
            self.squares_seg.append(new_tim)
    
    def big_snake(self):
            new_tim = Turtle('square')
            new_tim.color('green')
            new_tim.penup()
            new_tim.goto(self.squares_seg[-1].xcor() - 20, self.squares_seg[-1].ycor())
            self.squares_seg.append(new_tim)

    def Move(self):
        for seg_num in range(len(self.squares_seg) - 1, 0, -1):
            self.squares_seg[seg_num].goto(self.squares_seg[seg_num - 1].xcor(),self.squares_seg[seg_num - 1].ycor())
        self.head.forward(MOVE_DISTANCE)

    def Up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    
    def Down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def Right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def Left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)