import random
from turtle import Turtle

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len = 0.5, stretch_wid = 0.5)
        self.color("white")
        self.speed("fastest")
        self.goto(random.randint(-280,280), random.randint(-280,280))

    def refresh(self, snake_segments):
        while True:
            x = random.randint(-280, 280)
            y = random.randint(-280, 280)
            pos = (x, y)
            # Avoid spawning on snake body
            if all(segment.distance(pos) > 15 for segment in snake_segments):
                self.goto(pos)
                break


