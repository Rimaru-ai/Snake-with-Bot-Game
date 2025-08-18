from turtle import Turtle
import random


STARTING_POSITIONS = ((0, 0), (-20, 0), (-40, 0))
MOVE_DISTANCE = 20
COLOR = "white"


class Snake:

    def __init__(self, start_positions=STARTING_POSITIONS, color=COLOR):
        self.segments = []
        self.create_snake(start_positions,color)

    def create_snake(self, start_positions, color):
        for position in start_positions:
            new_segment = Turtle("square")
            new_segment.color(color)
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def reset(self, start_positions=None):
        # Hide old segments
        for segment in self.segments:
            segment.goto(1000, 1000)  # move off screen
        self.segments.clear()

        # Pick a new random start if none is given
        if not start_positions:
            x = random.randint(-200, 200)
            y = random.randint(-200, 200)
            start_positions = [(x, y), (x - 20, y), (x - 40, y)]

        # Create new snake
        self.create_snake(start_positions,"red")

    def grow(self,color):
        # Add a new segment to the snake at the position of the last segment
        last_segment = self.segments[-1]
        new_segment = Turtle("square")
        new_segment.color(color)
        new_segment.penup()
        new_segment.goto(last_segment.position())
        self.segments.append(new_segment)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def move_towards(self, target):
        if self.head.xcor() < target.xcor() and self.head.heading() != 180:
            self.go_right()
        elif self.head.xcor() > target.xcor() and self.head.heading() != 0:
            self.go_left()
        elif self.head.ycor() < target.ycor() and self.head.heading() != 90:
            self.go_up()
        elif self.head.ycor() > target.ycor() and self.head.heading() != 270:
            self.go_down()
        self.move()

    def go_right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)

    def go_left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)

    def go_up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)

    def go_down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)

    @property
    def head(self):
        return self.segments[0]
